import datetime
import db
import json
import jwt
from flask import request, json, Response, make_response

from auth import validatePassword
from models import User, Car, MaintenanceEntry
from settings import JWT_SECRET


def buildResponse(body, status):
    return Response(response=body, status=status, mimetype='application/json')

def requiresJWT():
    
    jwt_token = request.headers.get('authorization', None)
    if not jwt_token:
        return buildResponse(body=json.dumps({'message': 'Token is missing'}), status=401)
   
    jwt_token = jwt_token[7:]
    if jwt_token:
        try:
            payload = jwt.decode(jwt_token, JWT_SECRET)
            return None, payload['user']
        except (jwt.DecodeError):
            return buildResponse(body=json.dumps({'message': 'Token is invalid'}), status=401), None
        except (jwt.ExpiredSignatureError):
            return buildResponse(body=json.dumps({'message': 'Token is expired'}), status=401), None  
        

def getUserInfo():
    session = db.Session()
    users = session.query(User)
    for user in users:
        if user.username == request.json['username']:
            session.close()
            return json.dumps({
                'username': user.username, 
                'last_name': user.last_name, 
                'email': user.email, 
                'first_name': user.first_name, 
            })

    session.close()
    return json.dumps({})


def addUser():
    req = request.json
   
    session = db.Session()
    users = session.query(User)
    for user in users:
        if user.username == req['username']:
            session.close()
            return buildResponse("Username already registered", 401)

    session.close()
    user = User(req['username'], req['password'], req['first_name'], req['last_name'], req['email'])
    db.addObject(user)
    return buildResponse("Username successfully registered", 200)

def addCar():
    validJWT, username = requiresJWT()
    if validJWT:
        return validJWT

    req = request.json
    if not req['make'] or not req['model'] or not req['year'] or not req['owner']:
         return buildResponse("Missing fields", 400)
    
    car = Car(req['make'], req['model'], req['trim'], req['year'], req['owner'])
    db.addObject(car)
    return buildResponse("Car successfully added", status=200)


def deleteCar():
    validJWT, username = requiresJWT()
    
    if validJWT:
        return validJWT
    req = request.json
    
    if not request.args.get('id'):
        return buildResponse("Missing car id", 400)

    db.removeCar(id=int (request.args.get('id')))
    
    return  buildResponse("Car successfully deleted", status=200)
    

def getCarsByOwner():
    validJWT, username = requiresJWT()
    if validJWT:
        return validJWT

    session = db.Session()
    cars = session.query(Car)
    
    cars_by_owner = []

    for car in cars:
        if car.owner == username:
            cars_by_owner.append({
                'make': car.make,
                'model': car.model,
                'trim': car.trim,
                'year' : car.year,
                'id': car.id
            })

    session.close()
    return buildResponse(body=json.dumps(cars_by_owner), status=200)


def addServiceRecord():
    req = request.json
    session = db.Session()
    cars = session.query(Car)
    session.close()
    valid_car_id = False
    for car in cars:
        if car.id == req['id']:
            valid_car_id = True
            break
    
    if valid_car_id:
        new_entry = MaintenanceEntry(req['id'], req['service'], req['mileage'], req['date'])
        db.addObject(new_entry)
        return "Entry successfully added"
    else:
        return "Car does not exist"


def getServiceRecords():
    session = db.Session()
    entries = session.query(MaintenanceEntry)
    
    carID = int (request.args.get('id'))
    entries_by_car = []

    for entry in entries:
        if entry.car_id == carID:
            entries_by_car.append({
                'car_id': entry.car_id,
                'service': entry.service,
                'mileage': entry.mileage,
                'date' : entry.date,
            })

    session.close()
    return entries_by_car


def userLogin():
    username = request.json['username']
    password = request.json['password']


    hashed_password = ""
    salt = "" 
    session = db.Session()
    users = session.query(User)
    for user in users:
        if user.username == request.json['username']:
            hashed_password = user.hashed_password
            salt = user.salt
            break
    
    session.close()

    if not hashed_password:
        return buildResponse("User not found", 404)
    if validatePassword(password, salt, hashed_password):
        token = jwt.encode({'user': username, 'exp': (datetime.datetime.utcnow() + datetime.timedelta(minutes=120))}, JWT_SECRET)
        return buildResponse(json.dumps({'token': token.decode('utf-8')}), 200)
    else:
        return buildResponse("User password incorrect", 401)

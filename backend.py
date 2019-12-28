import db
import json
from flask import request, json
from models import User, Car, MaintenanceEntry


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
    user = User(req['username'], req['password'], req['first_name'], req['last_name'], req['email'])
    db.addObject(user)
  


def addCar():
    req = request.json
    car = Car(req['make'], req['model'], req['trim'], req['year'], req['owner'])
    db.addObject(car)


def getCarsByOwner():
    req = request.json
    username = req['username']

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
                'owner': car.owner,
                'id': car.id
            })

    session.close()
    return cars_by_owner


def addServiceRecord():
    req = request.json
    session = db.Session()
    cars = session.query(Car)
    session.close()
    valid_car_id = False
    for car in cars:
        if car.id == req['car_id']:
            valid_car_id = True
            break
    
    if valid_car_id:
        new_entry = MaintenanceEntry(req['car_id'], req['service'], req['mileage'], req['date'])
        db.addObject(new_entry)
        return "Entry successfully added"
    else:
        return "Car does not exist"


def getServiceRecords():
    req = request.json
    session = db.Session()
    entries = session.query(MaintenanceEntry)
    
    entries_by_car = []

    for entry in entries:
        if entry.car_id == req['car_id']:
            entries_by_car.append({
                'car_id': entry.car_id,
                'service': entry.service,
                'mileage': entry.mileage,
                'date' : entry.date,
            })

    session.close()
    return entries_by_car
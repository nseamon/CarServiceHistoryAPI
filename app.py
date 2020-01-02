import json.encoder
from flask import Flask, request
from flask_cors import CORS

import backend 


app = Flask(__name__)
CORS(app)

@app.route("/users", methods=['GET'])
def getUserInfo():
	user_info = backend.getUserInfo()
	return(user_info)


@app.route("/users", methods=['POST'])
def createUser():
	return(backend.addUser())


@app.route("/cars", methods=['GET'])
def getCars():
	return(backend.getCarsByOwner())


@app.route("/cars", methods=['POST'])
def addCar():
	return(backend.addCar())

@app.route("/cars", methods=['DELETE'])
def deleteCar():
	return(backend.deleteCar())

@app.route("/service", methods=['POST'])
def addServiceRecord():
	return(backend.addServiceRecord())


@app.route("/service", methods=['GET'])
def getServiceRecords():
	return(json.dumps(backend.getServiceRecords()))


@app.route("/login", methods=['POST'])
def userLogin():
	return(backend.userLogin())


if __name__ == '__main__':
	app.run(debug=True)

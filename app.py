import json.encoder
from flask import Flask, request
from flask_cors import CORS

from settings import IS_PRODUCTION
import backend 

application = Flask(__name__)
CORS(application)

@application.route("/users", methods=['GET'])
def getUserInfo():
	user_info = backend.getUserInfo()
	return(user_info)


@application.route("/users", methods=['POST'])
def createUser():
	return(backend.addUser())


@application.route("/cars", methods=['GET'])
def getCars():
	return(backend.getCarsByOwner())


@application.route("/cars", methods=['POST'])
def addCar():
	return(backend.addCar())

@application.route("/cars", methods=['DELETE'])
def deleteCar():
	return(backend.deleteCar())

@application.route("/service", methods=['POST'])
def addServiceRecord():
	return(backend.addServiceRecord())


@application.route("/service", methods=['GET'])
def getServiceRecords():
	return(json.dumps(backend.getServiceRecords()))

@application.route("/service", methods=['DELETE'])
def deleteServiceRecord():
	return(backend.deleteEntry())

@application.route("/login", methods=['POST'])
def userLogin():
	return(backend.userLogin())


if __name__ == '__main__':
	if (IS_PRODUCTION):
		application.run(host="0.0.0.0")
	else:
		application.run(debug=True)

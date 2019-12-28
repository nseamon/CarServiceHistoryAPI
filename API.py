from flask import Flask, request
import backend 
import psycopg2
import json.encoder

app = Flask(__name__)


@app.route("/users", methods=['GET'])
def getUserInfo():
	user_info = backend.getUserInfo()
	return(user_info)


@app.route("/users", methods=['Post'])
def createUser():
	backend.addUser()
	return("200")


@app.route("/cars", methods=['GET'])
def getCars():
	return(json.dumps(backend.getCarsByOwner()))


@app.route("/cars", methods=['POST'])
def addCar():
	backend.addCar()
	return("200")


@app.route("/service", methods=['POST'])
def addServiceRecord():
	backend.addServiceRecord()
	return("")


@app.route("/service", methods=['GET'])
def getServiceRecords():
	return(json.dumps(backend.getServiceRecords()))


if __name__ == '__main__':
	app.run(debug=True)
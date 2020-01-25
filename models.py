import auth
import os
import random
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date


Base = declarative_base()

class User(Base):
    
    __tablename__ = 'users'
    username = Column(String, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    hashed_password = Column(String)
    salt = Column(String)

    def __init__(self, username, password, first_name, last_name, email):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
        salt, hashed_password = auth.generateSaltAndHash(password) 

        self.salt = salt
        self.hashed_password = hashed_password
    

class Car(Base):
    
    __tablename__ = 'cars'
    make = Column(String)
    model = Column(String)
    trim = Column(String)
    year = Column(Integer)
    id = Column(Integer, primary_key=True, unique=True)
    owner = Column(String)

    def __init__(self, make, model, trim, year, owner):
        self.make = make
        self.model = model
        self.trim = trim
        self.year = year
        self.owner = owner
        self.id = random.randint(0, 100000000)

class MaintenanceEntry(Base):

    __tablename__ = 'entries'
    record_id = Column(Integer, primary_key=True, unique=True)
    car_id = Column(Integer)
    service = Column(String)
    mileage = Column(Integer)
    date = Column(String)
    common_services = Column(String)

    def __init__(self, car_id, service, mileage, date, common_services=""):
        self.car_id = car_id
        self.mileage = mileage
        self.service = service
        self.record_id = random.randint(0, 100000000)
        self.date = date
        self.common_services = common_services

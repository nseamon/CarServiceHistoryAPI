from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings import RDS_URI

engine = create_engine(RDS_URI)

Session = sessionmaker(bind=engine)

import models
models.Base.metadata.create_all(engine)

def addObject(object_too_add):
    session = Session()
    session.add(object_too_add)
    session.commit()
    session.close()

def removeCar(id):
    engine.execute("DELETE FROM entries where car_id={};".format(id))
    engine.execute("DELETE FROM cars where id={};".format(id))

def removeEntry(id):
     engine.execute("DELETE FROM entries where record_id={};".format(id))
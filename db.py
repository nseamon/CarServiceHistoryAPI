from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgres+psycopg2://Nathan:@localhost:5432/backend')
Session = sessionmaker(bind=engine)


def addObject(object_too_add):
    session = Session()
    session.add(object_too_add)
    session.commit()
    session.close()

def removeCar(id):
    engine.execute("DELETE FROM entries where car_id={};".format(id))
    engine.execute("DELETE FROM cars where id={};".format(id))
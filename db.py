import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('postgres+psycopg2://Nathan:@localhost:5432/backend')
Session = sessionmaker(bind=engine)


def addObject(obj):
    session = Session()
    session.add(obj)
    session.commit()
    session.close()
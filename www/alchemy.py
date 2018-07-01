# 导入:
import json

from sqlalchemy import Column, String, Integer, Float, Boolean, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class users(Base):
    __tablename__ = 'Users'

    User_ID = Column(Integer, primary_key=True)
    user_passwd = Column(String(50))
    admin = Column(Boolean)
    user_name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(50))
    records_number = Column(Integer)
    last_record_date = Column(Integer)
    create_at = Column(Float)

class records(Base):
    __tablename__ = 'Records'

    Record_ID = Column(Integer, primary_key=True)
    pain_number = Column(Integer)
    record_brief = Column(String(50))
    create_at = Column(Float)

class pains(Base):
    __tablename__ = 'Pains'

    Pain_ID = Column(Integer,primary_key=True)
    region_count = Column(Integer)
    description = Column(String(500))
    pain_character = Column(String(50))
    pain_severity = Column(Integer)
    depth = Column(String(50))
    frequency = Column(String(50))

class regions(Base):
    __tablename__ = 'Regions'

    Region_ID = Column(Integer,primary_key=True)
    region_severity = Column(Integer)
    cells_count = Column(Integer)

class cells(Base):
    __tablename__ = 'Cells'

    Cells_ID = Column(Integer, primary_key=True)
    cell_severity = Column(Integer)
    selected = Column(Boolean)

def tojson(self):
    if isinstance(self, users):
        return {
            'id': self.User_ID,
            'name': self.user_name,
            'age': self.age,
            'gender': self.gender
        }
    else:
        return {
            'id': self.User_ID,
            'name': self.user_name,
        }



engine = create_engine('mysql+mysqlconnector://ubuntu:ubuntu@localhost:3306/throughmypain')
DBSession = sessionmaker(bind=engine)

session=DBSession()
#new_user=users(User_ID = 4, user_passwd = '123456', gender='female', age=22, create_at=20180630.1818, admin=False, last_record_date=30, records_number=4 ,user_name = 'Jan')
#session.add(new_user)
#session.commit()
#session.close()

urs = session.query(users).all()
print('user type :', type(urs))
print(urs)
print('---------------------------')
u = session.query(users).filter(users.User_ID == '2').all()
print(u)
print(json.dumps(urs, default=tojson,indent=4))
session.close()
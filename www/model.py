# 导入:
import json

# from sqlalchemy import Column, String, Integer, Float, Boolean, create_engine, ForeignKey
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import time
from sqlalchemy.inspection import inspect
# Base = declarative_base()

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost:3306/throughmypain'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
db = SQLAlchemy()




class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class users(db.Model):
    __tablename__ = 'Users'

    User_ID = db.Column(db.String(50), primary_key=True)
    user_name = db.Column(db.String(50))
    user_passwd = db.Column(db.String(50))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(50))
    pains_number = db.Column(db.Integer)
    last_record_date = db.Column(db.String(50))
    create_at = db.Column(db.String(50))
    admin = db.Column(db.Boolean)

    def __init__(self, User_ID, user_name, user_passwd, age, gender, pains_number = 0, last_record_date = 'No record', create_at = time.strftime('%Y-%h-%d %H:%M',time.localtime(time.time())), admin = False):
        self.User_ID = User_ID
        self.user_name = user_name
        self.user_passwd = user_passwd
        self.age = age
        self.gender = gender
        self.pains_number = pains_number
        self.last_record_date = last_record_date
        self.create_at = create_at
        self.admin = admin

    def serialize(self):
        d = Serializer.serialize(self)
        return d
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d
    
    def __repr__(self):
        return self.user_name


# def dump_datetime(value):
#     """Deserialize datetime object into string form for JSON processing."""
#     if value is None:
#         return None
#     return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]

class records(db.Model):
    __tablename__ = 'Records'

    Record_ID = db.Column(db.String(50), primary_key=True)
    pain_number = db.Column(db.Integer)
    record_brief = db.Column(db.String(100))
    create_at = db.Column(db.String(50))
    pains_list = db.Column(db.String(20000))
    User_ID = db.Column(db.String(50), db.ForeignKey('Users.User_ID'))

    def __init__(self, Record_ID, pain_number, record_brief, pains_list, User_ID_record, create_at=time.strftime('%Y-%h-%d %H:%M',time.localtime(time.time()))):
        self.Record_ID = Record_ID
        self.pain_number = pain_number
        self.record_brief = record_brief
        self.pains_list = pains_list
        self.create_at = create_at
        self.User_ID = User_ID_record
    
    def serialize(self):
        d = Serializer.serialize(self)
        # del d['password']
        return d
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d

    def __repr__(self):
        return '<Record %r>' % self.Record_ID

class record_cache(db.Model):
    __tablename__ = 'Record_cache'

    Record_ID = db.Column(db.String(50), primary_key=True)
    record_brief = db.Column(db.String(100))
    pain_list = db.Column(db.String(21845))

    def __init__(self, Record_ID, record_brief, pain_list):
        self.Record_ID = Record_ID
        self.record_brief = record_brief
        self.pain_list = pain_list
    
    def serialize(self):
        d = Serializer.serialize(self)
        # del d['password']
        return d
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d

    def __repr__(self):
        return '<Record_cache %r>' % self.Record_ID

class pains(db.Model):
    __tablename__ = 'Pains'

    Pain_ID = db.Column(db.String(50),primary_key=True)
    region_count = db.Column(db.Integer)
    regions = db.Column(db.String(100))
    description = db.Column(db.String(500))
    pain_character = db.Column(db.String(50))
    pain_severity = db.Column(db.Integer)
    depth = db.Column(db.String(50))
    frequency = db.Column(db.String(50))
    create_at = db.Column(db.String(50))
    # Record_ID = db.Column(db.String(50), db.ForeignKey('Records.Record_ID'))
    Users_User_ID = db.Column(db.String(50), db.ForeignKey('Users.User_ID'))

    def __init__(self, Pain_ID, region_count, regions, description, pain_character, pain_severity, depth, frequency, User_ID_pain, create_at=time.strftime('%Y-%h-%d %H:%M',time.localtime(time.time()))):
        self.Pain_ID = Pain_ID
        self.region_count = region_count
        self.regions = regions
        self.description = description
        self.pain_character = pain_character
        self.pain_severity = pain_severity
        self.depth = depth
        self.frequency = frequency
        self.create_at = create_at
        # self.Record_ID = Record_ID_pain
        self.Users_User_ID = User_ID_pain

    def serialize(self):
        d = Serializer.serialize(self)
        # del d['password']
        return d
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d
    
    def __repr__(self):
        return '<Pain %r>' % self.Pain_ID

class regions(db.Model):
    __tablename__ = 'Regions'

    Region_ID = db.Column(db.String(50),primary_key=True)
    region_severity = db.Column(db.Integer)
    cells_count = db.Column(db.Integer)

    def __init__(self, Region_ID, region_severity, cells_count):
        self.Region_ID = Region_ID
        self.region_severity = region_severity
        self.cells_count = cells_count
    
    def __repr__(self):
        return '<Region %r>' % self.Region_ID

class cells(db.Model):
    __tablename__ = 'Cells'

    Cells_ID = db.Column(db.String(50), primary_key=True)
    cell_severity = db.Column(db.Integer)
    selected = db.Column(db.Boolean)

    def __init__(self, Cells_ID, cell_severity, selected):
        self.Cells_ID = Cells_ID
        self.cell_severity = cell_severity
        self.selected = selected
    
    def __repr__(self):
        return '<Cell %r>' % self.Cells_ID

class reports(db.Model):
    __tablename__ = 'Reports'

    Report_ID = db.Column(db.String(50), primary_key=True)
    chart_number = db.Column(db.Integer)
    create_at = db.Column(db.String(50))
    User_ID = db.Column(db.String(50), db.ForeignKey('Users.User_ID'))

    def __init__(self, Report_ID, chart_number, create_at,User_ID):
        self.Report_ID = Report_ID
        self.chart_number = chart_number
        self.create_at = create_at
        self.User_ID = User_ID
    
    def serialize(self):
        d = Serializer.serialize(self)
        # del d['password']
        return d
    def serialize_list(self):
        d = Serializer.serialize_list(self)
        return d
    def __repr__(self):
        return '<Cell %r>' % self.Cells_ID

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:password@localhost:3306/throughmypain'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

# engine = create_engine('mysql+mysqlconnector://ubuntu:ubuntu@localhost:3306/throughmypain')
# DBSession = sessionmaker(bind=engine)

# session=DBSession()
#new_user=users(User_ID = 4, user_passwd = '123456', gender='female', age=22, create_at=20180630.1818, admin=False, last_record_date=30, records_number=4 ,user_name = 'Jan')
#session.add(new_user)
#session.commit()
#session.close()

# urs = session.query(users).all()
# print('user type :', type(urs))
# print(urs)
# print('---------------------------')
# u = session.query(users).filter(users.User_ID == '2').all()
# print(u)
# print(json.dumps(urs, default=tojson,indent=4))
# session.close()

# db.create_all()
# demo = pains(2, 2, 'right hand lower wisdom tooth is inflamed', 'stiffness', 1, 'neural', 'constant', 2, 10)
# db.session.add(demo)
# db.session.commit()
# # app = create_app()
# a = Users.query.filter_by(user_name="asd").first()
# print(a.age)
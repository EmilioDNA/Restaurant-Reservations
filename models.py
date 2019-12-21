import os
from flask_sqlalchemy import SQLAlchemy
import json
import datetime

database_name= "reservations"
database_path = "postgres://{}@{}/{}".format('postgres:postgres', 'localhost:5433', database_name)


db = SQLAlchemy()


'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


def convert_string_datetime(datetime_str):
    return datetime.datetime.strftime(datetime_str, "%Y-%m-%d %H:%M:%S")

''' This is just a sample model in case that the Auth0 params should be stored locally'''
# class User(db.Model):
#     __tablename__ = 'User'

#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)
#     role_id= Connect to the other table

# class Role(db.Model):
#     __tablename__ = 'role'

#     id = Column(Integer, primary_key=True)
#     role = Column(String)
#     permissions = Column(String)

''' This is the Restaurant model that includes diverse fields. 
    It has a One to Many relationship with DinningTable
    One Restaurant may have many Tables, but a Table only belongs to one Restaurant
'''
class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    address = db.Column(db.String)
    phone = db.Column(db.String)
    image_link = db.Column(db.String)
    tables = db.relationship('DinningTable', backref='restaurant', lazy=True)

    def __init__(self, title, city, state, address, phone, image_link):
        self.title = title
        self.city = city
        self.state = state 
        self.address = address
        self.phone = phone
        self.image_link = image_link

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def format(self):
        return {
            'id': self.id,
            'title': self.title,
            'city': self.city,
            'state': self.state,
            'address': self.address,
            'phone': self.phone,
            'image_link': self.image_link,
        }


'''
    This is the the table that connects the Reservation with the DinningTable 
    in a Many to Many relationship.
    One Reservation may have multiple DinningTables 
    One DinningTable may be in multiple Reservations (as long as the tables are available, which relies on the start and end time of the reservation).
    This limitations will be implemented in the controller to avoid that a user reserves a table in the same period of time.
'''
reservation_tables = db.Table('reservation_tables',
    db.Column('reservation_id', db.Integer, db.ForeignKey('reservation.id'), primary_key=True),
    db.Column('dinning_table_id', db.Integer, db.ForeignKey('dinning_table.id'), primary_key=True)
    )

'''
    This is the Reservation model that is related in a Many to Many relationship to the DinningTable model
'''
class Reservation(db.Model):
    __tablename__ = 'reservation'

    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime())
    end_time = db.Column(db.DateTime())
    dinning_tables = db.relationship('DinningTable', secondary=reservation_tables,
                        backref=db.backref('reservations', lazy=True))

    
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()    

    def format(self):
        return {
            'id': self.id,
            'start_time': convert_string_datetime(self.start_time),
            'end_time': convert_string_datetime(self.end_time)
        }

    @property
    def display_dinning_tables(self):
        dinning_tables = self.dinning_tables 

        return {
            'id': self.id,
            'start_time': convert_string_datetime(self.start_time),
            'end_time': convert_string_datetime(self.end_time),
            'dinning_tables': [dinning_table.format() for dinning_table in dinning_tables]
        }

'''
    This is the DinningTable model that is related in a Many to Many relationship to the Reservation model
    It is also related to the Restaurant model in a Many to One relationship (Multiple tables may be part of one Restaurant)
'''
class DinningTable(db.Model):
    __tablename__ = 'dinning_table'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String)
    capacity = db.Column(db.Integer)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)

    def __init__(self, code, capacity, restaurant_id):
        self.code = code,
        self.capacity = capacity,
        self.restaurant_id = restaurant_id
    
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'code': self.code,
            'capacity': self.capacity,
            'restaurant_id': self.restaurant_id
        }

    @property
    def display_reservations(self):
        reservations = self.reservations 

        return {
            'id': self.id,
            'code': self.code,
            'reservations': [reservation.format() for reservation in reservations]
        }

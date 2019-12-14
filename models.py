import os
from sqlalchemy import Table, Column, String, Integer, ForeignKey, Datetime, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name= "reservations"
database_path = "postges://{}@{}/{}".format('postgres:postgres', 'localhost:5433', database_name)


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

''' This is just a sample model in case that the Auth0 params should be stored locally'''
# class User(db.Model):
#     __tablename__ = 'User'

#     id = Column(Integer, primary_key=True)
#     username = Column(String)
#     password = Column(String)
#     rol = Column(String)
#     permissions = Column(String)

''' This is the Restaurant model that includes diverse fields. 
    It has a One to Many relationship with DinningTable
    One Restaurant may have many Tables, but a Table only belongs to one Restaurant
'''
class Restaurant(db.Model):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    city = Column(String)
    state = Column(String)
    address = Column(String)
    phone = Column(String)
    image_link = Column(String)
    tables = db.relationship('DinningTable', backref='restaurant', lazy=True)

'''
    This is the the table that connects the Reservation with the DinningTable 
    in a Many to Many relationship.
    One Reservation may have multiple DinningTables 
    One DinningTable may be in multiple Reservations (as long as the tables are available, which relies on the start and end time of the reservation).
    This limitations will be implemented in the controller to avoid that a user reserves a table in the same period of time.
'''
reservation_tables = Table('reservation_tables',
    Column('reservation_id', Integer, ForeignKey('reservation.id'), primary_key=True),
    Column('dinning_table_id', Integer, ForeignKey('dinning_table.id'), primary_key=True)
    )


'''
    This is the Reservation model that is related in a Many to Many relationship to the DinningTable model
'''
class Reservation(db.Model):
    __tablename__ = 'reservation'

    id = Column(Integer, primary_key=True)
    start_time = Column(Datetime())
    end_time = Column(Datetime())
    dinning_tables = db.relationship('DinningTable', secondary=reservation_tables,
                        backref=db.backref('order', lazy=True))

'''
    This is the DinningTable model that is related in a Many to Many relationship to the Reservation model
    It is also related to the Restaurant model in a Many to One relationship (Multiple tables may be part of one Restaurant)
'''
class DinningTable(db.Model):
    __tablename__ = 'dinning_table'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    capacity = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'), nullable=False)






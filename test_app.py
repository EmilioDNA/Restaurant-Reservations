import os 
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Restaurant, DinningTable, Reservation


class ReservationTestCase(unittest.TestCase):
    '''This class represents the reservation test case'''

    def setUp(self):
        '''Define test variables and initialize the app.'''
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'reservations_test'
        self.database_path = "postgres://{}@{}/{}".format('postgres:postgres', 'localhost:5433', self.database_name)

        setup_db(self.app, self.database_path)

        # Creation test objects
        self.new_restaurant = {
            'title':'My Coffee Shop', 
            'city':'Comitan', 
            'state':'Chiapas', 
            'address': '1ra. Nte. #3545', 
            'phone':'4303923', 
            'image_link':'https://mycoffeebox.com'
        }

        self.new_dinning_table = {
            "code":"C001", 
            "capacity":4
        }

        self.new_reservation = {
            "start_time":"2019-12-22 12:40:00", 
            "end_time":"2019-12-22 15:40:00", 
            "dinning_table_codes":["C001"]
        }


        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            #self.db.drop_all()
            self.db.create_all()

    def tearDown(self):
        '''Executed after reach test'''
        pass


    ''' Tests for successful operation and for expected errors'''
    # Test Restaurant
    def test_get_restaurants(self):
        res = self.client().get('/restaurants')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_restaurants'])
        self.assertTrue(len(data['restaurants']))
        self.assertTrue(data['restaurants'])

    def test_get_paginated_restaurants(self):
        res = self.client().get('/restaurants?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_restaurants'])
        self.assertTrue(len(data['restaurants']))
        self.assertTrue(data['restaurants'])

    def test_404_sent_requesting_restaurant_beyond_valid_page(self):
        res = self.client().get('/restaurants?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_restaurant(self):
        res = self.client().post('/restaurants', json=self.new_restaurant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_restaurants'])
        self.assertTrue(len(data['restaurants']))

    def test_405_if_restaurant_created_not_allowed(self):
        res = self.client().post('/restaurants/23', json=self.new_restaurant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_update_restaurant(self):
        res = self.client().patch('/restaurants/1', json={"phone":"1234566"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])
        self.assertTrue(data['total_restaurants'])
        self.assertTrue(len(data['restaurants']))

    def test_404_update_if_restaurant_does_not_exist(self):
        res = self.client().patch('/restaurants/400', json={"phone":"1234566"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_restaurant(self):
        res = self.client().delete('/restaurants/17')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertTrue(data['total_restaurants'])
        self.assertTrue(len(data['restaurants']))

    def test_404_delete_if_restaurant_does_not_exist(self):
        res = self.client().delete('/restaurants/400')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Test DinningTable
    def test_get_dinning_tables(self):
        res = self.client().get('/restaurants/1/tables')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_dinning_tables'])
        self.assertTrue(len(data['dinning_tables']))
        self.assertTrue(data['dinning_tables'])

    def test_get_paginated_dinning_tables(self):
        res = self.client().get('/restaurants/1/tables?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_dinning_tables'])
        self.assertTrue(len(data['dinning_tables']))
        self.assertTrue(data['dinning_tables'])

    def test_404_sent_requesting_dinning_table_beyond_valid_page(self):
        res = self.client().get('/restaurants/1/tables?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_dinning_table(self):
        res = self.client().post('/restaurants/1/tables', json=self.new_dinning_table)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_dinning_tables'])
        self.assertTrue(len(data['dinning_tables']))

    def test_405_if_dinning_table_created_not_allowed(self):
        res = self.client().post('/restaurants/1/tables/23', json=self.new_dinning_table)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_update_dinning_table(self):
        res = self.client().patch('/restaurants/1/tables/2', json={"capacity":8})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])
        self.assertTrue(data['total_dinning_tables'])
        self.assertTrue(len(data['dinning_tables']))

    def test_404_update_if_dinning_table_does_not_exist(self):
        res = self.client().patch('/restaurants/1/tables/597', json={"capacity":8})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_dinning_table(self):
        res = self.client().delete('/restaurants/1/tables/12')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertTrue(data['total_dinning_tables'])
        self.assertTrue(len(data['dinning_tables']))

    def test_404_delete_if_dinning_table_does_not_exist(self):
        res = self.client().delete('/restaurants/1/tables/400')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    # Test Reservations
    def test_get_reservations(self):
        res = self.client().get('/restaurants/1/reservations')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_reservations'])
        self.assertTrue(len(data['reservations']))
        self.assertTrue(data['reservations'])

    def test_get_paginated_reservations(self):
        res = self.client().get('/restaurants/1/reservations?page=1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_reservations'])
        self.assertTrue(len(data['reservations']))
        self.assertTrue(data['reservations'])

    def test_404_sent_requesting_reservation_beyond_valid_page(self):
        res = self.client().get('/restaurants/1/reservations?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_new_reservation(self):
        res = self.client().post('/restaurants/1/reservations', json=self.new_reservation)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(data['total_reservations'])
        self.assertTrue(len(data['reservations']))

    def test_405_if_reservation_created_not_allowed(self):
        res = self.client().post('/restaurants/1/reservations/23', json=self.new_reservation)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')

    def test_update_reservation(self):
        res = self.client().patch('/restaurants/1/reservations/5', json={"start_time":"2019-12-22 13:40:00",  "dinning_table_codes":["C001"]})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated'])
        self.assertTrue(data['total_reservations'])
        self.assertTrue(len(data['reservations']))

    def test_404_update_if_reservation_does_not_exist(self):
        res = self.client().patch('/restaurants/1/reservations/597', json={"start_time":"2019-12-22 12:40:00"})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_delete_reservation(self):
        res = self.client().delete('/restaurants/1/reservations/9')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['deleted'])
        self.assertTrue(data['total_reservations'])
        self.assertTrue(len(data['reservations']))

    def test_404_delete_if_reservation_does_not_exist(self):
        res = self.client().delete('/restaurants/1/reservations/400')
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
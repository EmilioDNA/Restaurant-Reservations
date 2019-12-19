import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import dateutil.parser
import babel
import datetime
import sys 

from models import setup_db, Restaurant, DinningTable, Reservation


RESTAURANTS_PER_PAGE = 10
DINNING_TABLES_PER_PAGE = 10
RESERVATIONS_PER_PAGE = 10


# Pagination method
def paginate_restaurants(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * RESTAURANTS_PER_PAGE
    end = start + RESTAURANTS_PER_PAGE

    restaurants = [restaurant.format() for restaurant in selection]
    current_restaurants = restaurants[start:end]
    return current_restaurants

    
def paginate_tables(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * DINNING_TABLES_PER_PAGE
    end = start + DINNING_TABLES_PER_PAGE

    dinning_tables = [table.format() for table in selection]
    current_dinning_tables = dinning_tables[start:end]
    return current_dinning_tables

def paginate_reservations(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * RESERVATIONS_PER_PAGE
    end = start + RESERVATIONS_PER_PAGE

    reservations = [reservation.display_dinning_tables for reservation in selection]
    current_reservations = reservations[start:end]
    return current_reservations


def convert_string_datetime(datetime_str):
    return datetime.datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

def convert_datetime_string(datetime):
    return datetime.strptime("%Y-%m-%d %H:%M:%S")

def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
        format="EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
        format="EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.route('/')
    def hello():
      return 'Hello'

    @app.route('/restaurants', methods=['GET'])
    def retrieve_restaurants():
      selection = Restaurant.query.order_by(Restaurant.id).all()
      current_restaurants = paginate_restaurants(request, selection)

      if len(current_restaurants) == 0:
        abort(404)

      return jsonify({
        'success': True,
        'restaurants': current_restaurants,
        'total_restaurants':  len(selection)
      })

    @app.route('/restaurants', methods=['POST'])
    def create_restaurant():
        body = request.get_json()

        new_title = body.get('title', None)
        new_city = body.get('city', None)
        new_state = body.get('state', None)
        new_address = body.get('address', None)
        new_phone = body.get('phone', None)
        new_image_link = body.get('image_link', None)

        try:

            restaurant = Restaurant(title=new_title,
                                    city=new_city,
                                    state=new_state,
                                    address=new_address,
                                    phone=new_phone,
                                    image_link=new_image_link)
            restaurant.insert()

            selection = Restaurant.query.order_by(Restaurant.id).all()
            current_restaurants = paginate_restaurants(request, selection)

            return jsonify({
                'success': True,
                'created': restaurant.id,
                'restaurants': current_restaurants,
                'total_restaurants': len(selection)
            })

        except: 
            abort(422)


    @app.route('/restaurants/<int:restaurant_id>', methods=['PATCH'])
    def update_restaurant(restaurant_id):
        restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()

        if restaurant is None:
            abort(404)

        body = request.get_json()
        title = body.get('title', None)
        city = body.get('city', None)
        state = body.get('state', None)
        address = body.get('address', None)
        phone = body.get('phone', None)
        image_link = body.get('image_link', None)

        try:
            if title is not None:
                restaurant.title = title
            if city is not None:
                restaurant.city = city
            if state is not None:
                restaurant.state = state
            if address is not None:
                restaurant.address = address
            if phone is not None:
                restaurant.phone = phone
            if image_link is not None:
                restaurant.image_link = image_link

            restaurant.update()
            selection = Restaurant.query.order_by(Restaurant.id).all()
            current_restaurants = paginate_restaurants(request, selection)

            return jsonify({
                'success': True,
                'updated': restaurant_id,
                'restaurants': current_restaurants,
                'total_restaurants': len(selection)
            })
        except:
            abort(422)
    
    @app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
    def delete_restaurant(restaurant_id):
        restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()
        if restaurant is None:
            abort(404)
        try:
            restaurant.delete()
            selection = Restaurant.query.order_by(Restaurant.id).all()
            current_restaurants = paginate_restaurants(request, selection)

            return ({
                'success': True,
                'deleted': restaurant_id,
                'restaurants': current_restaurants,
                'total_restaurants': len(selection)
            })

        except:
            abort(422)



    @app.route('/restaurants/<int:restaurant_id>/tables', methods=['GET'])
    def retrieve_dinning_tables(restaurant_id):
        restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()
        if restaurant is None:
            abort(404)

        selection = DinningTable.query.filter(DinningTable.restaurant_id == restaurant_id).all()
        current_dinning_tables = paginate_tables(request, selection)

        if len(current_dinning_tables) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'dinning_tables': current_dinning_tables,
            'total_dinning_tables':  len(selection)
        })

    @app.route('/restaurants/<int:restaurant_id>/tables', methods=['POST'])
    def create_dinning_table(restaurant_id):
        restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()
        if restaurant is None:
            abort(404)

        body = request.get_json()
        new_code = body.get('code', None)
        new_capacity = body.get('capacity', None)
        new_restaurant_id = restaurant_id

        try:
            dinning_table = DinningTable(code=new_code,
                                        capacity=new_capacity,
                                        restaurant_id=new_restaurant_id)
            dinning_table.insert()
            selection = DinningTable.query.order_by(DinningTable.id).all()
            current_dinning_tables = paginate_tables(request, selection)

            return jsonify({
                'success': 200,
                'created': dinning_table.id,
                'dinning_tables': current_dinning_tables,
                'total_dinning_tables': len(selection)
            })                                    
        except:
            abort(422)

    @app.route('/restaurants/<int:restaurant_id>/tables/<int:table_id>', methods=['PATCH'])
    def update_dinning_table(restaurant_id, table_id):
        restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()
        dinning_table = DinningTable.query.filter(DinningTable.id == table_id).one_or_none()
        
        if restaurant is None or dinning_table is None:
            abort(404)
        
        body = request.get_json()
        code = body.get('code', None)
        capacity = body.get('capacity', None)

        try:
            if code is not None:
                dinning_table.code = code
            if capacity is not None:
                dinning_table.capacity = capacity

            dinning_table.update()
            selection = DinningTable.query.order_by(DinningTable.id).all()
            current_dinning_tables = paginate_tables(request, selection)

            return jsonify({
                'success': 200,
                'updated': dinning_table.id,
                'dinning_tables': current_dinning_tables,
                'total_dinning_tables': len(selection)
            })
        except:
            abort(422)

    
    @app.route('/restaurants/<int:restaurant_id>/tables/<int:table_id>', methods=['DELETE'])
    def delete_dinning_table(restaurant_id, table_id):
        restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()
        dinning_table = DinningTable.query.filter(DinningTable.id == table_id).one_or_none()
        
        if restaurant is None or dinning_table is None:
            abort(404)
        
        try:
            dinning_table.delete()
            selection = DinningTable.query.order_by(DinningTable.id).all()
            current_dinning_tables = paginate_tables(request, selection)

            return jsonify({
                'success': 200,
                'deleted': table_id,
                'dinning_tables': current_dinning_tables,
                'total_dinning_tables': len(selection)
            })

        except:
            abort(422)

    @app.route('/restaurants/<int:restaurant_id>/reservations', methods=['GET'])
    def retrieve_reservations(restaurant_id):
        restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()
        if restaurant is None:
            abort(404)

        selection = Reservation.query.join(DinningTable, Reservation.dinning_tables) \
                                        .filter(DinningTable.restaurant_id == restaurant_id) \
                                        .order_by(Reservation.id).all()

        current_reservations = paginate_reservations(request, selection)

        if len(current_reservations) == 0:
            abort(404)

        return {
            'success': 200,
            'reservations': current_reservations,
            'total_reservations': len(selection)
        }

        

    @app.route('/restaurants/<int:restaurant_id>/reservations', methods=['POST'])
    def create_reservation(restaurant_id):
        restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()
        if restaurant is None:
            abort(404)

        body = request.get_json()
        new_start_time = body.get('start_time', None)
        new_end_time = body.get('end_time', None)
        new_dinning_table_codes = body.get('dinning_table_codes', None)

        new_dinning_tables = DinningTable.query.filter(DinningTable.code.in_(new_dinning_table_codes)).all()

        if len(new_dinning_tables) == 0:
            abort(404)

        try:
            reservation = Reservation(start_time=new_start_time,
                                    end_time=new_end_time)

            for dinning_table in new_dinning_tables:
                reservation.dinning_tables.append(dinning_table)
            reservation.insert()

            selection = Reservation.query.join(DinningTable, Reservation.dinning_tables) \
                                        .filter(DinningTable.restaurant_id == restaurant_id) \
                                        .order_by(Reservation.id).all()

            current_reservations = paginate_reservations(request, selection)

            return jsonify({
                'success': 200,
                'created': reservation.id,
                'reservations': current_reservations,
                'total_reservations': len(selection)
            })                                    
        except:
            abort(422)
        

    @app.route('/restaurants/<int:restaurant_id>/reservations/<int:reservation_id>', methods=['PATCH'])
    def update_reservation(restaurant_id, reservation_id):
        restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()
        reservation = Reservation.query.filter(Reservation.id == reservation_id).one_or_none()
        if restaurant is None or reservation is None:
            abort(404)

        body = request.get_json()
        start_time = body.get('start_time', None)
        end_time = body.get('end_time', None)
        dinning_table_codes = body.get('dinning_table_codes', None)

        dinning_tables = DinningTable.query.filter(DinningTable.code.in_(dinning_table_codes)).all()
        print(dinning_tables)

        if len(dinning_tables) == 0:
            abort(404)
       
        try:
            if start_time is not None:
                reservation.start_time = start_time
            if end_time is not None:
                reservation.end_time = end_time
            if len(dinning_tables) != 0:
                reservation.dinning_tables.clear()
                for dinning_table in dinning_tables:
                    reservation.dinning_tables.append(dinning_table)

            reservation.update()

            selection = Reservation.query.join(DinningTable, Reservation.dinning_tables) \
                                        .filter(DinningTable.restaurant_id == restaurant_id) \
                                        .order_by(Reservation.id).all()

            current_reservations = paginate_reservations(request, selection)

            return jsonify({
                'success': 200,
                'updated': reservation.id,
                'reservations': current_reservations,
                'total_reservations': len(selection)
            })                                    
        except:
            abort(422)


    @app.route('/restaurants/<int:restaurant_id>/reservations/<int:reservation_id>', methods=['DELETE'])
    def delete_reservation(restaurant_id, reservation_id):
        restaurant = Restaurant.query.filter(Restaurant.id == restaurant_id).one_or_none()
        reservation = Reservation.query.filter(Reservation.id == reservation_id).one_or_none()
        if restaurant is None or reservation is None:
            abort(404)
       
        try:
            reservation.delete()

            selection = Reservation.query.join(DinningTable, Reservation.dinning_tables) \
                                        .filter(DinningTable.restaurant_id == restaurant_id) \
                                        .order_by(Reservation.id).all()

            current_reservations = paginate_reservations(request, selection)

            return jsonify({
                'success': 200,
                'deleted': reservation_id,
                'reservations': current_reservations,
                'total_reservations': len(selection)
            })                                    
        except:
            abort(422)

    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(422)
    def unproccesable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    @app.errorhandler(400)
    def bas_request(error):
        return jsonify({
            'success': False,
            'error': 400,
            'message': 'bad request'
        }), 400

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            'success': False,
            'error': 405,
            'message': 'method not allowed'
        }), 405


    return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000, debug=True)
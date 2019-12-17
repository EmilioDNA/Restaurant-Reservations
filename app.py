import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Restaurant, DinningTable, Reservation


RESTAURANTS_PER_PAGE = 10
DINNING_TABLES_PER_PAGE = 10
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
        

    return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000, debug=True)
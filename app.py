import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import setup_db, Restaurant, DinningTable, Reservation


RESTAURANTS_PER_PAGE = 10
# Pagination method
def paginate_restaurants(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * RESTAURANTS_PER_PAGE
    end = start + RESTAURANTS_PER_PAGE

    restaurants = [restaurant.format() for restaurant in selection]
    current_restaurants = restaurants[start:end]
    return current_restaurants



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




    return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='127.0.0.1', port=5000, debug=True)
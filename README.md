# Restaurant Reservations API Backend

## Description

This is a basic API that allows clients, restaurant managers, and admins to consult the availability of restaurants in specific places and to set reservations.

For this project, I only cover the functionality of one city. However, this project is intended to provide more capabilities in order to provide a better user experience.

## Getting Started

### Installing Dependencies

#### Python 3.7 

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### Pip Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/Restaurant-Reservations-API` directory and running:

```bash
pip install -r requirements.txt
```
I included all the needed dependencies for this project in the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM I'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from any frontend server. 

## Database Setup
In order to be able to test the app, is needed to insert data in the following order:
1.- Create Restaurants  (at least 2 elements)
2.- Create Dinning tables (at least 3 elements)
3.- Create Reservations (at least 2 elements)

Take into account that in order to be able to create a Reservation successfully,
the dinning table codes entered should exist (please refer to the API examples).

## Running the server

From withing the `Restaurant-Reservation-API` directory frist
ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to run the application.


## Testing
To run the tests, run
```
python test_app.py
```
Take into account that all the routes require authentication, so, You'll have to comment in the `@requires_auth` decorator to run the functional tests.

Consider that in order to test the application, Restaurant, Dinning table, and Reservation data must be created in a table called `reservation_tests`, the Ids from these elements must match with the tested endpoints. 

Additionally, you can test the authentication with Postman, by using the `Restaurant-Reservations-API-tests.postman_collection.json`, and run it within Postman.

## API Reference

## Getting started

# pending until launching
```
Base URL: At the moment, this app runs only locally and is not hosted as a base URL. The backend is hosted at the default, http://127.0.0.1:500/ , which is set as a proxy in the fronted configuration.

Authentication: This version of the application does not require authentication or API keys to work
```

## Error Handling
```
Errors are returned as JSON objects in the following format:
{
    "success": False,
    "error": 400,
    "message": "bad request"
}

The API will return four error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 405: Method Not Allowed
- 422: Not Processable
- 402: Not authorized

```

GET /restaurants

- General:
    Returns a list of restaurant objects, success value and  the total number of restaurants.
    Results are paginated in groups of 10, Include a request argument to choose page number, starting from 1.
- Sample: curl http://127.0.0.1:5000/restaurants

```
{
    "restaurants": [
        {
            "address": "2ra. Ote. #3545",
            "city": "Comitan",
            "id": 1,
            "image_link": "https://barriocentral.com",
            "phone": "1024564",
            "state": "Chiapas",
            "title": "Barrio Central"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 2,
            "image_link": "https://laesquina.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "La esquina de Tio Beli"
        },
,        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 3,
            "image_link": "https://italiancoffee.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "The Italian Coffee"
        }
        {
            "address": "2ra. Ote. #3545",
            "city": "Comitan",
            "id": 4,
            "image_link": "https://cafedavid.com",
            "phone": "1234567",
            "state": "Chiapas",
            "title": "Café David"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 5,
            "image_link": "https://nevarez.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Nevarez"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 7,
            "image_link": "https://starbucks.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Starbucks"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 8,
            "image_link": "https://sanseurban.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Sanse Urban"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 9,
            "image_link": "https://500noches.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "500 Noches"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 10,
            "image_link": "https://sanfers",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Sanfer's Coffee"
        },
        {
            "address": "2ra. Nte. #3545",
            "city": "Comitan",
            "id": 13,
            "image_link": "https://cielitoquerido.com",
            "phone": "3343923",
            "state": "Chiapas",
            "title": "Cielito Querido"
        },
        {
            "address": "2ra. Nte. #3545",
            "city": "Comitan",
            "id": 13,
            "image_link": "https://laselva.com",
            "phone": "3343923",
            "state": "Chiapas",
            "title": "La selva"
        }
    ],
    "success": true,
    "total_restaurants": 13
}
```


POST /restaurants

- General:
    Creates a specific restaurant by providing the title, city,
    state, address, phone, and image_link.
    Returns a list of restaurant objects that include the newly created restaurant, success value, the id of the created restaurant, and the total number of restaurants after creating.

- Sample: curl -d '{{"title":"La Selva", "city":"Comitan", "state":"Chiapas", "address": "2ra. Nte. #3545", "phone":"3343923", "image_link":"https://laselva.com"}}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/restaurants

```
{
    "restaurants": [
        {
            "address": "2ra. Ote. #3545",
            "city": "Comitan",
            "id": 1,
            "image_link": "https://barriocentral.com",
            "phone": "1024564",
            "state": "Chiapas",
            "title": "Barrio Central"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 2,
            "image_link": "https://laesquina.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "La esquina de Tio Beli"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 3,
            "image_link": "https://italiancoffee.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "The Italian Coffee"
        },
        {
            "address": "2ra. Ote. #3545",
            "city": "Comitan",
            "id": 4,
            "image_link": "https://cafedavid.com",
            "phone": "1234567",
            "state": "Chiapas",
            "title": "Café David"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 5,
            "image_link": "https://nevarez.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Nevarez"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 7,
            "image_link": "https://starbucks.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Starbucks"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 8,
            "image_link": "https://sanseurban.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Sanse Urban"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 9,
            "image_link": "https://500noches.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "500 Noches"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 10,
            "image_link": "https://sanfers",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Sanfer's Coffee"
        },
        {
            "address": "2ra. Nte. #3545",
            "city": "Comitan",
            "id": 13,
            "image_link": "https://cielitoquerido.com",
            "phone": "3343923",
            "state": "Chiapas",
            "title": "Cielito Querido"
        },
        {
            "address": "2ra. Nte. #3545",
            "city": "Comitan",
            "id": 13,
            "image_link": "https://laselva.com",
            "phone": "3343923",
            "state": "Chiapas",
            "title": "La selva"
        }
    ],
    "success": true,
    "total_restaurants": 14,
    "created": 13
}
```


PATCH /restaurants/{restaurant_id}

- General:
    Updates a specific restaurant by providing the id.
    You may update all the fields or just one, depending on your needs.
    Returns a list of restaurant objects that include the updated restaurant, success value, the id of the updated restaurant, and the total number of restaurants after updating.

- Sample: curl -d '{{ "phone":"1234567867"}}' -H "Content-Type: application/json" -X PATCH http://127.0.0.1:5000/restaurants/13

```
{
    "restaurants": [
        {
            "address": "2ra. Ote. #3545",
            "city": "Comitan",
            "id": 1,
            "image_link": "https://barriocentral.com",
            "phone": "1024564",
            "state": "Chiapas",
            "title": "Barrio Central"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 2,
            "image_link": "https://laesquina.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "La esquina de Tio Beli"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 3,
            "image_link": "https://italiancoffee.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "The Italian Coffee"
        },
        {
            "address": "2ra. Ote. #3545",
            "city": "Comitan",
            "id": 4,
            "image_link": "https://cafedavid.com",
            "phone": "1234567",
            "state": "Chiapas",
            "title": "Café David"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 5,
            "image_link": "https://nevarez.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Nevarez"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 7,
            "image_link": "https://starbucks.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Starbucks"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 8,
            "image_link": "https://sanseurban.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Sanse Urban"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 9,
            "image_link": "https://500noches.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "500 Noches"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 10,
            "image_link": "https://sanfers",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Sanfer's Coffee"
        },
        {
            "address": "2ra. Nte. #3545",
            "city": "Comitan",
            "id": 13,
            "image_link": "https://cielitoquerido.com",
            "phone": "3343923",
            "state": "Chiapas",
            "title": "Cielito Querido"
        },
        {
            "address": "2ra. Nte. #3545",
            "city": "Comitan",
            "id": 13,
            "image_link": "https://laselva.com",
            "phone": "1234567867",
            "state": "Chiapas",
            "title": "La selva"
        }
    ],
    "success": true,
    "total_restaurants": 14,
    "updated": 13
}
```


DELETE /restaurants/{restaurant_id}

- General:
    Deletes a specific restaurant by providing the id.
    Returns a list of restaurant objects that include the deleted restaurant's id, success value, and the total number of restaurants after deleting.

- Sample: curl  -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/restaurants/13

```
{
    "restaurants": [
        {
            "address": "2ra. Ote. #3545",
            "city": "Comitan",
            "id": 1,
            "image_link": "https://barriocentral.com",
            "phone": "1024564",
            "state": "Chiapas",
            "title": "Barrio Central"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 2,
            "image_link": "https://laesquina.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "La esquina de Tio Beli"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 3,
            "image_link": "https://italiancoffee.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "The Italian Coffee"
        },
        {
            "address": "2ra. Ote. #3545",
            "city": "Comitan",
            "id": 4,
            "image_link": "https://cafedavid.com",
            "phone": "1234567",
            "state": "Chiapas",
            "title": "Café David"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 5,
            "image_link": "https://nevarez.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Nevarez"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 7,
            "image_link": "https://starbucks.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Starbucks"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 8,
            "image_link": "https://sanseurban.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Sanse Urban"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 9,
            "image_link": "https://500noches.com",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "500 Noches"
        },
        {
            "address": "1ra. Av. Ote. Nte. #45",
            "city": "Comitan",
            "id": 10,
            "image_link": "https://sanfers",
            "phone": "10245649",
            "state": "Chiapas",
            "title": "Sanfer's Coffee"
        },
        {
            "address": "2ra. Nte. #3545",
            "city": "Comitan",
            "id": 13,
            "image_link": "https://cielitoquerido.com",
            "phone": "3343923",
            "state": "Chiapas",
            "title": "Cielito Querido"
        }
    ],
    "success": true,
    "total_restaurants": 13,
    "deleted": 13
}
```

GET /restaurants/{restaurant_id}/tables

- General:
    Returns a list of dinning table objects, success value and  the total number of dinning tables.
    Results are paginated in groups of 10, Include a request argument to choose page number, starting from 1.
- Sample: curl http://127.0.0.1:5000/restaurants/1/tables

```
{
    "dinning_tables": [
        {
            "id": 1,
            "code": "A001",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 2,
            "code": "A002",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 3,
            "code": "A003",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 4,
            "code": "B001",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 5,
            "code": "B002",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 6,
            "code": "B003",
            "capacity": 4,
            "restaurant_id": 1
        },
    ],
    "success": true,
    "total_dinning_tables": 6
}
```


POST /restaurants/{restaurant_id}/tables

- General:
    Creates a specific dinning table by providing the code and the capacity.
    Returns a list of dinning table objects that include the newly created dinning table, success value, the id of the created dinning table, and the total number of dinning tables after creating.

- Sample: curl -d '{{"code":"C001", "capacity":8}}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/restaurants/1/tables

```
{
    "dinning_tables": [
        {
            "id": 1,
            "code": "A001",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 2,
            "code": "A002",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 3,
            "code": "A003",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 4,
            "code": "B001",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 5,
            "code": "B002",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 6,
            "code": "B003",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 7,
            "code": "C001",
            "capacity": 8,
            "restaurant_id": 1
        },
        
    ],
    "success": true,
    "total_dinning_tables": 7,
    "created": 7
}
```


PATCH /restaurants/{restaurant_id}/tables/{table_id}

- General:
    Updates a specific dinning table by providing the id.
    You may update all the fields or just one, depending on your needs.
    Returns a list of dinning table objects that include the updated dinning table, success value, the id of the updated dinning table, and the total number of dinning tables after updating.

- Sample: curl -d '{{ "capacity":12}}' -H "Content-Type: application/json" -X PATCH http://127.0.0.1:5000/restaurants/1/tables/7

```
{
    "dinning_tables": [
        {
            "id": 1,
            "code": "A001",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 2,
            "code": "A002",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 3,
            "code": "A003",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 4,
            "code": "B001",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 5,
            "code": "B002",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 6,
            "code": "B003",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 7,
            "code": "C001",
            "capacity": 12,
            "restaurant_id": 1
        },
        
    ],
    "success": true,
    "total_dinning_tables": 7,
    "updated": 7
}
```


DELETE /restaurants/{restaurant_id}/tables/{table_id}

- General:
    Deletes a specific dinning table by providing the id.
    Returns a list of dinning table objects that include the deleted dinning table's id, success value, and the total number of dinning tables after deleting.

- Sample: curl  -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/restaurants/1/tables/7

```
{
    "dinning_tables": [
        {
            "id": 1,
            "code": "A001",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 2,
            "code": "A002",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 3,
            "code": "A003",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 4,
            "code": "B001",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 5,
            "code": "B002",
            "capacity": 4,
            "restaurant_id": 1
        },
        {
            "id": 6,
            "code": "B003",
            "capacity": 4,
            "restaurant_id": 1
        }
    ],
    "success": true,
    "total_dinning_tables": 6,
    "deleted": 7
}
```

GET /restaurants/{restaurant_id}/reservations

- General:
    Returns a list of reservation objects, success value and  the total number of reservations.
    Results are paginated in groups of 10, Include a request argument to choose page number, starting from 1.
- Sample: curl http://127.0.0.1:5000/restaurants/1/reservations

```
{   "reservations": [
        {

            "id":1
            "start_time": "2019-12-22 12:40:00",
            "end_time": "2019-12-22 15:40:00",
            "dinning_tables": [
                {
                    "id": 1,
                    "code": "A001",
                    "capacity": 4,
                    "restaurant_id": 1
                },
                {
                    "id": 2,
                    "code": "A002",
                    "capacity": 4,
                    "restaurant_id": 1
                },
                {
                    "id": 3,
                    "code": "A003",
                    "capacity": 4,
                    "restaurant_id": 1
                }
            ]
        }
    ],

    "success": true,
    "total_reservations": 1
}
```


POST /restaurants/{restaurant_id}/reservations

- General:
    Creates a specific reservation by providing the start time, the end time and the list of tables to reserve. If the dinning tables don't belong to the requested restaurant, the reservation won't be possible. 
    Returns a list of reservation objects that include the newly created reservation, success value, the id of the created reservation, and the total number of reservations after creating.

- Sample: curl -d '{{"start_time":"2019-12-22 12:50:00", "end_time":"2019-12-22 13:40:00", "dinning_table_codes":["B001", "B002"]}}' -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/restaurants/1/reservations

```
{   
    "reservations": [
        {   
            "id": 1,
            "start_time": "2019-12-22 12:40:00",
            "end_time": "2019-12-22 15:40:00",
            "dinning_tables": [
                {
                    "id": 1,
                    "code": "A001",
                    "capacity": 4,
                    "restaurant_id": 1
                },
                {
                    "id": 2,
                    "code": "A002",
                    "capacity": 4,
                    "restaurant_id": 1
                },
                {
                    "id": 3,
                    "code": "A003",
                    "capacity": 4,
                    "restaurant_id": 1
                }
            ]
        },
        {
            "id":2, 
            "start_time": "2019-12-22 12:50:00",
            "end_time": "2019-12-22 13:40:00",
            "dinning_tables": [
                {
                    "id": 4,
                    "code": "B001",
                    "capacity": 4,
                    "restaurant_id": 1
                },
                {
                    "id": 5,
                    "code": "B002",
                    "capacity": 4,
                    "restaurant_id": 1
                }
            ]
        }
    ],
    "success": true,
    "total_reservations": 2,
    "created": 2
}
```


PATCH /restaurants/{restaurant_id}/reservations/{reservation_id}

- General:
    Updates a specific reservation by providing the id.
    You may update all the fields or just one, depending on your needs.
    Returns a list of reservation objects that include the updated reservation, success value, the id of the updated reservation, and the total number of reservations after updating.

- Sample: curl -d '{{ "end_time":2019-12-22 16:00:00}}' -H "Content-Type: application/json" -X PATCH http://127.0.0.1:5000/restaurants/1/reservations/2

```
{   
    "reservations": [
        {   
            "id": 1,
            "start_time": "2019-12-22 12:40:00",
            "end_time": "2019-12-22 15:40:00",
            "dinning_tables": [
                {
                    "id": 1,
                    "code": "A001",
                    "capacity": 4,
                    "restaurant_id": 1
                },
                {
                    "id": 2,
                    "code": "A002",
                    "capacity": 4,
                    "restaurant_id": 1
                },
                {
                    "id": 3,
                    "code": "A003",
                    "capacity": 4,
                    "restaurant_id": 1
                }
            ]
        },
        {
            "id":2, 
            "start_time": "2019-12-22 12:50:00",
            "end_time": "2019-12-22 16:00:00",
            "dinning_tables": [
                {
                    "id": 4,
                    "code": "B001",
                    "capacity": 4,
                    "restaurant_id": 1
                },
                {
                    "id": 5,
                    "code": "B002",
                    "capacity": 4,
                    "restaurant_id": 1
                }
            ]
        }
    ],
    "success": true,
    "total_reservations": 2,
    "updated": 2
}
```


DELETE /restaurants/{restaurant_id}/reservations/{reservation_id}

- General:
    Deletes a specific reservation by providing the id.
    Returns a list of reservation objects that include the deleted reservation's id, success value, and the total number of reservations after deleting.

- Sample: curl  -H "Content-Type: application/json" -X DELETE http://127.0.0.1:5000/restaurants/1/reservations/2

```
{   
    "reservations": [
        {   
            "id": 1,
            "start_time": "2019-12-22 12:40:00",
            "end_time": "2019-12-22 15:40:00",
            "dinning_tables": [
                {
                    "id": 1,
                    "code": "A001",
                    "capacity": 4,
                    "restaurant_id": 1
                },
                {
                    "id": 2,
                    "code": "A002",
                    "capacity": 4,
                    "restaurant_id": 1
                },
                {
                    "id": 3,
                    "code": "A003",
                    "capacity": 4,
                    "restaurant_id": 1
                }
            ]
        }
    ],
    "success": true,
    "total_reservations": 1,
    "deleted": 2
}
```
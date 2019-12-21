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
# Pending until implementation

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
dropdb reservation_tests
createdb reservation_test
psql reservation_test < reservations.psql
python test_app.py
```
Take into account that all the routes require authentication, so, You'll have to comment in the `@requires_auth` decorator to run the functional tests.

Additionally, you can test the authentication with Postman, by using the `restaurants-reservation-posman-test-collection.file`, and run it within Postman.

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
    "total_restaurants": 13
}
```


POST /restaurant

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
    Returns a list of restaurant objects that include the updated restaurant, success value, the id of the updated restaurant, and the total number of restaurants after creating.

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
    Returns a list of restaurant objects that include the deleted restaurant's id, success value, and the total number of restaurants after creating.

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
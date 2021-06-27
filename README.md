# pymongo-restapi-poc
REST API using Flask and PyMongo.

## API Calls

---
POST
http://127.0.0.1:5000/users

Headers:
Content-Type > application/json

Body:

{
    "username": "beto",
    "password": "hello12345",
    "email": "beto@mail.com"
}

---
GET
http://127.0.0.1:5000/users

---
GET
http://127.0.0.1:5000/users/60d2bcd8135558e8a574c4d3

---
DELETE
http://127.0.0.1:5000/users/60d2bcd8135558e8a574c4d3

---
PUT
http://127.0.0.1:5000/users/60d2bfa70d0395b77936b740

Headers:
Content-Type > application/json

Body:

{
    "username": "petar",
    "email": "petar@mail.com",
    "password": "hi12345"
}

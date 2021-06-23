import logging
from flask import Flask, request, Response, jsonify
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/pythonmongodb'
mongo = PyMongo(app)


@app.route('/users', methods=['POST'])
def create_user():
    print(request.json)

    if 'username' in request.json and 'email' in request.json and 'password' in request.json:
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert_one(
            {'username': username, 'email': email, 'password': hashed_password}
        )
        logging.debug(id)
        response = {
            'id': str(id),
            'username': username,
            'email': email,
            'password': hashed_password
        }
        return response
    else:
        return not_found()

    return {'message': 'received'}


@app.route('/users', methods=['GET'])
def get_users():
    logging.debug(request.json)
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype='application/json')


@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    print(id)
    user = mongo.db.users.find_one({'_id': ObjectId(id)})
    response = json_util.dumps(user)
    return Response(response, mimetype='application/json')


@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    print(id)
    if 'username' in request.json and 'email' in request.json and 'password' in request.json:
        username = request.json['username']
        email = request.json['email']
        password = request.json['password']
        hashed_password = generate_password_hash(password)

        mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': {
            'username': username,
            'email': email,
            'password': hashed_password
        }})

    response = jsonify({
        'message': 'User ' + id + ' was updated successfully'
    })
    return response


@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    print(id)
    user = mongo.db.users.delete_one({'_id': ObjectId(id)})
    response = jsonify({
        'message': 'User ' + id + ' was deleted successfully'
    })
    return response


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource not found: ' + request.url,
        'status': 404
    })
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True)

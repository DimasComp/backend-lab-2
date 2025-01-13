from flask import Blueprint, jsonify, request
from server.db import users
import uuid

user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'])
def get_users():
    return jsonify(users.values())

@user.route('/user/<id>', methods=['GET'])
def get_user(id):
    if id not in users:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users[id])

@user.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    id = uuid.uuid4().hex
    users[id] = {'id': id, 'name': data['name']}
    return jsonify(users[id]), 201

@user.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    if id not in users:
        return jsonify({'error': 'User not found'}), 404
    user = users[id]
    del users[id]
    return jsonify(user), 200

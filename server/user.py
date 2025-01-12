from flask import Blueprint, jsonify, request
from server.db import users

user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

@user.route('/user/<id>', methods=['GET'])
def get_user(uid):
    if uid not in users:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(users.get(uid))

@user.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    if data['id'] in users:
        return jsonify({'error': 'User already exists'}), 400
    uid = uuid.uuid4().hex
    users[uid] = {'name': data['name'], 'id': uid}
    return jsonify(users[uid]), 201

@user.route('/user/<id>', methods=['DELETE'])
def delete_user(uid):
    if uid not in users:
        return jsonify({'error': 'User not found'}), 404
    user = users[uid]
    del users[uid]
    return jsonify(user), 200

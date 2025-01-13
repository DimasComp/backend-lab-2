from flask import Blueprint, jsonify, request
from server.models.user import UserModel
from server.schemas.user import user_schema, users_schema
from server.globals import db

user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'])
def get_users():
    users = UserModel.query.all()
    return jsonify(user_schema.dump(users))

@user.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = UserModel.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user_schema.dump(user))

@user.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_user = UserModel(name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user)), 201

@user.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = UserModel.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify(user_schema.dump(user)), 200

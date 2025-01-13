from flask import Blueprint, jsonify, request
from server.models.user import UserModel
from server.models.wallet import WalletModel
from server.schemas.user import user_schema, users_schema
from server.globals import db
import uuid

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
    wallet_id = uuid.uuid4().hex
    new_wallet = WalletModel(id=wallet_id)
    db.session.add(new_wallet)
    new_user = UserModel(name=data['name'], wallet_id=wallet_id)
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

@user.route('/user/<id>/add_money', methods=['POST'])
def add_money(id):
    data = request.get_json()
    if 'amount' not in data:
        return jsonify({'error': 'Field amount is missing'}), 400
    user = UserModel.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    user.add_money_to_wallet(data['amount'])
    return jsonify(user_schema.dump(user)), 200

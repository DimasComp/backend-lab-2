from flask import Blueprint, jsonify, request
from server.models.user import UserModel
from server.models.wallet import WalletModel
from server.schemas.user import user_schema, users_schema
from server.globals import db, jwt
import uuid
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import jwt_required, create_access_token

user = Blueprint('user', __name__)

@jwt_required()
@user.route('/users', methods=['GET'])
def get_users():
    users = UserModel.query.all()
    print(users)
    return jsonify(users_schema.dump(users))

@jwt_required()
@user.route('/user/<id>', methods=['GET'])
def get_user(id):
    user = UserModel.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user_schema.dump(user))


@user.route('/user', methods=['POST'])
def register():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    wallet_id = uuid.uuid4().hex
    new_wallet = WalletModel(id=wallet_id)
    db.session.add(new_wallet)
    pass_hash = pbkdf2_sha256.hash(data['password'])
    new_user = UserModel(name=data['name'], wallet_id=wallet_id, password=pass_hash)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(user_schema.dump(new_user)), 201


@user.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if 'name' not in data or 'password' not in data:
        return jsonify({'error': 'Missing name or password'}), 400
    user = UserModel.query.filter_by(name=data['name']).first()
    if not user:
        return jsonify({'error': 'User not found'}), 404
    if not pbkdf2_sha256.verify(data['password'], user.password):
        return jsonify({'error': 'Invalid password'}), 400
    return jsonify({'token': create_access_token(identity=user.id)}), 200


@jwt_required()
@user.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = UserModel.query.get(id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    wallet_id = user.wallet_id
    wallet = WalletModel.query.get(wallet_id)
    if wallet:
        db.session.delete(wallet)

    db.session.delete(user)
    db.session.commit()
    return jsonify(user_schema.dump(user)), 200


@jwt_required()
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

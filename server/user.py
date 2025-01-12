from flask import Blueprint, jsonify, request

user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'])
def get_users():
    return jsonify({'users': 'get_users'})


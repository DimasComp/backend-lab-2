from flask import Blueprint, jsonify, request
from server.db import categories

category = Blueprint('category', __name__)

@category.route('/category', methods=['GET'])
def get_category():
    data = request.get_json()
    if 'id' not in data:
        return jsonify({'error': 'Missing id'}), 400
    if data['id'] not in categories:
        return jsonify({'error': 'Category not found'}), 404
    return jsonify(categories.get(data['id']))

@category.route('/category', methods=['POST'])
def add_category():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Missing name'}), 400
    if data['id'] in categories:
        return jsonify({'error': 'Category already exists'}), 400
    cid = uuid.uuid4().hex
    categories[cid] = {'name': data['name'], 'id': cid}
    return jsonify(categories[cid]), 201

@category.route('/category', methods=['DELETE'])
def delete_category():
    data = request.get_json()
    if 'id' not in data:
        return jsonify({'error': 'Missing id'}), 400
    if data['id'] not in categories:
        return jsonify({'error': 'Category not found'}), 404
    category = categories.get(data['id'])
    del categories[data['id']]
    return jsonify(category), 200
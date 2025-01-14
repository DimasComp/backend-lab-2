from flask import Blueprint, jsonify, request
from server.globals import db
from server.models.category import CategoryModel
from server.schemas.category import category_schema

category = Blueprint('category', __name__)


@jwt_required()
@category.route('/category', methods=['GET'])
def get_category():
    data = request.get_json()
    if 'id' not in data:
        return jsonify({'error': 'Missing id'}), 400
    category = CategoryModel.query.get(data['id'])
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    return jsonify(category.to_dict())


@jwt_required()
@category.route('/category', methods=['POST'])
def add_category():
    data = request.get_json()
    errors = category_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_category = CategoryModel(name=data['name'])
    db.session.add(new_category)
    db.session.commit()
    return jsonify(new_category.to_dict()), 201


@jwt_required()
@category.route('/category', methods=['DELETE'])
def delete_category():
    data = request.get_json()
    if 'id' not in data:
        return jsonify({'error': 'Missing id'}), 400
    category = CategoryModel.query.get(data['id'])
    if not category:
        return jsonify({'error': 'Category not found'}), 404
    db.session.delete(category)
    db.session.commit()
    return jsonify(category.to_dict()), 200
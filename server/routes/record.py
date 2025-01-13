from flask import Blueprint, jsonify, request
from main import db
from server.models.record import RecordModel
from server.schemas.record import record_schema, records_schema

record = Blueprint('record', __name__)


@record.route('/record/<id>', methods=['GET'])
def get_record(id):
    record = RecordModel.query.get(id)
    if not record:
        return jsonify({'error': 'Record not found'}), 404
    return jsonify(record_schema.dump(record))


@record.route('/record', methods=['POST'])
def add_record():
    data = request.get_json()
    errors = record_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    new_record = RecordModel(
        user_id=data['user_id'],
        category_id=data['category_id'],
        amount=data['amount']
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify(record_schema.dump(new_record)), 201


@record.route('/record/<id>', methods=['DELETE'])
def delete_record(id):
    record = RecordModel.query.get(id)
    if not record:
        return jsonify({'error': 'Record not found'}), 404
    db.session.delete(record)
    db.session.commit()
    return jsonify(record_schema.dump(record)), 200


@record.route('/record', methods=['GET'])
def get_filtered_records():
    data = request.get_json()
    query = RecordModel.query
    if 'user_id' in data:
        query = query.filter_by(user_id=data['user_id'])
    if 'category_id' in data:
        query = query.filter_by(category_id=data['category_id'])
    filtered_records = query.all()
    return jsonify(records_schema.dump(filtered_records))

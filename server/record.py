from flask import Blueprint, jsonify, request
from server.db import records
import pytz
import uuid
from datetime import datetime

record = Blueprint('record', __name__)
zone = pytz.timezone('Etc/GMT+2')


@record.route('/record/<id>', methods=['GET'])
def get_record(rid):
    if rid not in records:
        return jsonify({'error': 'Record not found'}), 404
    return jsonify(records[rid])


@record.route('/record', methods=['POST'])
def add_record():
    data = request.get_json()
    if any(k not in data for k in ['user_id', 'category_id', 'amount']):
        return jsonify({'error': 'Missing name, cid or amount'}), 400
    rid = uuid.uuid4().hex
    records[rid] = {'user_id': data['user_id'], 'category_id': data['category_id'], 'amount': data['amount'],
                    'id': rid, 'date': datetime.now(pytz.utc).strftime('%d-%m-%Y %H:%M:%S')}
    return jsonify(records[rid]), 201

@record.route('/record/<id>', methods=['DELETE'])
def delete_record(rid):
    if rid not in records:
        return jsonify({'error': 'Record not found'}), 404
    record = records[rid]
    del records[rid]
    return jsonify(record), 200

@record.route('/record', methods=['GET'])
def get_filtered_records():
    data = request.get_json()
    if 'user_id' not in data and 'category_id' not in data:
        return jsonify({'error': 'Missing user_id or category_id'}), 400
    filtered_records = []

    for record in records.values():
        if 'user_id' in data and record['user_id'] != data['user_id']:
            continue
        if 'category_id' in data and record['category_id'] != data['category_id']:
            continue
        filtered_records.append(record)
    return jsonify(filtered_records)

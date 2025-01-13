from marshmallow import Schema, fields, validate

class RecordSchema(Schema):
    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=True)
    category_id = fields.Str(required=True)
    amount = fields.Float(required=True, validate=validate.Range(min=0))
    date = fields.DateTime(dump_only=True)

record_schema = RecordSchema()
records_schema = RecordSchema(many=True)
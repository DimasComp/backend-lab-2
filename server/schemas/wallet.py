from marshmallow import Schema, fields, validate

class WalletSchema(Schema):
    id = fields.Str(dump_only=True)
    balance = fields.Float(dump_only=True)

wallet_schema = WalletSchema()
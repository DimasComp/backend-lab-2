from marshmallow import Schema, fields, validate
from server.schemas.wallet import WalletSchema

class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    password = fields.Str(required=True, validate=validate.Length(min=1))
    wallet = fields.Nested(WalletSchema, dump_only=True)


user_schema = UserSchema()
users_schema = UserSchema(many=True)

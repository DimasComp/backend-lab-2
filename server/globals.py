from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_jwt_extended import JWTManager

os.environ.setdefault('POSTGRES_USER', 'mock_user')
os.environ.setdefault('POSTGRES_PASSWORD', 'mock_password')
os.environ.setdefault('POSTGRES_HOST', 'localhost')
os.environ.setdefault('POSTGRES_DB', 'mock_db')

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_Key', 'mock_secret_key')

db = SQLAlchemy(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
   return (
       jsonify({"message": "The token has expired.", "error": "token_expired"}),
       401,
   )


@jwt.invalid_token_loader
def invalid_token_callback(error):
   return (
       jsonify(
           {"message": "Signature verification failed.", "error": "invalid_token"}
       ),
       401,
   )


@jwt.unauthorized_loader
def missing_token_callback(error):
   return (
       jsonify(
           {
               "description": "Request does not contain an access token.",
               "error": "authorization_required",
           }
       ),
       401,
   )

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_restful import Api
from flask_jwt_extended import JWTManager
import server.jwt_setup

os.environ.setdefault('POSTGRES_USER', 'mock_user')
os.environ.setdefault('POSTGRES_PASSWORD', 'mock_password')
os.environ.setdefault('POSTGRES_HOST', 'localhost')
os.environ.setdefault('POSTGRES_DB', 'mock_db')

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_Key', 'mock_secret_key')

db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)
migrate = Migrate(app, db)

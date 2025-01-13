from server.globals import db
from server.models.user import UserModel
from server.models.category import CategoryModel
import uuid
import pytz
from datetime import datetime


class RecordModel(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.String(32), primary_key=True,
                   default=lambda: uuid.uuid4().hex)
    user_id = db.Column(db.String(32), db.ForeignKey('users.id'))
    user = db.relationship('UserModel', backref='records')
    category_id = db.Column(db.String(32), db.ForeignKey('categories.id'))
    category = db.relationship('CategoryModel', backref='records')
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.now(pytz.utc))

    def __init__(self, user_id, category_id, amount):
        self.user_id = user_id
        self.category_id = category_id
        self.amount = amount
        user = UserModel.query.get(self.user_id)
        if not user:
            raise ValueError(f"User with id: {self.user_id} not found")

        user.subtract_money_from_wallet(amount)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'amount': self.amount,
            'date': self.date.strftime('%d-%m-%Y %H:%M:%S')
        }

from datetime import datetime
import pytz
import uuid

zone = pytz.timezone('Etc/GMT+2')


class RecordModel(db.Model):
    __tablename__ = 'records'

    id = db.Column(db.String(32), primary_key=True,
                   default=lambda: uuid.uuid4().hex)
    user_id = db.Column(db.String(32), nullable=False)
    category_id = db.Column(db.String(32), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=lambda: datetime.now(pytz.utc))

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'amount': self.amount,
            'date': self.date.strftime('%d-%m-%Y %H:%M:%S')
        }

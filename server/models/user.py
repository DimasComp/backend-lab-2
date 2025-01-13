import uuid
from server.globals import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(32), primary_key=True,
                   default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name
        }

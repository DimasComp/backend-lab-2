from server.globals import db
from server.models.wallet import WalletModel
import uuid


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(32), primary_key=True,
                   default=lambda: uuid.uuid4().hex)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    wallet_id = db.Column(db.String(32), db.ForeignKey('wallets.id'))
    wallet = db.relationship('WalletModel', backref='user', uselist=False)

    def add_money_to_wallet(self, amount):
        self.wallet.add_money(amount)

    def subtract_money_from_wallet(self, amount):
        self.wallet.subtract_money(amount)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'wallet': self.wallet.to_dict()
        }

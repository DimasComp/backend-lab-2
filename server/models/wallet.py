from server.globals import db
import uuid

class WalletModel(db.Model):
    __tablename__ = 'wallets'

    id = db.Column(db.String, primary_key=True, default=lambda: uuid.uuid4().hex)
    balance = db.Column(db.Float, default=0.0)

    def add_money(self, amount):
        self.balance += amount
        db.session.commit()

    def subtract_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            db.session.commit()
        else:
            raise ValueError("Insufficient funds in wallet")
    
    def to_dict(self):
        return {
            'id': self.id,
            'balance': self.balance
        }

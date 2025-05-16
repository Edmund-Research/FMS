from . import db

class Transaction(db.Model):
    transaction_id   = db.Column(db.Integer, primary_key=True)
    amount           = db.Column(db.Float)
    num_failed_logins= db.Column(db.Integer)
    is_foreign       = db.Column(db.Boolean)
    hour             = db.Column(db.Integer)
    fraud_rule_flag  = db.Column(db.Boolean)
    ml_pred          = db.Column(db.Boolean)

class FraudCase(db.Model):
    case_register_id = db.Column(db.Integer, primary_key=True)
    transaction_id   = db.Column(db.Integer, db.ForeignKey('transaction.transaction_id'))
    flagged_at       = db.Column(db.DateTime, server_default=db.func.now())

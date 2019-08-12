from app import db

class Order(db.Model):
    """
        Order model to store order information.
    """
    id = db.Column(db.Integer, primary_key = True)
    customer_name = db.Column(db.String(50))
    currency = db.Column(db.String(10))
    total_price = db.Column(db.Float)
    sub_total_price = db.Column(db.Float)
    created_at = db.Column(db.DateTime)
    email = db.Column(db.String(80), nullable=True)
    phone_no = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(200))
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)

from app.order.views import order as order_module
app.register_blueprint(order_module)

db.create_all()
import os
import uuid

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
BASE_DIR = os.path.abspath(os.path.dirname(__name__))
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://shubham:shubhamcs@127.0.0.1:5432/Order'
SHOPIFY_KEY = b'c8169a0fa2a87c528c856bc2e3d7f5f0837731683594364cbbc830883e7f8e6f'
SECRET_KEY = str(uuid.uuid4())

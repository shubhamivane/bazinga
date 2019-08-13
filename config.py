import os
import uuid
import dotenv


BASE_DIR = os.path.abspath(os.path.dirname(__name__))
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = str(uuid.uuid4())
SHOPIFY_KEY = b'c8169a0fa2a87c528c856bc2e3d7f5f0837731683594364cbbc830883e7f8e6f'
dotenv_file = os.path.join(BASE_DIR, ".env")
SQLALCHEMY_DATABASE_URI = None
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
if not SQLALCHEMY_DATABASE_URI:
    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://lsftwfubnhqqhk:a975fdf2b3aa7e1489b4065565b47e08bd98f4c2c4b384e83e9629bdfb487e24@ec2-54-225-119-13.compute-1.amazonaws.com:5432/db44brfhai45f'
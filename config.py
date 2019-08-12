import os
import uuid
import dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__name__))
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)
DEBUG = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = str(uuid.uuid4())
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
SHOPIFY_KEY = b'c8169a0fa2a87c528c856bc2e3d7f5f0837731683594364cbbc830883e7f8e6f'

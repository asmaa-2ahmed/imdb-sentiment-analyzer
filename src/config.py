import os
from dotenv import load_dotenv

load_dotenv(override=True)

APP_NAME = os.getenv('APP_NAME')
VERSION = os.getenv('VERSION')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')

Base_Path = os.path.dirname(os.path.abspath(__file__))
ASSETS_Path = os.path.join(Base_Path, "assets")
VIEW_PATH= os.path.join(Base_Path ,"views")

vocab_size = 10000
embed_size = 128
epochs = 5
batch_size = 64
max_seq_len = 300


import os
import dotenv
from sqlalchemy import create_engine


dotenv.load_dotenv(".env")

dialect = 'postgresql'
username = os.environ.get('PG_USER')
password = os.environ.get('PG_PASSWORD')
host = '127.0.0.1'
port = '5431'
database = os.getenv("PG_DB")

DSN = f'{dialect}://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(DSN)
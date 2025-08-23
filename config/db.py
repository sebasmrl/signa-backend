import os
from sqlalchemy import create_engine, MetaData

sqlite_filename = '../db/database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_filename)}"

DATABASE_URL = os.getenv("DATABASE_URL", database_url)

#Engine
engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()

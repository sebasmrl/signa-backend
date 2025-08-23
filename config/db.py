import os
from sqlalchemy import create_engine, MetaData

base_dir = os.path.dirname(os.path.realpath(__file__))
database_url = f"sqlite:///{os.path.join(base_dir, '..', 'db', 'database.sqlite')}"

DATABASE_URL = os.getenv("DATABASE_URL", database_url)

#Engine
engine = create_engine(DATABASE_URL)
meta = MetaData()
conn = engine.connect()

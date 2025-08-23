from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

brands = Table('brands', meta,
               Column('id', Integer, primary_key=True, autoincrement=True),
               Column('owner', String(length=50)),
               Column('brand', String(length=50)),
               Column('state', Boolean, default=False)
               )
#Añadir configuración
meta.create_all(engine) 

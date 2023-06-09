from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer
from config.db import meta

users  = Table(
    'users', meta,
    Column('id', Integer, primary_key=True)
    )
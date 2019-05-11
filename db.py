import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.interfaces import ConnectionProxy
import sys

import config

engine = sqlalchemy.create_engine(config.SQL_ALCHEMY_URI,
                                  isolation_level="READ COMMITTED",
                                  pool_recycle=3600)
_session = sessionmaker(bind=engine)
session = _session()

from db import engine, session
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import desc

import model
from db import session


def years():
    return session.query(model.Year).all()


year = None

try:
    year = session.query(model.Year).order_by(desc(model.Year.id)).first()
except SQLAlchemyError:
    session.rollback()
    raise
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from ml_ops_labs.db.tools import get_dsn
from sqlalchemy.orm import sessionmaker
from datetime import datetime


Base = declarative_base()


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    text = Column(String, nullable=False)


engine = create_engine(get_dsn(with_params=False))
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


# Пример добавления записи в таблицу Log
def add_log_entry(log_text):
    new_log = Log(text=log_text)
    session.add(new_log)
    session.commit()

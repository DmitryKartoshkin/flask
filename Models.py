from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import sessionmaker

from dsn import engine


Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)


class Advert(Base):
    __tablename__ = "advertisements"

    id = Column(Integer, primary_key=True)
    heading = Column(String(length=150), nullable=False)
    description = Column(Text, nullable=False)
    owner = Column(String(length=40))
    date_creat = Column(DateTime, server_default=func.now())


Base.metadata.create_all(bind=engine)

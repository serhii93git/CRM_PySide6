from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker



DATABASE_URL = 'postgresql+psycopg2://postgres:12159374@localhost:5432/crm'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)

Base.metadata.create_all(engine)


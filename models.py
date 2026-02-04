from sqlalchemy import Column, Integer, String
from database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    subject = Column(String)
    price = Column(Integer)
    experience = Column(Integer)

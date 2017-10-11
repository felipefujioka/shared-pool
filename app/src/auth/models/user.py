from db.util import BaseModel
from sqlalchemy import Column, Integer, String, DateTime

class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

from db.util import BaseModel
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime

class PasswordCredential(BaseModel):
    __tablename__ = 'password_credentials'

    user_id = Column('user_id', Integer, ForeignKey("user.id"), nullable=False),
    password_hash = Column(String(), nullable=False)
    updated_at = Column(DateTime, nullable=False)

from db.util import BaseModel
from sqlalchemy import Column, ForeignKey, PrimaryKeyConstraint, Integer, String, DateTime


class PasswordCredential(BaseModel):
    __tablename__ = 'password_credentials'
    __table_args__ = (
        PrimaryKeyConstraint('user_id'),
    )

    user_id = Column('user_id', Integer, ForeignKey("user.id"))
    password_hash = Column(String(), nullable=False)
    updated_at = Column(DateTime, nullable=False)

import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

BaseModel = declarative_base()

engine = create_engine(os.environ['DATABASE_URL'])

BaseModel.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from conf import *

engine = create_engine('postgresql://{}:{}@{}:{}/sqlalchemy'.format(user, password, host, port))
Session = sessionmaker(bind=engine)

Base = declarative_base()
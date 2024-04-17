from dotenv import load_dotenv
load_dotenv()
import os
import sqlalchemy as db
engine = db.create_engine('sqlite:///main.db', echo=True)
metadata = db.MetaData()
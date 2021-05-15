from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from setting import Setting
setting = Setting()

engine = create_engine(setting.SQLALCHEMY_DATABASE_URL)
db = sessionmaker(autocommit=False, autoflush=False, bind=engine)

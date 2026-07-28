from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = "hero"
DB_PASSWORD = "hero.9493"  
DB_HOST = "localhost"     
DB_PORT = "3306"          
DB_NAME = "user_db"  

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{"hero@localhost"}:{"hero.9493"}@{localhost}:{3306}/{user_db}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
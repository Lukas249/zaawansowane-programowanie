from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_engine():
    DATABASE_URL = "sqlite:///./database/sqlite.db"
    return create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

def get_session():
    engine = get_engine()
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)()
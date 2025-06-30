from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load your database URL from .env or use a default
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/Registration"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ✅ This is what FastAPI expects
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = 'postgresql://kadanur:password@localhost/kupur-db'
SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://default:s0rvYRJ1OyTu@ep-steep-sea-a2zkedyl.eu-central-1.aws.neon.tech:5432/verceldb?sslmode=require'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)

SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
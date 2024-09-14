from sqlalchemy import Column, Integer, String
from database import Base

class News(Base):
    __tablename__ = "news"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    title = Column(String)
    description = Column(String)
    source = Column(String)
    sourceUrl = Column(String)
    imageUrl = Column(String)
    category = Column(String)
    author = Column(String)
    date = Column(String)

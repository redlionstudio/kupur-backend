from sqlalchemy import Column, Integer, String, Float
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

class SystemCheck(Base):
    __tablename__ = "system_information"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    minimumIOSVersion = Column(String)
    minimumAndroidVersion = Column(String)
    appStoreUrl = Column(String)
    playStoreUrl = Column(String)

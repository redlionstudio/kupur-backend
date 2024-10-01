from fastapi import HTTPException
from sqlalchemy.orm import Session
import mobile_app.mobile_schemas as mobile_schemas
import mobile_app.mobile_models as mobile_models
import common.common_schemas as common_schemas

def createNews(db: Session, news: mobile_schemas.CreateNews):
    db_news = mobile_models.News(
        title = news.title,
        description = news.description,
        source = news.source,
        sourceUrl = news.source,
        imageUrl = news.imageUrl,
        category = news.category,
        author = news.author,
        date = news.date
    )
    
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    
    return db_news

def getNewsList(db: Session):
    return db.query(mobile_models.News).all()

def deleteNewsById(db: Session, id: int):
    db_news = db.query(mobile_models.News).filter(mobile_models.News.id == id).first()

    if db_news is None:
        raise HTTPException(status_code=404, detail="News is not found.")
    
    db.delete(db_news)
    db.commit()

    return common_schemas.StatusResponse(status= True)

def get_news_detail_by_id(db: Session, id: int):
    db_news = db.query(mobile_models.News).filter(mobile_models.News.id == id).first()

    if db_news is None:
        raise HTTPException(status_code=404, detail="News is not found.")
    
    return db_news
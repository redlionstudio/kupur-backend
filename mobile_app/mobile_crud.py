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
        sourceUrl = news.sourceUrl,
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

def get_system_check_informations(db: Session):
    db_system_check = db.query(mobile_models.SystemCheck).first()

    if db_system_check is None:
        raise HTTPException(status_code=404, detail="System check is not found.")

    return mobile_schemas.SystemCheckResponse(
        minimumIOSVersion = db_system_check.minimumIOSVersion,
        minimumAndroidVersion = db_system_check.minimumAndroidVersion,
        appStoreUrl = db_system_check.appStoreUrl,
        playStoreUrl = db_system_check.playStoreUrl
    )

def update_system_check_informations(db: Session, system_check_informations: mobile_schemas.SystemCheckResponse):
    db_system_check = db.query(mobile_models.SystemCheck).first()

    if db_system_check is None:
        raise HTTPException(status_code=404, detail="System check is not found.")

    db_system_check.minimumIOSVersion = system_check_informations.minimumIOSVersion
    db_system_check.minimumAndroidVersion = system_check_informations.minimumAndroidVersion
    db_system_check.appStoreUrl = system_check_informations.appStoreUrl
    db_system_check.playStoreUrl = system_check_informations.playStoreUrl

    db.commit()
    db.refresh(db_system_check)

    return system_check_informations

def update_news(db: Session, id: int, updated_news: mobile_schemas.CreateNews):
    db_news = db.query(mobile_models.News).filter(mobile_models.News.id == id).first()

    if db_news is None:
        raise HTTPException(status_code=404, detail="News is not found.")

    db_news.title = updated_news.title
    db_news.description = updated_news.description
    db_news.source = updated_news.source
    db_news.sourceUrl = updated_news.sourceUrl
    db_news.imageUrl = updated_news.imageUrl
    db_news.category = updated_news.category
    db_news.author = updated_news.author
    db_news.date = updated_news.date

    db.commit()
    db.refresh(db_news)

    return updated_news
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from typing import List
import mobile_app.mobile_schemas as mobile_schemas
import common.common_schemas as common_schemas
import mobile_app.mobile_crud as crud

router = APIRouter()

@router.post("/news", response_model=mobile_schemas.News, tags= ["Not Mobile"])
def create_news(news: mobile_schemas.CreateNews, db: Session = Depends(get_db)):
    return crud.createNews(db = db, news = news)

@router.get("/news/list", response_model= List[mobile_schemas.News], tags=["Mobile"])
def get_news_list(db: Session = Depends(get_db)):
    return crud.getNewsList(db = db)

@router.delete("/news/{id}", response_model= common_schemas.StatusResponse, tags=["Not Mobile"])
def delete_news_by_id(id: int, db: Session = Depends(get_db)):
    return crud.deleteNewsById(db = db, id= id)

@router.get("/news/{id}", response_model= mobile_schemas.News, tags=["Mobile"])
def get_news_detail(id: int, db: Session = Depends(get_db)):
    return crud.get_news_detail_by_id(db = db, id = id)
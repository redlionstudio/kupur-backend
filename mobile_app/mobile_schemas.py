from pydantic import BaseModel

class News(BaseModel):
    id: int
    title: str
    description: str
    source: str
    sourceUrl: str
    imageUrl: str
    category: str
    author: str
    date: str

class CreateNews(BaseModel):
    title: str
    description: str
    source: str
    sourceUrl: str
    imageUrl: str
    category: str
    author: str
    date: str

class SystemCheckResponse(BaseModel):
    minimumIOSVersion: str
    minimumAndroidVersion: str
    appStoreUrl: str
    playStoreUrl: str
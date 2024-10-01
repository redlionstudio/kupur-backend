from fastapi import FastAPI
from database import engine
import mobile_app.mobile_models as mobile_models
from mobile_app.mobile_routes import router as mobile_router

mobile_models.Base.metadata.create_all(bind = engine)

app = FastAPI(title= "Kupur Backend")

app.include_router(mobile_router)

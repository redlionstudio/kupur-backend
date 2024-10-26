from fastapi import FastAPI
from database import engine
import mobile_app.mobile_models as mobile_models
from mobile_app.mobile_routes import router as mobile_router
from fastapi.middleware.cors import CORSMiddleware


mobile_models.Base.metadata.create_all(bind = engine)

app = FastAPI(title= "Kupur Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(mobile_router)

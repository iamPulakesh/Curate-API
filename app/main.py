import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from app.database import Base, engine
from app.routes import user_routes, item_routes, recommendation_routes
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
APP_HOST = os.getenv("APP_HOST")
APP_PORT = int(os.getenv("APP_PORT"))

app = FastAPI(title=APP_NAME)

@app.get("/")
def root():
    return FileResponse("homepage/index.html")

app.mount("/homepage", StaticFiles(directory="homepage"))

# create DB tables
Base.metadata.create_all(bind=engine)

# registering routers
app.include_router(user_routes.router)
app.include_router(item_routes.router)
app.include_router(recommendation_routes.router)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",  
        host=APP_HOST,
        port=APP_PORT,
        reload=True
    )

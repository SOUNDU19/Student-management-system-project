from fastapi import FastAPI
from app.database.database import engine, Base
from app.models.student import Student

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to EduManage Student Management System"
    }
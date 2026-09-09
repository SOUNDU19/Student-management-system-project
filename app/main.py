from fastapi import FastAPI

from app.database.database import engine, Base
from app.models.student import Student
from app.routes.student import router as student_router


Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(student_router)


@app.get("/")
def home():
    return {
        "message": "Welcome to EduManage Student Management System"
    }
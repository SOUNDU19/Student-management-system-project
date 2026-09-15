from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentResponse
from app.schemas.student import StudentCreate, StudentResponse, StudentUpdate
router = APIRouter()


@router.post("/students", response_model=StudentResponse)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    new_student = Student(
        name=student.name,
        email=student.email,
        age=student.age,
        department=student.department
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

@router.get("/students/{student_id}", response_model=StudentResponse)
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student

@router.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student_data: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    student.name = student_data.name
    student.email = student_data.email
    student.age = student_data.age
    student.department = student_data.department

    db.commit()
    db.refresh(student)

    return student

@router.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }
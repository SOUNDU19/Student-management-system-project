from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=17, le=100)
    department: str = Field(min_length=2, max_length=100)


class StudentUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    age: int = Field(ge=17, le=100)
    department: str = Field(min_length=2, max_length=100)


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    department: str

    class Config:
        from_attributes = True
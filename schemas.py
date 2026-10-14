from pydantic import BaseModel

class TeacherCreate(BaseModel):
    name: str
    subject: str
    price: int
    experience: int

class TeacherOut(TeacherCreate):
    id: int

    class Config:
        orm_mode = True

log 

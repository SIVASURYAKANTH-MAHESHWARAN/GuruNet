from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models, schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Teacher Branding Platform")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add teacher (teacher becomes a brand)
@app.post("/teachers", response_model=schemas.TeacherOut)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    new_teacher = models.Teacher(**teacher.dict())
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return new_teacher

# View all teachers (student side)
@app.get("/teachers", response_model=list[schemas.TeacherOut])
def get_teachers(db: Session = Depends(get_db)):
    return db.query(models.Teacher).all()

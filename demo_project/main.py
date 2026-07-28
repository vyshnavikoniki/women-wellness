from fastapi import FastAPI, Depends, Form, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
import database

class User(database.Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    gender = Column(String)
    country = Column(String)

database.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register")
def register_user(
    name: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    gender: str = Form(None), # Optional, as radio buttons might not be selected
    country: str = Form(...),
    db: Session = Depends(get_db)
):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user object
    # NOTE: In a real app, you must hash the password (e.g., using bcrypt) before saving!
    new_user = User(
        name=name,
        email=email,
        password=password, 
        gender=gender,
        country=country
    )

    # Save to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Return a success message or redirect
    return {"message": f"User {name} successfully registered!", "user_id": new_user.id}
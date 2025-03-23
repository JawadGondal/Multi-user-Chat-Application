import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from Chat_app.auth import get_password_hash, verify_password, create_access_token
from Chat_app.database import get_db
from Chat_app.models import User
from datetime import timedelta
from fastapi.security import OAuth2PasswordBearer

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

@router.post("/api/register")
def register(username: str, email: str, password: str, db: Session = Depends(get_db)):
    hashed_password = get_password_hash(password)
    user = User(username=username, email=email, password_hash=hashed_password)
    db.add(user)
    db.commit()
    return {"message": "User registered successfully"}

@router.post("/api/login")
def login(email:str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token({"sub": str(user.id)}, timedelta(minutes=30))
    return {"access token": access_token,"token_type": "bearer"}

@router.post("/api/logout")
def logout(token: str = Depends(oauth2_scheme)):
    return {"message":"Logout successfully"}
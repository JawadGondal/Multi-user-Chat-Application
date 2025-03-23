import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Chat_app.models import ChatRoom, Message
from Chat_app.database import get_db
from datetime import datetime, timezone

router = APIRouter()

@router.get("/api/chat/rooms")
def get_chat_rooms(db: Session = Depends(get_db)):
    return db.query(ChatRoom).all()

@router.get("/api/chat/room/{room_id}")
def get_chat_room(room_id: int, db: Session = Depends(get_db)):
    return db.query(ChatRoom).filter(ChatRoom.id == room_id).first()

@router.post("/api/chat/rooms/{room_id}/messages")
def send_message(room_id: int, text: str, sender_id: int, db: Session = Depends(get_db)):
    message = Message(text=text, sender_id=sender_id, room_id=room_id, created_at =datetime.now(timezone.utc))
    db.add(message)
    db.commit()
    return {"message":"Message sent successfully"}

@router.get("/api/chat/rooms/{room_id}/messages")
def get_messages(room_id: int, db: Session = Depends(get_db)):
    return db.query(Message).filter(Message.room_id == room_id).all()
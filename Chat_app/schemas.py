from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

# User Schemas
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime
    
    class config:
        from_attributes = True
        
# Chat Room Schemas
class ChatRoomCreate(BaseModel):
    name: str
    
class ChatRoomResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    
    class config:
        from_attributes = True

# Message Schemas 
class MessageCreate(BaseModel):
    text: str
    sender_id: int
    room_id: int
    
class MessageResponse(BaseModel):
    id: int
    text: str
    sender_id: int
    room_id: int
    created_at: datetime
    
    class config:
        from_attributes = True

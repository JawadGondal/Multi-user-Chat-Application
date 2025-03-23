import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from Chat_app.database import engine, Base
from routes import users, chat
from websocket import router as ws_router

app = FastAPI()
# Mount the templates directory
templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(bind =engine)

app.include_router(users.router)
app.include_router(chat.router)
app.include_router(ws_router)

# Route to serve chat.html
@app.get("/chat/{room_id}", response_class=HTMLResponse)
async def get_chat_page(request: Request, room_id: int):
    return templates.TemplateResponse("chat.html", {"request": request, "room_id": room_id})
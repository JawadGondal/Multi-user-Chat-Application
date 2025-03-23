from fastapi import APIRouter, WebSocket
from typing import Dict, List

router = APIRouter()

# Dictionary to store active connections for each room
rooms: Dict[int, List[WebSocket]] = {}

@router.websocket("/ws/chat/{room_id}/{sender_name}")
async def websocket_endpoint(websocket: WebSocket, room_id: int, sender_name: str):
    await websocket.accept()

    if room_id not in rooms:
        rooms[room_id] = []

    rooms[room_id].append(websocket)

    try:
        while True:
            data = await websocket.receive_text()
            message = f"Room {room_id} {sender_name}: {data}"

            # Send message to all users in the same room
            for connection in rooms[room_id]:
                await connection.send_text(message)

    except:
        rooms[room_id].remove(websocket)

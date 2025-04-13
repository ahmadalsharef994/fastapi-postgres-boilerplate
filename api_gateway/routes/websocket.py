# --- api_gateway/routes/websocket.py ---
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from events.event_bus import event_bus

router = APIRouter()

connected_clients = set()

@router.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    connected_clients.add(ws)
    try:
        while True:
            data = await ws.receive_text()
            await event_bus.publish("chat_message", data)
    except WebSocketDisconnect:
        connected_clients.remove(ws)

# Event Listener for broadcasting
async def broadcast_message(message):
    disconnected = []
    for client in connected_clients:
        try:
            await client.send_text(f"Broadcast: {message}")
        except WebSocketDisconnect:
            disconnected.append(client)
    for d in disconnected:
        connected_clients.remove(d)

event_bus.subscribe("chat_message", broadcast_message)

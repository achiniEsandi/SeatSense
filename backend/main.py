from fastapi import FastAPI, WebSocket
from backend.routes import router

app = FastAPI(title="SeatSense Backend")

# Include API routes
app.include_router(router)

# WebSocket for real-time updates
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # For now, just echo
        await websocket.send_text(f"Received: {data}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

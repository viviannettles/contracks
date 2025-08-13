from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

static_path = Path(__file__).parent / "static"

# Mount static files (JS, CSS, images)
app.mount("/static", StaticFiles(directory=static_path / "static"), name="static")

@app.get("/")
def serve_react_app():
    return FileResponse(static_path / "index.html")

# Example API route
@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!"}


# Catch-all route to serve React frontend
@app.get("/{full_path:path}")
def serve_react(full_path: str):
    return FileResponse(os.path.join("templates", "index.html"))

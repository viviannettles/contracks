from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Mount static files (JS, CSS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")


# Example API route
@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI!"}


# Catch-all route to serve React frontend
@app.get("/{full_path:path}")
def serve_react(full_path: str):
    return FileResponse(os.path.join("templates", "index.html"))

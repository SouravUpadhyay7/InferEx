import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from models_db import MODELS_DB
from models_db.data import CATEGORIES

app = FastAPI(title="InferEx AI Hub", description="A premium Model Zoo & Learning Platform")

# Ensure static subdirectories exist
os.makedirs("static/models", exist_ok=True)
os.makedirs("static/notebooks", exist_ok=True)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ---------------------------------------------------------------------------
# Generate dummy placeholder files so downloads work out-of-the-box
# ---------------------------------------------------------------------------
for model in MODELS_DB:
    model_path = f"static/models/{model['model_file']}"
    notebook_path = f"static/notebooks/{model['notebook_file']}"
    if not os.path.exists(model_path):
        with open(model_path, "w") as f:
            f.write("Dummy Model Weights")
    if not os.path.exists(notebook_path):
        with open(notebook_path, "w") as f:
            f.write('{"cells": [], "metadata": {}, "nbformat": 4, "nbformat_minor": 5}')


# ---------------------------------------------------------------------------
# Page Routes
# ---------------------------------------------------------------------------

@app.get("/", response_class=HTMLResponse)
async def home_route(request: Request):
    """Landing page — professional hero + category showcase."""
    stats = {
        "total_models": len(MODELS_DB),
        "total_categories": len(CATEGORIES),
        "total_notebooks": len(MODELS_DB),
    }
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "categories": CATEGORIES, "stats": stats}
    )


@app.get("/explore", response_class=HTMLResponse)
async def explore_route(request: Request):
    """Browse & filter all models across all categories."""
    return templates.TemplateResponse(
        "explore.html",
        {"request": request, "models": MODELS_DB, "categories": CATEGORIES}
    )


@app.get("/model/{model_id}", response_class=HTMLResponse)
async def model_detail_route(request: Request, model_id: str):
    """Individual model detail page."""
    model_data = next((m for m in MODELS_DB if m["id"] == model_id), None)
    if not model_data:
        return HTMLResponse("<h1>Model not found</h1>", status_code=404)
    return templates.TemplateResponse(
        "model.html",
        {"request": request, "model": model_data}
    )


# ---------------------------------------------------------------------------
# Download / Static Routes
# ---------------------------------------------------------------------------


@app.get("/api/download/model/{filename}")
async def api_download_model(filename: str):
    file_path = f"static/models/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/octet-stream", filename=filename)
    return {"error": "File not found"}


@app.get("/api/download/notebook/{filename}")
async def api_download_notebook(filename: str):
    file_path = f"static/notebooks/{filename}"
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="application/x-ipynb+json", filename=filename)
    return {"error": "File not found"}

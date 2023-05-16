from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

curr_path = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(curr_path, 'templates')

app = FastAPI()
templates = Jinja2Templates(directory=templates_path)

@app.get("/")
async def index(request:Request, visitors: int = 0):
    return templates.TemplateResponse(name = "index.html", context = {"request":request, "visitors":visitors}, status_code=200)

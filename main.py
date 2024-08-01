from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from api import tasks
from database.client import database
from database.models.templates import Templates

app = FastAPI()
app.include_router(tasks.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=Templates.RESPONSE)
async def root(request: Request):
    _tasks = list(database.tasks.find())
    
    try:
        return Templates.HTML.TemplateResponse("index.html", {"request": request, "tasks": _tasks, "status": "Operational"})
    except Exception as err:
        return Templates.HTML.TemplateResponse("error.html", {"request": request, "status": f"System Error: {str(err)}"})

from fastapi import APIRouter, Request, Form, HTTPException, status
from fastapi.responses import RedirectResponse, JSONResponse
from bson.objectid import ObjectId
from database.client import database
from database.models.task import Task
from database.models.templates import Templates
from datetime import datetime

router = APIRouter(
    tags=["task_panel"]
)

@router.post("/add_task", response_class=Templates.RESPONSE)
async def post_add_task(
    request: Request,
    name: str = Form(...),
    description: str = Form(...),
    due_date: datetime = Form(...)
):
    task = Task(
        name=name,
        description=description,
        due_date=due_date
    )
    
    database.tasks.insert_one(task.model_dump())
    return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)

@router.delete("/delete_task", response_class=Templates.RESPONSE)
async def delete_task(request: Request):
    try:
        data = await request.json()
        task_id = ObjectId(data.get("taskId"))
        
        if not task_id:
            raise HTTPException(status_code=400, detail="Task ID is required.")
        
        result = database.tasks.delete_one({"_id": task_id})
        
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Task not found")

        return JSONResponse(content={"status": "Task deleted successfully."})

    except Exception as e:
        return JSONResponse(content={"status": f"Error: {str(e)}"}, status_code=500)
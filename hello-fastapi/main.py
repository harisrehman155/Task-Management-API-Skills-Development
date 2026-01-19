from fastapi import FastAPI, HTTPException, Depends, status
from database import create_db_and_tables, get_session
from models import Task
from sqlmodel import Session, select

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/tasks")
def list_tasks(session: Session = Depends(get_session)):
    tasks = session.exec(select(Task)).all()
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int, session: Session = Depends(get_session)):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/tasks", status_code=201)
def create_task(
    task: Task,
    session: Session = Depends(get_session)
):
    session.add(task)
    session.commit()
    session.refresh(task)  # Get the assigned ID
    return task

@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task_update: Task,
    session: Session = Depends(get_session)
):
    task = session.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = task_update.title
    task.description = task_update.description
    task.status = task_update.status

    session.add(task)
    session.commit()
    session.refresh(task)
    return task

@app.delete("/delete/{task_id}", status_code=204)
def delete_task(task_id:int, session:Session=Depends(get_session)):
    task = session.get(Task,task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task Not Found")
    session.delete(task)
    session.commit()
    return None

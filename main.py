from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Task Manager API",
    description="Простой CRUD для задач в памяти",
    version="1.0.0",
)


# ---------- Модели ----------

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    done: bool = False


# ---------- "База данных" в памяти ----------

tasks: dict[int, Task] = {}
next_id: int = 1


# ---------- CRUD ----------

@app.get("/tasks", response_model=list[Task], tags=["Tasks"])
def list_tasks():
    """Получить список всех задач."""
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def get_task(task_id: int):
    """Получить задачу по ID."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]


@app.post("/tasks", response_model=Task, status_code=status.HTTP_201_CREATED, tags=["Tasks"])
def create_task(payload: TaskCreate):
    """Создать новую задачу."""
    global next_id
    task = Task(id=next_id, **payload.model_dump())
    tasks[next_id] = task
    next_id += 1
    return task


@app.put("/tasks/{task_id}", response_model=Task, tags=["Tasks"])
def update_task(task_id: int, payload: TaskUpdate):
    """Обновить задачу."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]
    data = payload.model_dump(exclude_unset=True)
    updated = task.model_copy(update=data)
    tasks[task_id] = updated
    return updated


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Tasks"])
def delete_task(task_id: int):
    """Удалить задачу."""
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[task_id]
    return None
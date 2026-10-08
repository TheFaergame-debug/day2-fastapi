from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_task_service
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import TaskNotFoundError, TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("", response_model=list[TaskResponse])
def list_tasks(service: TaskService = Depends(get_task_service)):
    return service.list_tasks()


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, service: TaskService = Depends(get_task_service)):
    try:
        return service.get_task(task_id)
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(
    payload: TaskCreate,
    service: TaskService = Depends(get_task_service),
):
    try:
        return service.create_task(payload)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    payload: TaskUpdate,
    service: TaskService = Depends(get_task_service),
):
    try:
        return service.update_task(task_id, payload)
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    try:
        service.delete_task(task_id)
    except TaskNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
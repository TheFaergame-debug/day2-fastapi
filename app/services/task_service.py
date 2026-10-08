from typing import Optional
from app.models.task import Task
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate


class TaskNotFoundError(Exception):
    """Задача не найдена."""


class TaskService:
    """Бизнес-логика для задач."""

    def __init__(self, repository: TaskRepository) -> None:
        self._repo = repository

    def list_tasks(self) -> list[Task]:
        return self._repo.get_all()

    def get_task(self, task_id: int) -> Task:
        task = self._repo.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundError(f"Task with id={task_id} not found")
        return task

    def create_task(self, payload: TaskCreate) -> Task:
        # Пример бизнес-правила: нельзя создать уже выполненную задачу
        if payload.done:
            raise ValueError("Cannot create a task with done=True")
        return self._repo.create(
            title=payload.title,
            description=payload.description,
            done=payload.done,
        )

    def update_task(self, task_id: int, payload: TaskUpdate) -> Task:
        # Проверяем существование
        if self._repo.get_by_id(task_id) is None:
            raise TaskNotFoundError(f"Task with id={task_id} not found")

        data = payload.model_dump(exclude_unset=True)
        updated = self._repo.update(task_id, **data)
        assert updated is not None
        return updated

    def delete_task(self, task_id: int) -> None:
        if not self._repo.delete(task_id):
            raise TaskNotFoundError(f"Task with id={task_id} not found")
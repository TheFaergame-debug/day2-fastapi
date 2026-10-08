from typing import Optional
from app.models.task import Task


class TaskRepository:
    """Хранилище задач в памяти."""

    def __init__(self) -> None:
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def get_all(self) -> list[Task]:
        return list(self._tasks.values())

    def get_by_id(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)

    def create(self, title: str, description: Optional[str], done: bool) -> Task:
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            done=done,
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def update(self, task_id: int, **fields) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if task is None:
            return None
        for key, value in fields.items():
            if value is not None:
                setattr(task, key, value)
        return task

    def delete(self, task_id: int) -> bool:
        if task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True
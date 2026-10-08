from functools import lru_cache

from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService


@lru_cache
def get_task_repository() -> TaskRepository:
    """Создаём репозиторий один раз на весь процесс."""
    return TaskRepository()


def get_task_service() -> TaskService:
    """Собираем сервис, прокидывая в него репозиторий."""
    return TaskService(repository=get_task_repository())
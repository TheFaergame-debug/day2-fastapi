# Отчёт по Дню 3

## Теория
Разобрал слоистую архитектуру (API / Service / Repository / Schemas / Models),
принципы Clean Code, SRP, DRY, DI через Depends.

## Практика
- Создал ветку refactor/layered-architecture
- Разбил монолитный main.py на слои:
  - app/main.py — точка входа
  - app/api/tasks.py — HTTP-роутеры
  - app/services/task_service.py — бизнес-логика
  - app/repositories/task_repository.py — хранилище
  - app/schemas/task.py — Pydantic DTO
  - app/models/task.py — доменная модель
  - app/dependencies.py — DI
- Добавил бизнес-правило: нельзя создать задачу с done=True
- Проверил все эндпоинты через Swagger (включая 400 на бизнес-правило)
- Создал PR, провёл Code Review, смержил в main

## Результат
- Приложение работает так же, как в Дне 2
- Структура проекта профессиональная
- PR: https://github.com/TheFaergame-debug/day2-fastapi/pull/2
- Репозиторий: https://github.com/TheFaergame-debug/day2-fastapi

## Проблемы и решения
- Имена файлов не совпадали с импортами
  (tasks.py вместо task.py, tasks.py вместо task_service.py) →
  переименовал через Rename-Item в PowerShell
- Локальная ветка была удалена до merge PR → восстановил через
  merge PR на GitHub и git pull

## Вывод
Понял, зачем нужны слои: замена БД, тестирование, работа в команде.
API-слой не знает про SQL, Service — про HTTP, Repository — про бизнес-правила.
Это позволяет менять любую часть независимо.

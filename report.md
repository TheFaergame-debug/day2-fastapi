# Отчёт по Дню 2

## Теория
Разобрал клиент-серверную архитектуру, HTTP-методы и коды ответов,
REST API, JSON, FastAPI, OpenAPI/Swagger.

## Практика
- Установил Python, создал виртуальное окружение (venv)
- Установил FastAPI и uvicorn
- Реализовал CRUD для задач в памяти:
  - GET /tasks — список всех задач
  - GET /tasks/{id} — одна задача
  - POST /tasks — создание (201)
  - PUT /tasks/{id} — частичное обновление
  - DELETE /tasks/{id} — удаление (204)
- Обработал 404 для несуществующих задач
- Протестировал все эндпоинты через Swagger UI

## Результат
- Приложение работает на http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- Репозиторий: https://github.com/TheFaergame-debug/day2-fastapi

## Проблемы и решения
- PowerShell блокировал активацию venv → 
  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
- В .gitignore не хватало __pycache__/ → дополнил

## Вывод
Освоил базовый REST API на FastAPI. Понял, как HTTP-методы
мапятся на CRUD-операции. Swagger UI — удобный инструмент
для тестирования API без Postman. Pydantic автоматически
валидирует входящие данные.


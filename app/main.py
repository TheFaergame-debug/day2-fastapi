from fastapi import FastAPI

from app.api.tasks import router as tasks_router

app = FastAPI(
    title="Task Manager API",
    description="CRUD для задач, слоистая архитектура",
    version="2.0.0",
)

app.include_router(tasks_router)


@app.get("/", tags=["Health"])
def health_check():
    return {"status": "ok"}
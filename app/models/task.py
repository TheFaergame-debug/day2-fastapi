from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    description: str | None = None
    done: bool = False
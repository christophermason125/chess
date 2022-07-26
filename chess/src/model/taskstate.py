from enum import Enum, auto


class TaskState(Enum):
    READY = auto()
    SCHEDULED = auto()
    RUNNING = auto()
    CANCELED = auto()
    FINISHED = auto()

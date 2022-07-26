from abc import ABC, abstractmethod

from chess.src.model.taskstate import TaskState


class Task(ABC):
    base_priority = None

    def __init__(self):
        self._priority = self.base_priority
        self._state = TaskState.READY

    @property
    def state(self):
        return self._state

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority):
        if self.state == TaskState.SCHEDULED:
            raise ValueError(f"{self}'s priority cannot be changed once scheduled.")
        self._priority = priority

    def cancel(self):
        self._state = TaskState.CANCELED

    def set_scheduled(self):
        self._state = TaskState.SCHEDULED

    def run(self, *args, **kwargs):
        if self._state == TaskState.READY or self._state == TaskState.SCHEDULED:
            self._state = TaskState.RUNNING
            self._run()
            self._state = TaskState.FINISHED
        else:
            raise RuntimeError(f"Task '{self}' cannot run while it is in the {self._state.name} state.")

    @abstractmethod
    def _run(self, *args, **kwargs):
        pass

    def __lt__(self, other):
        return self.priority < other.priority

    def __le__(self, other):
        return self.priority <= other.priority

    def __eq__(self, other):
        return self.priority == other.priority

    def __ne__(self, other):
        return self.priority != other.priority

    def __gt__(self, other):
        return self.priority > other.priority

    def __ge__(self, other):
        return self.priority >= other.priority

    def __str__(self):
        return f"<'{self.__class__.__name__}' Task priority={self.priority.name}, state={self.state.name}>"

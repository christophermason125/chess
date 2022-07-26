import heapq
from collections.abc import Sequence

from chess.src.model.task import Task
from chess.src.model.taskstate import TaskState


class TaskQueue(Sequence):

    class TaskItem:
        def __init__(self, task, order):
            self.task = task
            self.order = order

        def __lt__(self, other):
            return (self.task, self.order) < (other.task, other.order)

        def __le__(self, other):
            return (self.task, self.order) <= (other.task, other.order)

        def __eq__(self, other):
            return (self.task, self.order) == (other.task, other.order)

        def __ne__(self, other):
            return (self.task, self.order) != (other.task, other.order)

        def __gt__(self, other):
            return (self.task, self.order) > (other.task, other.order)

        def __ge__(self, other):
            return (self.task, self.order) >= (other.task, other.order)

        def __str__(self):
            return str(self.task)

    def __init__(self):
        self._container = []
        self.backfill = None
        self.running = False

    def __len__(self):
        return self._container.__len__()

    def __getitem__(self, i):
        return self._container.__getitem__(i).task

    def schedule(self, task):
        if not isinstance(task, Task):
            raise TypeError(f"Cannot schedule '{task}' (it is not a Task).")

        if task.state != TaskState.READY:
            raise ValueError(f"Cannot schedule '{task}' in the '{task.state.name}' state.")

        if self.running:
            if self.backfill is None:
                self.backfill = TaskQueue()
            heapq.heappush(self.backfill._container, TaskQueue.TaskItem(task, len(self.backfill)))
        else:
            heapq.heappush(self._container, TaskQueue.TaskItem(task, len(self)))
        task.set_scheduled()

    def run(self, *args, **kwargs):
        self.running = True
        while self._container:
            task = heapq.heappop(self._container).task
            if task.state == TaskState.SCHEDULED:
                task.run(*args, **kwargs)
            if self.backfill is not None:
                task.backfill.run(*args, **kwargs)

        self.running = False






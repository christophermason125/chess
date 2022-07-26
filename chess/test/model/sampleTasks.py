from chess.src.model.priority import Priority
from chess.src.model.task import Task


class HighestA(Task):
    base_priority = Priority.HIGHEST

    def _run(self, *args, **kwargs):
        print(self)


class HighestB(Task):
    base_priority = Priority.HIGHEST

    def _run(self, *args, **kwargs):
        print(self)


class HighestC(Task):
    base_priority = Priority.HIGHEST

    def _run(self, *args, **kwargs):
        print(self)


class HighestA(Task):
    base_priority = Priority.HIGHEST

    def _run(self, *args, **kwargs):
        print(self)


class HighestB(Task):
    base_priority = Priority.HIGHEST

    def _run(self, *args, **kwargs):
        print(self)


class HighA(Task):
    base_priority = Priority.HIGH

    def _run(self, *args, **kwargs):
        print(self)


class HighB(Task):
    base_priority = Priority.HIGH

    def _run(self, *args, **kwargs):
        print(self)


class HighC(Task):
    base_priority = Priority.HIGH

    def _run(self, *args, **kwargs):
        print(self)


class MediumA(Task):
    base_priority = Priority.MEDIUM

    def _run(self, *args, **kwargs):
        print(self)


class MediumB(Task):
    base_priority = Priority.MEDIUM

    def _run(self, *args, **kwargs):
        print(self)


class MediumC(Task):
    base_priority = Priority.MEDIUM

    def _run(self, *args, **kwargs):
        print(self)


class LowA(Task):
    base_priority = Priority.LOW

    def _run(self, *args, **kwargs):
        print(self)


class LowB(Task):
    base_priority = Priority.LOW

    def _run(self, *args, **kwargs):
        print(self)


class LowC(Task):
    base_priority = Priority.LOW

    def _run(self, *args, **kwargs):
        print(self)


class LowestA(Task):
    base_priority = Priority.LOWEST

    def _run(self, *args, **kwargs):
        print(self)


class LowestB(Task):
    base_priority = Priority.LOWEST

    def _run(self, *args, **kwargs):
        print(self)


class LowestC(Task):
    base_priority = Priority.LOWEST

    def _run(self, *args, **kwargs):
        print(self)

from chess.src.model.taskstate import TaskState
from chess.test.model.sampleTasks import *

t = HighestA()

assert t.priority == Priority.HIGHEST
assert t.state == TaskState.READY

t.cancel()

assert t.state == TaskState.CANCELED
t.priority = Priority.MEDIUM
assert t.priority == Priority.MEDIUM

try:
    t.run()
    raise AssertionError
except RuntimeError:
    pass

t = LowB()
t.set_scheduled()
try:
    t.priority = Priority.HIGHEST
    raise AssertionError
except ValueError:
    pass

assert LowA() > HighA()
assert MediumB() == MediumB()
assert MediumC() < LowestB()
assert LowestC() >= LowestA()
assert HighestC() <= HighestB()
assert HighestA() != HighB()

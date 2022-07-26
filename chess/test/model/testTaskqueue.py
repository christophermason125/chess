from chess.src.model.taskqueue import TaskQueue
from chess.test.model.sampleTasks import *

tq = TaskQueue()

tq.schedule(MediumA())
tq.schedule(HighestA())
tq.schedule(HighestB())
tq.schedule(LowC())
tq.schedule(HighC())
tq.schedule(MediumB())
tq.schedule(LowestC())
tq.schedule(HighestC())
tq.schedule(MediumC())
tq.schedule(LowA())
tq.schedule(LowestB())
tq.schedule(HighA())
tq.schedule(LowestA())
tq.schedule(LowB())
tq.schedule(HighB())

tq.run()

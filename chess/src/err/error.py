from typing import NewType

GameEndInterrupt = NewType("GameEndInterrupt", StopIteration)
ActionPerformedInterrupt = NewType("ActionPerformedInterrupt", StopIteration)

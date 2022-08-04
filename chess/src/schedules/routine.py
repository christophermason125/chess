from typing import Any, Optional

from chess.src.game import game as g


class Routine(list):
    def __init__(self, __game: g.Game, /, *tasks):
        self.game = __game
        super().__init__(tasks)

    def __call__(self, __result: Optional[Any] = None, /, *args: Any, **kwargs: Any) -> Any:
        for task in self:
            try:
                __result = task(__result, *args, **kwargs)
            except StopIteration as error:
                return error
        self(__result, *args, **kwargs)


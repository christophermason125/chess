from abc import ABC, abstractmethod
from typing import Any

from chess.src.game import game as g
from chess.src.game.player.player import Player


class Schedule(list, ABC):
    @abstractmethod
    def __init__(self, __game: g.Game, /, *tasks):
        self.game = __game
        super().__init__(tasks)

    def __call__(self, __result: Any, /, *args, **kwargs):
        result = None
        for task in self:
            result = task(result, *args, **kwargs)
        return result

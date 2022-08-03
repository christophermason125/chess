from chess.src.game.game import Game
from chess.src.game.player import player as p
from abc import ABC, abstractmethod


class Action(ABC):
    def __init__(self, game: Game, player: p.Player) -> None:
        self.game = game
        self.player = player

    def __call__(self, *args, **kwargs):
        self.validate(*args, **kwargs)
        self.run(*args, **kwargs)

    @abstractmethod
    def validate(self, *args, **kwargs):
        pass

    @abstractmethod
    def run(self, *args, **kwargs):
        pass

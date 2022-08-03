from chess.src.game import game as g
from chess.src.game.player.player import Player


class Schedule(list):
    order = tuple()

    def __init__(self, game: g.Game):
        self.game = game
        super().__init__(self.order)

    def __call__(self, __player: Player, /, *args, **kwargs):
        for task in self:
            result = task(__player, *args, **kwargs)
            if result:
                return result


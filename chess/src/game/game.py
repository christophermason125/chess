from chess.src.game.domain.bag import Bag
from chess.src.game.domain.board import Board
from chess.src.game.domain.domain import Domain
from chess.src.game.player.player import Player


class Game:
    def __init__(self, domains: set[Domain], players: set[Player]) -> None:

        self.players = players

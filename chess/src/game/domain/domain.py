from abc import ABC
from typing import Optional

from chess.src.game.domain.location import location as loc
from chess.src.game.player.player import Player


class Domain(ABC):
    def __init__(self, players: list[Player], locations: Optional[list[loc.Location]] = None) -> None:
        if locations is None:
            locations = []
        self.players = players
        self.locations = locations

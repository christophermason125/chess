from abc import ABC
from typing import Optional

from chess.src.game.color.color import Color
from chess.src.game.domain.location import location as loc


class Piece(ABC):
    def __init__(self, color: Color, location: Optional[loc.Location] = None) -> None:
        self.color = color
        self.location = location

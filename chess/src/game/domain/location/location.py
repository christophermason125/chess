from typing import Optional

from chess.src.game.color.color import Color
from chess.src.game.piece import piece as p
from chess.src.game.domain import domain as d


class Location:
    def __init__(self, __color: Color,
                 __domain: d.Domain,
                 __contents: Optional[p.Piece] = None,
                 /,
                 **coordinates: [int]) -> None:
        self.__dict__.update(coordinates)
        self.contents = __contents
        self.color = __color

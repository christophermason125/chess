from chess.src.game.domain.domain import Domain
from chess.src.game.domain.location.location import Location


class Board(Domain):
    def __contains__(self, item: Location) -> bool:
        for rank in self.locations:
            if item in rank:
                return True
        return False

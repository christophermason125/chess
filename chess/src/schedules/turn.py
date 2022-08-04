from typing import Any, Optional

from chess.src.schedules.routine import Routine
from chess.src.game import game as g


class Turn(Routine):
    def __init__(self, game: g.Game):
        super().__init__(
            game,
            self.resolve_resigned_player,
            self.resolve_claimed_draw,
            self.resolve_dead_position,
            self.resolve_repeated_position_limit,
            self.resolve_passive_move_limit,
            self.resolve_all_valid_moves,
            self.resolve_in_check,
            self.resolve_checkmate,
            self.resolve_stalemate
        )

    def resolve_resigned_player(self, __result: Optional[Any] = None, /, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_claimed_draw(self, __result: Optional[Any] = None, /, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_all_valid_moves(self, __result: Optional[Any] = None, /, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_in_check(self, __result: Optional[Any] = None, /, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_dead_position(self, __result: Optional[Any] = None, /, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_repeated_position_limit(self, __result: Optional[Any] = None, /, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_passive_move_limit(self, __result: Optional[Any] = None, /, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_checkmate(self, __result: Optional[Any] = None, /, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_stalemate(self, __result: Any, *args: Any, **kwargs: Any) -> Any:
        pass
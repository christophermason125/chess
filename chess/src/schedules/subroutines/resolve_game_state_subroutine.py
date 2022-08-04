from typing import Any

from chess.src.schedules.schedule import Schedule
from chess.src.game import game as g
from chess.src.schedules.subroutines.force_draw_subroutine import ForceDrawSubroutine


class ResolveGameStateSubroutine(Schedule):
    def __init__(self, game: g.Game):
        super().__init__(
            game,
            self.resolve_resigned_player,
            self.resolve_claimed_draw,
            ForceDrawSubroutine(game),
            self.resolve_all_valid_moves,
            self.resolve_in_check,
        )

    def resolve_resigned_player(self, __result: Any, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_claimed_draw(self, __result: Any, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_all_valid_moves(self, __result: Any, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_in_check(self, __result: Any, *args: Any, **kwargs: Any) -> Any:
        pass


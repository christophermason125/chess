from typing import Any

from chess.src.schedules.schedule import Schedule
from chess.src.game import game as g


class ForceDrawSubroutine(Schedule):
    def __init__(self, game: g.Game):
        super().__init__(
            game,
            self.resolve_insufficient_material,
            self.resolve_repeated_position_limit,
            self.resolve_move_limit
        )

    def resolve_insufficient_material(self, __result: Any, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_repeated_position_limit(self, __result: Any, *args: Any, **kwargs: Any) -> Any:
        pass

    def resolve_move_limit(self, __result: Any, *args: Any, **kwargs: Any) -> Any:
        pass

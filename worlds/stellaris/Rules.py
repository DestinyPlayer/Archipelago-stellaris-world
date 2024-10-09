from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import StellarisWorld


def set_rules(world: "StellarisWorld"):
    player = world.player
    multiworld = world.multiworld
    options = world.options
    # Win Condition
    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
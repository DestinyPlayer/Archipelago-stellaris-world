from dataclasses import dataclass
from Options import Choice, Range, Toggle, PerGameCommonOptions, StartInventoryPool, OptionGroup, OptionSet
from .dlc.dlc_data import DlcNames


class ResearchHardMode(Toggle):
    """Progressive Tech Items won't give you the research for free, only add them to your research pool"""
    display_name = "Research Hard Mode"

class ResearchExtraSlots(Range):
    """How many extra research slots should there be?"""
    display_name = "Extra Research Slots"
    range_start = 0
    range_end = 1000
    default = 5

class DLCIncluded(OptionSet):
    """What DLC you have/intend to use"""
    display_name = "What DLC you have"
    valid_keys = {
        DlcNames.leviathans,
        DlcNames.utopia,
        DlcNames.megacorp,
        DlcNames.apocalypse,
        DlcNames.federations,
        DlcNames.nemesis,
        DlcNames.overlord,
        DlcNames.galacticParagons,
        DlcNames.astralPlanes,
        DlcNames.cosmicStorms,
        DlcNames.machineAge,
        DlcNames.syntheticDawn,
        DlcNames.distantStars,
        DlcNames.ancientRelics,
        DlcNames.firstContact,
        DlcNames.humanoidsSpecies,
        DlcNames.plantoidsSpecies,
        DlcNames.lithoidsSpecies,
        DlcNames.necroidsSpecies,
        DlcNames.aquaticsSpecies,
        DlcNames.toxoidsSpecies
                  }

stellarisOptionGroups = [
    OptionGroup("Research Options", [
        ResearchExtraSlots,
        ResearchHardMode
    ], start_collapsed=False),
    OptionGroup("Other Options",[
        DLCIncluded
    ])
]

@dataclass
class StellarisOptions(PerGameCommonOptions):
    researchHardMode: ResearchHardMode
    researchExtraSlots: ResearchExtraSlots
    dlcIncluded: DLCIncluded
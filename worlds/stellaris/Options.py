from dataclasses import dataclass
from Options import Choice, Range, Toggle, PerGameCommonOptions, StartInventoryPool


class ResearchHardMode(Toggle):
    """Progressive Tech Items won't give you the research for free, only add them to your research pool"""
    display_name = "Research Hard Mode"

class ResearchExtraSlots(Range):
    """How many extra research slots should there be?"""
    display_name = "Extra Research Slots"
    range_start = 0
    range_end = 1000
    default = 5

@dataclass
class StellarisOptions(PerGameCommonOptions):
    researchHardMode: ResearchHardMode
    researchExtraSlots: ResearchExtraSlots
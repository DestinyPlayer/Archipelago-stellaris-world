from typing import Callable, NamedTuple, Optional, TYPE_CHECKING, Dict
from . import Utility, Options
from BaseClasses import Location

if TYPE_CHECKING:
    from . import StellarisWorld

class StellarisLocation(Location):
    game = "Stellaris"

class StellarisLocationData(NamedTuple):
    region:      str
    address:     Optional[int]                      = None
    can_create:  Callable[["StellarisWorld"], bool] = lambda world: True
    locked_item: Optional[str]                      = None

def getLocationDataTable(count,world: "StellarisWorld"):
    """This function generates location slots based on all potential items in Stellaris + an option offset"""
    location_data_table: Dict[str, StellarisLocationData] = {}
    for i in range(count+world.options.researchExtraSlots):
        region  = "Research"
        address = 750000 + i
        location_data_table["Research " + str(i)] = StellarisLocationData(
            region  = region,
            address = address
        )
    return location_data_table

def getLocationTable(count):
    """This function generates a list of location slots used for generating Location IDs.
    It utilizes the absolute largest number of slots possible for the world"""
    location_table = {}
    for i in range(count+Options.ResearchExtraSlots.range_end):
        name = "Research " + str(i)
        code = 75000 + i
        location_table[name] = code
    return location_table

researchCount = Utility.getTotalResearchCount()

locationTable = getLocationTable(researchCount)
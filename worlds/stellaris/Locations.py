from typing import Callable, NamedTuple, Optional, TYPE_CHECKING, Dict
from . import Utility, Options
from BaseClasses import Location

if TYPE_CHECKING:
    from . import StellarisWorld

class StellarisLocation(Location):
    game = "Stellaris"

class StellarisLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["StellarisWorld"], bool] = lambda world: True
    locked_item: Optional[str] = None

def getLocationDataTable(count,world: "StellarisWorld"):
    location_data_table: Dict[str, StellarisLocationData] = {}
    for i in range(count+world.options.researchExtraSlots):
        location_data_table["Research " + str(i)] = StellarisLocationData(
            region="Research",
            address=750000 + i
        )
    return location_data_table

def getLocationTable(count):
    location_table = {}
    for i in range(count+1000):
        location_table["Research " + str(i)] = 75000 + i
    return location_table

researchCount = Utility.getTotalResearchCount()

locationTable = getLocationTable(researchCount)
from typing import Callable, NamedTuple, Optional, TYPE_CHECKING, Dict
from . import DataTech
from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from . import StellarisWorld

class StellarisItem(Item):
    game = "Stellaris"


class StellarisItemData(NamedTuple):
    code: Optional[int] = None
    type: ItemClassification = ItemClassification.filler
    can_create: Callable[["StellarisWorld"], bool] = lambda world: True
    gameType: str = ""

def getItemDataTable():
    item_data_table: Dict[str, StellarisItemData] = {}
    for key, tech in enumerate(DataTech.techs):
        for i in range(tech["levels"]):
            if tech["progType"] == "progression":
                progType = ItemClassification.progression
            if tech["progType"] == "filler":
                progType = ItemClassification.useful
            else:
                progType = ItemClassification.filler
            item_data_table["tech_progressive_"+tech["name"]+"_"+str(i+1)] = StellarisItemData(
                code=7500000000+(key+1),
                type=progType
            )
    return item_data_table

def getItemTable():
    item_table = {}
    for key, tech in enumerate(DataTech.techs):
        for i in range(tech["levels"]):
            item_table["tech_progressive_"+tech["name"]+"_"+str(i+1)] = 7500000000+(key+1)
    return item_table

itemDataTable: Dict[str, StellarisItemData] = getItemDataTable()
itemTable = getItemTable()
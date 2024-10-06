from BaseClasses import Tutorial, Item, ItemClassification
from worlds.AutoWorld import WebWorld, World


class StellarisWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Factorio software on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["DestinyPlayer"]
    )]

class StellarisWorld(World):
    """
    Stellaris is a Grand Strategy game about leading an empire to galactic domination.
    Explore the secrets of the massive, ancient galaxy, Expand your territory, Exploit both resources and your neighbors
    and, if they prove to be too much of an issue, Exterminate them until all that's left is you.
    """
    game = "Stellaris"
    web = StellarisWeb()
    item_name_to_id = {
        "Test": 75000
    }
    location_name_to_id = {
        "Nowhere": 76000
    }

    def create_item(self, name: str) -> Item:
        if name == "Test":
            return Item(name, ItemClassification.filler, -1, self.player)
        raise KeyError(name)
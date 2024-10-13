import time
from typing import List, Dict, Mapping, Any
from BaseClasses import Tutorial, Item, ItemClassification, Region
from Utils import local_path
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, components, Type, launch_subprocess, icon_paths
from . import Regions, DataTech, Generate, Rules
from .Items import StellarisItemData, itemDataTable, itemTable, StellarisItem
from .Locations import StellarisLocationData,researchCount, getLocationDataTable, StellarisLocation
from .Options import StellarisOptions, stellarisOptionGroups
from .DataEvent import finalLocations, finalTechItemsInternal, finalTechItemsExternal

#########################################################################################
#          _______ _______ _______               _______  ______ _____ _______          #
#          |______    |    |______ |      |      |_____| |_____/   |   |______          #
#          ______|    |    |______ |_____ |_____ |     | |    \_ __|__ ______|          #
#########################################################################################

def launch_client():
    from worlds.stellaris.Client import runStellarisClient
    launch_subprocess(runStellarisClient, name="StellarisClient")


components.append(Component(
    "Stellaris Client",
    "StellarisClient",
    func           = launch_client,
    component_type = Type.CLIENT,
    icon           = 'sticon'
))


icon_paths['sticon'] = local_path('data', 'sticon.png')

class StellarisWeb(WebWorld):
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Factorio software on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["DestinyPlayer"]
    )]
    option_groups = stellarisOptionGroups

class StellarisWorld(World):
    """
    Stellaris is a Grand Strategy game about leading an empire to galactic domination.
    Explore the secrets of the massive, ancient galaxy, Expand your territory, Exploit both resources and your neighbors
    and, if they prove to be too much of an issue, Exterminate them until all that's left is you.
    """
    game                = "Stellaris"
    web                 = StellarisWeb()
    options             = StellarisOptions
    options_dataclass   = StellarisOptions
    item_name_to_id     = Items.itemTable
    location_name_to_id = Locations.locationTable

    '''def set_rules(self) -> None:
        Rules.set_rules(self)'''

    def create_regions(self) -> None:
        # Create regions.
        for region_name in Regions.region_data_table.keys():
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        # Create locations.
        locationDataTable: Dict[str, StellarisLocationData] = getLocationDataTable(researchCount, self)

        for region_name, region_data in Regions.region_data_table.items():
            region = self.get_region(region_name)
            region.add_locations({
                location_name: location_data.address for location_name, location_data in locationDataTable.items()
                if location_data.region == region_name and location_data.can_create(self)
            }, StellarisLocation)
            region.add_exits(Regions.region_data_table[region_name].connecting_regions)

    def create_item(self, name: str) -> StellarisItem:
        return StellarisItem(name, itemDataTable[name].type, itemDataTable[name].code, self.player)

    def create_items(self) -> None:
        item_pool: List[StellarisItem] = []

        for name, item in itemDataTable.items():
            if item.code and item.can_create(self):
                item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool

        # Set priority location for the Big Red Button!
        self.options.priority_locations.value.add("Research")

    def generate_output(self, output_directory: str) -> None:
        print("o---------------------------------------------[Stellaris]---------------------------------------------o")
        DataEvent.finalLocations = self.multiworld.get_filled_locations(self.player)

        for location in DataEvent.finalLocations:
            if "Research" in str(location):
                if self.player == location.item.player:
                    DataEvent.finalTechItemsInternal.append([
                        location.item,
                        location.address,
                        location.item.player,
                        self.player_name
                    ])
                else:
                    DataEvent.finalTechItemsExternal.append([
                        location.item,
                        location.address,
                        location.item.player,
                        ""
                    ])

        self.create_mod(output_directory)
        self.cleanUpGeneration()
        print("o---------------------------------------------[Stellaris]---------------------------------------------o")
        input("Press any key to finalize") #This is for debug, remove later

    def cleanUpGeneration(self):
        """This method cleans saved multiworld data to prevent memory leaks"""
        DataEvent.finalTechItemsExternal.clear()
        DataEvent.finalTechItemsInternal.clear()
        DataEvent.finalLocations.clear()
        print("|Stellaris: Cleaned up Multiworld object allocations                                                  |")

    '''def checkTechPresence(self,item: str):
        """This function checks for if the item in a location slot is a Stellaris item"""
        for tech in DataTech.techs:
            techFull = "tech_progressive_"+tech["name"]
            if techFull in item:
                print("Item ",item," is this mod's item!")
                return True'''

    def create_mod(self, outputDirectory) -> None:
        """This method generates the Stellaris mod"""
        Generate.generateMod(self,outputDirectory)
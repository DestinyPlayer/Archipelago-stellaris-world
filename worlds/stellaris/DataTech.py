from typing import TYPE_CHECKING
from .dlc.dlc_data import DlcNames

if TYPE_CHECKING:
    from . import StellarisWorld

techs = [
    {"name":"reactor", "levels":5, "area":"physics","category":"particles", "tier":1, "non_research": "",
     "progType": "progression"},
    {"name":"hyperdrive", "levels":4, "area":"physics", "category":"particles", "tier":1, "non_research": "",
     "progType": "progression"},
    {"name":"thruster", "levels":4, "area":"engineering", "category":"propulsion", "tier":1, "non_research": "",
     "progType": "progression"},
    {"name":"ship", "levels":5, "area":"engineering", "category":"voidcraft", "tier":1, "non_research": "",
     "progType": "progression"},
    {"name":"starbase", "levels":3, "area":"engineering", "category":"voidcraft", "tier":1, "non_research": "",
     "progType": "progression"},
    {"name":"wormhole", "levels":2, "area":"physics", "category":"particles", "tier":2, "non_research": "",
     "progType": "progression"},
    {"name": "corvette_upgrades", "levels": 3, "area": "engineering", "category": "voidcraft", "tier": 2, "non_research": "",
     "progType": "filler"},
    {"name": "destroyer_upgrades", "levels": 3, "area": "engineering", "category": "voidcraft", "tier": 2, "non_research": "",
     "progType": "filler"},
    {"name": "cruiser_upgrades", "levels": 3, "area": "engineering", "category": "voidcraft", "tier": 2, "non_research": "",
     "progType": "filler"},
    {"name": "battleship_upgrades", "levels": 3, "area": "engineering", "category": "voidcraft", "tier": 2, "non_research": "",
     "progType": "filler"},
    {"name": "titan_upgrades", "levels": 2, "area": "engineering", "category": "voidcraft", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "starbase_upgrades", "levels": 2, "area": "engineering", "category": "voidcraft", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "strike_craft", "levels": 4, "area": "engineering", "category": "voidcraft", "tier": 1, "non_research": "",
     "progType": "useful"},
    {"name": "orbital_habitats", "levels": 3, "area": "engineering", "category": "voidcraft", "tier": 2, "non_research": "",
     "progType": "progression"},
    {"name": "ship_armor", "levels": 4, "area": "engineering", "category": "materials", "tier": 1, "non_research": "",
     "progType": "progression"},
    {"name": "armor_hardener", "levels": 2, "area": "engineering", "category": "materials", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "robotics", "levels": 5, "area": "engineering", "category": "industry", "tier": 1, "non_research": "",
     "progType": "progression"},
    {"name": "space_mining", "levels": 5, "area": "engineering", "category": "industry", "tier": 1, "non_research": "",
     "progType": "useful"},
    {"name": "planetary_mining", "levels": 3, "area": "engineering", "category": "industry", "tier": 2, "non_research": "",
     "progType": "progression"},
    {"name": "alloy_production", "levels": 2, "area": "engineering", "category": "materials", "tier": 3, "non_research": "",
     "progType": "progression"},
    {"name": "consumer_goods", "levels": 2, "area": "engineering", "category": "materials", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "afterburners", "levels": 2, "area": "engineering", "category": "propulsion", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "planetary_build_speed", "levels": 2, "area": "engineering", "category": "industry", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "housing", "levels": 3, "area": "engineering", "category": "industry", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "mass_drivers", "levels": 4, "area": "engineering", "category": "propulsion", "tier": 1, "non_research": "",
     "progType": "progression"},
    {"name": "kinetic_artillery", "levels": 2, "area": "engineering", "category": "propulsion", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "mass_accelerators", "levels": 2, "area": "engineering", "category": "propulsion", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "autocannon", "levels": 4, "area": "engineering", "category": "propulsion", "tier": 1, "non_research": "",
     "progType": "useful"},
    {"name": "flak_battery", "levels": 3, "area": "engineering", "category": "propulsion", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "missiles", "levels": 4, "area": "engineering", "category": "propulsion", "tier": 1, "non_research": "",
     "progType": "progression"},
    {"name": "swarm_missiles", "levels": 2, "area": "engineering", "category": "propulsion", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "torpedoes", "levels": 3, "area": "engineering", "category": "propulsion", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "shields", "levels": 5, "area": "physics", "category": "field_manipulation", "tier": 1, "non_research": "",
     "progType": "progression"},
    {"name": "science_lab", "levels": 3, "area": "physics", "category": "computing", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "station_science", "levels": 5, "area": "physics", "category": "computing", "tier": 1, "non_research": "",
     "progType": "filler"},
    {"name": "colony_ship", "levels": 2, "area": "physics", "category": "computing", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "research_ai", "levels": 3, "area": "physics", "category": "computing", "tier": 2, "non_research": "",
     "progType": "progression"},
    {"name": "encryption", "levels": 3, "area": "physics", "category": "computing", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "decryption", "levels": 3, "area": "physics", "category": "computing", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "reactor_booster", "levels": 2, "area": "physics", "category": "particles", "tier": 2, "non_research": "",
     "progType": "filler"},
    {"name": "shield_hardener", "levels": 2, "area": "physics", "category": "field_manipulation", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "sensors", "levels": 3, "area": "physics", "category": "computing", "tier": 2, "non_research": "",
     "progType": "progression"},
    {"name": "power_plants", "levels": 3, "area": "physics", "category": "field_manipulation", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "lasers", "levels": 4, "area": "physics", "category": "particles", "tier": 1, "non_research": "",
     "progType": "progression"},
    {"name": "lances", "levels": 2, "area": "physics", "category": "particles", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "plasma", "levels": 3, "area": "physics", "category": "particles", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "arc_emitter", "levels": 2, "area": "physics", "category": "particles", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "disruptors", "levels": 3, "area": "physics", "category": "particles", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "energy_torpedoes", "levels": 2, "area": "physics", "category": "particles", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "point_defense", "levels": 2, "area": "physics", "category": "computing", "tier": 3, "non_research": "",
     "progType": "progression"},
    {"name": "trade", "levels": 3, "area": "society", "category": "statecraft", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "farming", "levels": 4, "area": "society", "category": "biology", "tier": 1, "non_research": "",
     "progType": "progression"},
    {"name": "habitability", "levels": 4, "area": "society", "category": "new_worlds", "tier": 1, "non_research": "",
     "progType": "filler"},
    {"name": "hospital", "levels": 2, "area": "society", "category": "biology", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "terraforming", "levels": 3, "area": "society", "category": "new_worlds", "tier": 2, "non_research": "",
     "progType": "useful"},
    {"name": "leader_genetics", "levels": 3, "area": "society", "category": "biology", "tier": 2, "non_research": "",
     "progType": "filler"},
    {"name": "gene_tailoring", "levels": 6, "area": "society", "category": "biology", "tier": 1, "non_research": "",
     "progType": "useful"},
    {"name": "army_genetics", "levels": 3, "area": "society", "category": "biology", "tier": 2, "non_research": "",
     "progType": "filler"},
    {"name": "fleet_size", "levels": 5, "area": "society", "category": "military_theory", "tier": 1, "non_research": "",
     "progType": "useful"},
    {"name": "naval_capacity", "levels": 4, "area": "society", "category": "military_theory", "tier": 1, "non_research": "",
     "progType": "useful"},
    {"name": "army_defense", "levels": 2, "area": "society", "category": "military_theory", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "army_offense", "levels": 2, "area": "society", "category": "military_theory", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "psionics", "levels": 3, "area": "society", "category": "psionics", "tier": 2, "non_research": "",
     "progType": "progression"},
    {"name": "starbase_capacity", "levels": 2, "area": "society", "category": "new_worlds", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "campaigns", "levels": 2, "area": "society", "category": "military_theory", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "planet_government", "levels": 3, "area": "society", "category": "statecraft", "tier": 2, "non_research": "",
     "progType": "progression"},
    {"name": "planet_infrastructure", "levels": 2, "area": "society", "category": "new_worlds", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "bureaucracy", "levels": 4, "area": "society", "category": "statecraft", "tier": 1, "non_research": "",
     "progType": "filler"},
    {"name": "thralls", "levels": 2, "area": "society", "category": "statecraft", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "psionic_shield", "levels": 2, "area": "society", "category": "psionics", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "embassy", "levels": 2, "area": "society", "category": "statecraft", "tier": 3, "non_research": "",
     "progType": "useful"},
    {"name": "capital_production", "levels": 3, "area": "society", "category": "statecraft", "tier": 2, "non_research": "",
     "progType": "filler"},
    {"name": "bioreactor", "levels": 2, "area": "society", "category": "biology", "tier": 3, "non_research": "",
     "progType": "filler"},
    {"name": "hull_regen", "levels": 1, "area": "society", "category": "biology", "tier": 4, "non_research": "",
     "progType": "filler"},
    {"name": "megastructures", "levels": 2, "area": "engineering", "category": "voidcraft", "tier": 3, "non_research": "",
     "progType": "progression"}
]

leviathansTechs = [

]

horizonSignalTech = [

]

utopiaTechs = [

]

megacorpTechs = [

]

apocalypseTechs = [

]

federationsTechs = [

]

nemesisTechs = [

]

overlordTechs = [

]

galacticParagonsTechs = [

]

astralPlanesTechs = [

]

cosmicStormsTechs = [

]

syntheticDawnTechs = [

]

distantStarsTechs = [

]

ancientRelicsTechs = [

]

firstContactTechs = [

]

"""def addDlcTechs(world: "StellarisWorld"):
    for dlc in world.options.dlcIncluded.value:
        print(dlc)
        if dlc == DlcNames.leviathans:
            print("Detected ",dlc," DLC")
        elif dlc == DlcNames.utopia:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.megacorp:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.apocalypse:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.federations:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.nemesis:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.overlord:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.galacticParagons:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.astralPlanes:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.cosmicStorms:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.machineAge:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.syntheticDawn:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.distantStars:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.ancientRelics:
            print("Detected ", dlc, " DLC")
        elif dlc == DlcNames.firstContact:
            print("Detected ", dlc, " DLC")"""
#Areas:
#   physics, society, engineering

#Categories:
#   Physics:
#       field_manipulation, particles, computing
#   Society:
#       psionics, new_worlds, statecraft, biology, military_theory
#   Engineering:
#       materials, rocketry, voidcraft, industry

########################################################################################################################
'''import DataTechVanilla

def QuickGenerateTechs():
    """SHOULD ONLY BE UNCOMMENTED IF IN USE

    This method generates a list of technology dictionaries based on DataTechVanilla.py"""
    techsOut   = "techs = ["
    techBase   = '{{"name":"{name}", "levels":{levels}, "area":None, "category":None, "tier":{tier}, "non_research": "",\n     "progType": None}}'
    eventsOut  = "items = ["
    eventsBase = '{{"type":"tech", "name":"{name}", "description":"Progressive {name2} technology"}}'

    for tech in DataTechVanilla.vanillaTechs:
        try:
            tech.split()[1]
        except:
            print("SHOULD ONLY BE UNCOMMENTED IF IN USE")
        else:
            continue

        if "repeatable" in tech or "miscellaneous" in tech or tech == "event":
            continue

        levels = len(DataTechVanilla.vanillaTechs[tech])

        if levels >= 5:
            tier = 1
        else:
            tier = 5 - levels

        techsOut  += "\n    "
        techsOut  += techBase.format(name = tech, levels = levels, tier = tier)
        techsOut  += ","
        eventsOut += "\n    "
        eventsOut += eventsBase.format(name=tech, name2=tech.replace("_"," "))
        eventsOut += ","

    techsOut  += "\n]"
    eventsOut += "\n]"

    f = open("DataTechTest.py", "w")
    f.write(techsOut)
    f.write("\n")
    f.write(eventsOut)
    f.close()

QuickGenerateTechs()'''
########################################################################################################################
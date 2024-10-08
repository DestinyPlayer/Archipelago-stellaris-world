techs = [
    {"name":"reactor", "levels":5, "area":"physics","category":"particles", "tier":1, "non_research": "13",
     "progType": "progression"},
    {"name":"hyperdrive", "levels":4, "area":"physics", "category":"particles", "tier":1, "non_research": "13",
     "progType": "progression"},
    {"name":"thruster", "levels":4, "area":"engineering", "category":"rocketry", "tier":1, "non_research": "13",
     "progType": "progression"},
    {"name":"ship", "levels":5, "area":"engineering", "category":"voidcraft", "tier":1, "non_research": "13",
     "progType": "progression"},
    {"name":"starbase", "levels":3, "area":"engineering", "category":"voidcraft", "tier":1, "non_research": "13",
     "progType": "progression"},
    {"name":"wormhole", "levels":2, "area":"physics", "category":"particles", "tier":2, "non_research": "2",
     "progType": "progression"},
    {"name":"repeatable_engineering", "levels":6, "area":"physics", "category":"particles", "tier":2, "non_research": "2",
     "progType": "filler"}
]

#Areas:
#   physics, society, engineering

#Categories:
#   Physics:
#       field_manipulation, particles, computing
#   Society:
#       psionics, new_worlds, statecraft, biology, military_theory
#   Engineering:
#       materials, rocketry, voidcraft, industry

#Cost:
#If set to 0 it is set to unavailable

import DataTechVanilla

def QuickGenerateTechs():
    techsOut = "techs = ["
    techBase = '{{"name":"{name}", "levels":{levels}, "area":None, "category":None, "tier":{tier}, "non_research": None,\n     "progType": None}}'
    eventsOut = "items = ["
    eventsBase = '{{"type":"tech", "name":"{name}", "description":"Progressive {name2} technology"}}'
    for tech in DataTechVanilla.vanillaTechs:
        try:
            tech.split()[1]
        except:
            1
        else:
            continue
        if "repeatable" in tech or tech == "event":
            continue
        levels = len(DataTechVanilla.vanillaTechs[tech])
        if levels >= 5:
            tier = 1
        else:
            tier = 5 - levels
        techsOut = techsOut + "\n    "
        techsOut = techsOut + techBase.format(name = tech, levels = levels, tier = tier)
        techsOut = techsOut + ","
        eventsOut = eventsOut + "\n    "
        eventsOut = eventsOut + eventsBase.format(name=tech, name2=tech.replace("_"," "))
        eventsOut = eventsOut + ","
    techsOut = techsOut + "\n]"
    eventsOut = eventsOut + "\n]"
    f = open("DataTechTest.py", "w")
    f.write(techsOut)
    f.write("\n")
    f.write(eventsOut)
    f.close()

QuickGenerateTechs()
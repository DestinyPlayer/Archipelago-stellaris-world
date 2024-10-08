from worlds.stellaris.Utility import writeToFile

techs = [
    {"name":"reactor", "levels":5, "area":"physics","category":"particles", "tier":1, "non_research": "13"},
    {"name":"hyperdrive", "levels":4, "area":"physics", "category":"particles", "tier":1, "non_research": "13"},
    {"name":"thruster", "levels":4, "area":"engineering", "category":"rocketry", "tier":1, "non_research": "13"},
    {"name":"ship", "levels":5, "area":"engineering", "category":"voidcraft", "tier":1, "non_research": "13"},
    {"name":"starbase", "levels":3, "area":"engineering", "category":"voidcraft", "tier":1, "non_research": "13"},
    {"name":"wormhole", "levels":2, "area":"physics", "category":"particles", "tier":2, "non_research": "2"}
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

'''import DataTechVanilla

def QuickGenerateTechs():
    techsOut = "techs = ["
    techBase = '{{"name":"{name}", "levels":{levels}, "area":None, "category":None, "tier":{tier}, "non_research": None}}'
    for tech in DataTechVanilla.vanillaTechs:
        levels = len(DataTechVanilla.vanillaTechs[tech])
        if levels == 5:
            tier = 1
        else:
            tier = 5 - levels
        techsOut = techsOut + "\n    "
        techsOut = techsOut + techBase.format(name = tech, levels = levels, tier = tier)
        techsOut = techsOut + ","
    techsOut = techsOut + "\n]"
    f = open("DataTechTest.py", "w")
    f.write(techsOut)
    f.close()

QuickGenerateTechs()'''
from random import randrange
import shutil
from . import DataTech
from .CreateEvents import findTech
from .DataEvent import unScrewTechData, finalTechItemsInternal, finalTechItemsExternal, smoothTechData
from .templates.TemplateTech import techStart, techTemplate, techProgCost, weightNull
from .templates.TemplateLocalisation import localisationStart, localisationTechTemplate, localisationExternalTechTemplate
from .Utility import writeToFile, languages
import time


randomTechArea                = ["physics","society","engineering"]
randomTechPhysicsCategory     = ["field_manipulation", "particles", "computing"]
randomTechSocietyCategory     = ["psionics", "new_worlds", "statecraft", "biology", "military_theory"]
randomTechEngineeringCategory = ["materials", "rocketry", "voidcraft", "industry"]


def countFinalTechs(tech):
    count = 0

    for item in finalTechItemsInternal:
        itemLoc = smoothTechData(item[0])
        if tech["name"] == itemLoc:
            count += 1

    return tech["levels"] - count


def createOutsideTech():
    techText = techStart

    for key,tech in enumerate(finalTechItemsExternal):
        type = "external_" + smoothTechData(tech[0])
        area = randomTechArea[randrange(0,2)]

        if area == "physics":
            category = randomTechPhysicsCategory[randrange(0,2)]
        elif area == "society":
            category = randomTechSocietyCategory[randrange(0,4)]
        else:
            category = randomTechEngineeringCategory[randrange(0,3)]

        tier        = randrange(1,5)
        cost        = techProgCost + str(randrange(1,5))
        weight_null = ""
        weight      = randrange(1,5)

        techText    = techText + techTemplate.format(
            type        = type,
            num         = tech[1] - 750000 + 20000,
            area        = area,
            category    = category,
            cost        = cost,
            weight      = weight,
            tier        = tier,
            weight_null = weight_null
        )

    for key,tech in enumerate(finalTechItemsInternal):
        name = str(tech[0]).split(" ")[0]
        lev = name[-1:]
        name = name[:-2]
        name = name.replace("tech_progressive_","")
        find = findTech(name)
        type = "internal_" + name + "_" + lev
        area = find["area"]
        category = find["category"]

        tier        = find["tier"] + int(lev)-1
        if tier > 5: tier = 5
        cost        = techProgCost + str(tier)
        weight_null = ""
        weight      = tier

        techText    = techText + techTemplate.format(
            type        = type,
            num         = tech[1] - 750000 + 20000,
            area        = area,
            category    = category,
            cost        = cost,
            weight      = weight,
            tier        = tier,
            weight_null = weight_null
        )

    techText += techTemplate.format(
        type = "fillTech",
        num  = "14151",
        area = "physics",
        category = "particles",
        cost = 10,
        weight = 0,
        tier = 1,
        weight_null = weightNull
        )

    writeToFile("common/technology/archipelago_external_tech.txt", techText)
    print("|Stellaris:     Finished generation of external research definition files                             |")

def createOutsideTechLocalisations():
    """This function assembles the technology localisation files in the mod (names and descriptions)"""
    for lang in languages:
        localisationText = localisationStart.format(lang=lang)

        for key,tech in enumerate(finalTechItemsExternal):
            type = smoothTechData(tech[0])
            name = tech[0]
            type = "external_" + type
            code = tech[1] - 750000 + 20000

            localisationText += localisationTechTemplate.format(
                type = type,
                num  = code,
                name = name,
                desc = name
            )

        writeToFile("localisation/" + lang + "/archipelago_external_techs_l_" + lang + ".yml", localisationText,
                    "utf-8-sig")
    print("|Stellaris:     Finished generation of external technology localisation files                         |")

def createTech():
    """This function assembles the technology definition files in the mod"""
    techText = techStart

    for tech in DataTech.techs:
        type     = "progressive_" + tech["name"]
        area     = tech["area"]
        tier     = tech["tier"]
        category = tech["category"]
        count    = countFinalTechs(tech)

        if count != 0:
            for i in range(count):
                tech["non_research"] += str(i + 1)

        for i in range(tech["levels"]): #Generate
            tierAdd = i + tier

            if tierAdd > 5:
                tierAdd = 5

            cost = techProgCost + str(tierAdd)
            weight = tierAdd
            weight_null = ""

            for item in finalTechItemsInternal:
                if True:
                    cost        = techProgCost+"0"
                    weight      = 0
                    weight_null = weightNull
                    break

            techText += techTemplate.format(
                type        = type,
                num         = i + 1,
                area        = area,
                category    = category,
                cost        = cost,
                weight      = weight,
                tier        = tierAdd,
                weight_null = weight_null
            )

    writeToFile("common/technology/archipelago_progressive_tech.txt",techText)
    print("|Stellaris:     Finished generation of technology definition files                                    |")


def createTechLocalisations():
    """This function assembles the technology localisation files in the mod (names and descriptions)"""
    for lang in languages:
        localisationText = localisationStart.format(lang = lang)

        for tech in DataTech.techs:
            type  = tech["name"]
            desc  = (type[0].upper() + type[1:]).replace("_"," ")
            name  = "Progressive " + desc
            type  = "progressive_" + type

            for i in range(tech["levels"]):
                localisationText += localisationTechTemplate.format(
                    type  = type,
                    num   = i + 1,
                    name  = name,
                    desc  = desc
                )

        for key, tech in enumerate(finalTechItemsExternal):
            type = "external_"+smoothTechData(tech[0])
            name = str(tech[0])
            localisationText +=localisationExternalTechTemplate.format(
                type = type,
                num  = key + 1,
                name = name
            )

        writeToFile("localisation/" + lang + "/archipelago_progressive_techs_l_" + lang + ".yml", localisationText,
                    "utf-8-sig")
    print("|Stellaris:     Finished generation of technology localisation files                                  |")

def createTechIcons():
    """This function assigns icons to technologies"""
    path         = "worlds/stellaris/mod/archipelago-stellaris-mod/gfx/interface/icons/technologies/"
    iconTempName = "tech_progressive"
    iconFinName  = "{type}_{num}"
    format       = ".dds"

    for tech in DataTech.techs:
        type = tech["name"]
        for i in range(tech["levels"]):
            iconFinal = iconTempName + "_" + iconFinName.format(
                type = type,
                num  = i + 1
            )
            iconFinal += format
            iconFinal  = path + iconFinal
            pathFinal  = path + iconTempName + format
            shutil.copyfile(pathFinal, iconFinal)

    for tech in finalTechItemsExternal:
        type = "tech_external_"+smoothTechData(tech[0])
        iconFinal = iconFinName.format(
            type = type,
            num  = tech[1] - 750000 + 20000
        )
        iconFinal += format
        iconFinal = path + iconFinal
        pathFinal = path + iconTempName + format
        shutil.copyfile(pathFinal, iconFinal)

    print("|Stellaris:     Finished generation of technology icon files                                          |")
import random
import shutil
import string

from . import DataTech, DataEvent
from .DataEvent import unScrewTechData, finalTechItemsInternal, finalTechItemsExternal, unExternalizeTechData
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
        itemLoc = unScrewTechData(item[0])
        if tech["name"] == itemLoc:
            count += 1
    return tech["levels"]-count

def createOutsideTech():
    techText = techStart
    for key,tech in enumerate(finalTechItemsExternal):
        type = "external_"+unExternalizeTechData(tech[0])
        area = randomTechArea[random.randrange(0,2)]
        if area == "physics":
            category = randomTechPhysicsCategory[random.randrange(0,2)]
        elif area == "society":
            category = randomTechSocietyCategory[random.randrange(0,4)]
        else:
            category = randomTechEngineeringCategory[random.randrange(0,3)]
        tier        = random.randrange(1,5)
        cost        = techProgCost+str(random.randrange(1,5))
        weight_null = ""
        weight      = random.randrange(1,5)
        techText    = techText + techTemplate.format(type        = type,
                                                     num         = tech[1],
                                                     area        = area,
                                                     category    = category,
                                                     cost        = cost,
                                                     weight      = weight,
                                                     tier        = tier,
                                                     weight_null = weight_null)
    writeToFile("common/technology/archipelago_external_tech.txt", techText)
    print("    Finished generation of external research definition files")

def createTech():
    """This function assembles the technology definition files in the mod"""
    techText = techStart
    for tech in DataTech.techs:
        type     = "progressive_"+tech["name"]
        area     = tech["area"]
        tier     = tech["tier"]
        category = tech["category"]
        count    = countFinalTechs(tech)
        if count != 0:
            for i in range(count):
                tech["non_research"] += str(i+1)
        for i in range(tech["levels"]):
            tierAdd = i+tier
            if tierAdd > 5:
                tierAdd = 5
            cost = techProgCost
            if str(i+1) in tech["non_research"]:
                cost        = cost + "0"
                weight      = 0
                weight_null = weightNull
            else:
                cost        = cost + str(tierAdd)
                weight      = tierAdd
                weight_null = ""
            techText = techText + techTemplate.format(
                type        = type,
                num         = i+1,
                area        = area,
                category    = category,
                cost        = cost,
                weight      = weight,
                tier        = tierAdd,
                weight_null = weight_null
            )
    writeToFile("common/technology/archipelago_progressive_tech.txt",techText)
    print("    Finished generation of technology definition files")

def createTechLocalisations():
    """This function assembles the technology localisation files in the mod (names and descriptions)"""
    for lang in languages:
        localisationText = localisationStart.format(lang = lang)
        for tech in DataTech.techs:
            type = tech["name"]
            name = "Progressive "+(type[0].upper() + type[1:]).replace("_"," ")
            type = "progressive_"+type
            for i in range(tech["levels"]):
                localisationText = localisationText + localisationTechTemplate.format(
                    type = type,
                    num  = i+1,
                    name = name
                )
        for key, tech in enumerate(finalTechItemsExternal):
            type = "external_"+unExternalizeTechData(tech[0])
            name = str(tech[0])
            localisationText = localisationText + localisationExternalTechTemplate.format(
                type = type,
                num  = key + 1,
                name = name
            )
        writeToFile("localisation/" + lang + "/archipelago_progressive_techs_l_" + lang + ".yml", localisationText,
                    "utf-8-sig")
    print("    Finished generation of technology localisation files")

def createTechIcons():
    """This function assigns icons to technologies"""
    path         = "worlds/stellaris/mod/archipelago-stellaris-mod/gfx/interface/icons/technologies/"
    iconTempName = "tech_progressive"
    iconFinName  = iconTempName+"_{type}_{num}"
    format       = ".dds"
    for tech in DataTech.techs:
        type = tech["name"]
        for i in range(tech["levels"]):
            iconFinal = iconFinName.format(
                type = type,
                num  = i+1
            )+format
            shutil.copyfile(path + iconTempName + format, path + iconFinal)
    print("    Finished generation of technology icon files")
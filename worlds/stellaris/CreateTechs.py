import shutil
from . import DataTech
from .templates.TemplateTech import techStart, techTemplate, techProgCost, weightNull
from .templates.TemplateLocalisation import localisationStart, localisationTechTemplate
from .Utility import writeToFile, languages


def createTech():
    """This function assembles the technology definition files in the mod"""
    techText = techStart
    for tech in DataTech.techs:
        type = tech["name"]
        area = tech["area"]
        tier = tech["tier"]
        category = tech["category"]
        for i in range(tech["levels"]):
            tierAdd = i+tier
            if tierAdd > 5:
                tierAdd = 5
            cost = techProgCost
            if str(i+1) in tech["non_research"]:
                cost = cost + "0"
                weight = 0
                weight_null = weightNull
            else:
                cost = cost + str(tierAdd)
                weight = tierAdd
                weight_null = ""
            techText = techText + techTemplate.format(type = type, num = i+1, area = area, category = category, cost = cost,
                                                      weight = weight, tier = tierAdd, weight_null = weight_null)
    writeToFile("common/technology/archipelago_progressive_tech.txt",techText)
    print("    Finished generation of technology definition files")

def createTechLocalisations():
    """This function assembles the technology localisation files in the mod (names and descriptions)"""
    for lang in languages:
        localisationText = localisationStart.format(lang = lang)
        for tech in DataTech.techs:
            type = tech["name"]
            name = (type[0].upper() + type[1:]).replace("_"," ")
            for i in range(tech["levels"]):
                if i+1 == tech["levels"]:
                    final = "final"
                else:
                    final = "next"
                localisationText = localisationText + localisationTechTemplate.format(type = type, num = i+1,
                                                                                      name = name, final = final)
        writeToFile("localisation/" + lang + "/archipelago_progressive_techs_l_" + lang + ".yml", localisationText,
                    "utf-8-sig")
    print("    Finished generation of technology localisation files")

def createTechIcons():
    """This function assigns icons to technologies"""
    path = "worlds/stellaris/mod/archipelago-stellaris-mod/gfx/interface/icons/technologies/"
    iconTempName = "tech_progressive"
    iconFinName = iconTempName+"_{type}_{num}"
    format = ".dds"
    for tech in DataTech.techs:
        type = tech["name"]
        for i in range(tech["levels"]):
            iconFinal = iconFinName.format(type = type,num = i+1)+format
            shutil.copyfile(path+iconTempName+format,path+iconFinal)
    print("    Finished generation of technology icon files")
import shutil
from . import DataTech
from .templates.TemplateTech import techStart, techTemplate, techProgCost, weightNull
from .templates.TemplateLocalisation import localisationStart, localisationTechTemplate
from .Utility import writeToFile, languages


#This function assembles the Technologies
def createTech():
    techText = techStart
    for tech in DataTech.techs:
        type = tech["name"]
        area = tech["area"]
        tier = tech["tier"]
        category = tech["category"]
        for i in range(tech["levels"]):
            if str(i+1) in tech["non_research"]:
                cost = techProgCost
                weight = 0
                weight_null = weightNull
            else:
                cost = tech["cost"]
                weight = tech["weight"]
                weight_null = ""
            techText = techText + techTemplate.format(type = type, num = i+1, area = area, category = category, cost = cost,
                                                      weight = weight, tier = tier+i, weight_null = weight_null)
    writeToFile("common/technology/archipelago_progressive_tech.txt",techText)

#This function assembles the Technology Localisations (names and descriptions)
def createTechLocalisations():
    for lang in languages:
        localisationText = localisationStart.format(lang = lang)
        for tech in DataTech.techs:
            type = tech["name"]
            name = type[0].upper() + type[1:]
            for i in range(tech["levels"]):
                if i+1 == tech["levels"]:
                    final = "final"
                else:
                    final = "next"
                localisationText = localisationText + localisationTechTemplate.format(type = type, num = i+1, name = name, final = final)
        writeToFile("localisation/" + lang + "/archipelago_progressive_techs_l_" + lang + ".yml", localisationText,"utf-8-sig")

#This function assigns the default icon to every added Technology
def createTechIcons():
    path = "mod/archipelago-stellaris-mod/gfx/interface/icons/technologies/"
    iconTempName = "tech_progressive"
    iconFinName = iconTempName+"_{type}_{num}"
    format = ".dds"
    for tech in DataTech.techs:
        type = tech["name"]
        for i in range(tech["levels"]):
            iconFinal = iconFinName.format(type = type,num = i+1)+format
            shutil.copyfile(path+iconTempName+format,path+iconFinal)
from . import DataTechVanilla, DataTech, DataEvent
from .templates.TemplateEvent import eventStart, eventTemplate, eventAction, eventIfTech, eventNotIfTech, eventGiveTech
from .templates.TemplateLocalisation import localisationStart, localisationEventTemplate
from .Utility import writeToFile, languages

test = True

#This function looks through the tech dictionary for technology with the specified name
def findTech(search):
    for tech in DataTech.techs:
        if tech["name"] == search:
            return tech

#This function assembles the Event logic for when to not trigger
def constructTechAction(tech):
    action = ""
    for i in range(tech["levels"]):
        name = "tech_progressive_" + tech["name"] + "_"
        conditions = ""
        result = eventGiveTech.format(name = name + str(i+1))
        if i != 0:
            elseif = "else_if"
            conditions = conditions + eventIfTech.format(has = name + str(i))
        else:
            elseif = "if"
        if test is True:
            vanilla = DataTechVanilla.vanillaTechs[tech["name"]]
            for split in vanilla[i].split(" "):
                result = result + eventGiveTech.format(name = split)
        conditions = conditions + eventNotIfTech.format(hasnot = name + str(i+1))
        action = action + eventAction.format(elseif = elseif, conditions = conditions, result = result)
    return action

#This function assembles the Events
def createEvents():
    eventText = eventStart
    for key,item in enumerate(DataEvent.items):
        value = item["item_code"]
        if item["type"] == "tech": #Events that give you technology
            tech = findTech(item["name"])
            action = constructTechAction(tech)
        else: #Shouldn't come up except for testing purposes
            action = ""
        eventText = eventText+eventTemplate.format(num = 1000*(key+1),value = value,resource = "urp_000",action = action)
    writeToFile("events/archipelago_dynamic_events.txt",eventText)

#This function assembles the Event Localizations (names and descriptions)
def createEventLocalisations():
    for lang in languages:
        localisationText = localisationStart.format(lang = lang)
        for key,item in enumerate(DataEvent.items):
            value = item["item_code"]
            desc = item["description"]
            localisationText = localisationText + localisationEventTemplate.format(num = 1000*(key+1), value = value, desc = desc)
        writeToFile("localisation/"+lang+"/archipelago_dynamic_events_l_"+lang+".yml", localisationText, "utf-8-sig")
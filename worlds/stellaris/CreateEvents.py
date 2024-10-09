import time

from BaseClasses import CollectionState
from . import DataTechVanilla, DataTech, DataEvent, Options
from .templates.TemplateEvent import eventStart, eventTemplate, eventAction, eventIfTech, eventNotIfTech, eventGiveTech
from .templates.TemplateLocalisation import localisationStart, localisationEventTemplate
from .Utility import writeToFile, languages
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from . import StellarisWorld

def findTech(search):
    """This function looks through the tech dictionary for technology with the specified name"""
    for tech in DataTech.techs:
        if tech["name"] == search:
            return tech

def constructTechAction(tech, world: "StellarisWorld"):
    """This function assembles the Event logic for when to trigger or not to trigger"""
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
        if world.options.researchHardMode.value == 0:
            vanilla = DataTechVanilla.vanillaTechs[tech["name"]]
            for split in vanilla[i].split(" "):
                result = result + eventGiveTech.format(name = split)
        conditions = conditions + eventNotIfTech.format(hasnot = name + str(i+1))
        action = action + eventAction.format(elseif = elseif, conditions = conditions, result = result)
    return action

def createEvents(world: "StellarisWorld"):
    """This function assembles the Events"""
    eventText = eventStart
    for key,item in enumerate(DataEvent.events):
        if item["type"] == "tech": #Events that give you technology
            tech = findTech(item["name"])
            value = key
            action = constructTechAction(tech, world)
        else: #Shouldn't come up except for testing purposes
            action = ""
            value = ""
        eventText = eventText+eventTemplate.format(num = 10000+(key*10+10),value = value+1,resource = "urp_000",action = action)
    writeToFile("events/archipelago_dynamic_events.txt",eventText)
    print("    Finished generation of event definition files")

def createEventLocalisations():
    """This function assembles the Event Localizations (names and descriptions)"""
    for lang in languages:
        localisationText = localisationStart.format(lang = lang)
        for key,item in enumerate(DataEvent.events):
            if item["type"] == "tech":
                value = key
            else: #Shouldn't come up except for testing purposes
                value = ""
            desc = item["description"]
            localisationText = localisationText + localisationEventTemplate.format(num = 10000+(key*10+10), value = value+1, desc = desc)
        writeToFile("localisation/"+lang+"/archipelago_dynamic_events_l_"+lang+".yml", localisationText, "utf-8-sig")
    print("    Finished generation of event localisation files")
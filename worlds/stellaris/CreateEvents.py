import time

from BaseClasses import CollectionState
from . import DataTechVanilla, DataTech, DataEvent, Options
from .DataEvent import finalTechItemsExternal, finalTechItemsInternal, unExternalizeTechData, unScrewTechData
from .templates.TemplateEvent import (eventStart, eventTemplate, eventAction, eventIfTech,
                                      eventNotIfTech, eventGiveTech, eventIfOutTech)
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
        name       = "tech_progressive_" + tech["name"] + "_"
        conditions = ""
        result     = eventGiveTech.format(name = name + str(i+1))
        if i != 0:
            elseif     = "else_if"
            conditions = conditions + eventIfTech.format(has = name + str(i))

        else:
            elseif = "if"

        if world.options.researchHardMode.value == 0:
            vanilla = DataTechVanilla.vanillaTechs[tech["name"]]
            for split in vanilla[i].split(" "):
                result = result + eventGiveTech.format(name = split)

        conditions = conditions + eventNotIfTech.format(hasnot = name + str(i+1))
        action     = action     + eventAction.format(
            elseif         = elseif,
            conditions     = conditions,
            result         = result
        )
    return action

def createEvents(world: "StellarisWorld"):
    """This function assembles the Events"""
    eventText = eventStart
    for key,item in enumerate(DataEvent.events):
        if item["type"] == "techReceive": #Events that give you technology
            tech        = findTech(item["name"])
            value       = key+1
            postValue   = -99999999
            action      = constructTechAction(tech, world)
            num         = 10000+(key*10+10)
            resource    = "urp_000"
            outResearch = ""

        elif item["type"] == "techSend":
            value       = 0
            postValue   = item["location"]-750000
            action      = ""
            num         = item["location"]
            resource    = "urp_001"

            for i in finalTechItemsExternal:
                if item["name"] == unExternalizeTechData(i[0]):
                    has = "tech_external_"+item["name"]+"_"+str(num)
                    break

            for i in finalTechItemsInternal:
                splitItem = str(i[0]).split(" ")
                for j in range(5):
                    addItem = "tech_progressive_"+item["name"]
                    if addItem == splitItem[0]:
                        has = str(splitItem[0])
                        break
            outResearch = eventIfOutTech.format(has = has)

        else: #Shouldn't come up except for testing purposes
            print("|Stellaris: An event didn't generate right! Please check your stuff                               |")
            continue
        eventText = eventText+eventTemplate.format(
            num         = num,
            value       = value,
            postValue   = postValue,
            resource    = resource,
            action      = action,
            outResearch = outResearch
        )
    writeToFile("events/archipelago_dynamic_events.txt",eventText)
    print("|Stellaris:     Finished generation of event definition files                                         |")

def createEventLocalisations():
    """This function assembles the Event Localizations (names and descriptions)"""
    for lang in languages:
        localisationText = localisationStart.format(lang = lang)
        for key,item in enumerate(DataEvent.events):
            if item["type"] == "techReceive":
                value        = key
                num          = 10000+(key*10+10)
                receiveSend  = "received from"
                receivedSent = "received"

            elif item["type"] == "techSend":
                value        = key
                num          = item["location"]
                receiveSend  = "sent to"
                receivedSent = "sent"

            else: #Shouldn't come up except for testing purposes
                print("|Stellaris: An event localisation didn't generate right! Please check your stuff              |")
                continue
            desc = item["description"]
            localisationText = localisationText + localisationEventTemplate.format(
                num          = num,
                value        = value+1,
                desc         = desc,
                receiveSend  = receiveSend,
                receivedSent = receivedSent
            )
        writeToFile("localisation/"+lang+"/archipelago_dynamic_events_l_"+lang+".yml",
                    localisationText,"utf-8-sig")
    print("|Stellaris:     Finished generation of event localisation files                                       |")
import time
from operator import itemgetter

from BaseClasses import CollectionState
from . import DataTechVanilla, DataTech, DataEvent, Options
from .DataEvent import finalTechItemsExternal, finalTechItemsInternal, smoothTechData, unScrewTechData
from .templates.TemplateEvent import (eventStart, eventTemplate, eventAction, eventIfTech,
                                      eventNotIfTech, eventGiveTech, eventIfOutTech, eventSetVar, eventUnsetVar,
                                      eventTemplateReceive)
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

def constructTechAction(tech, i, world: "StellarisWorld"):
    """This function assembles the Event logic for when to trigger or not to trigger"""
    action = ""
    name       = "tech_progressive_" + tech["name"] + "_"
    conditions = ""
    result     = eventGiveTech.format(name = name + str(i+1))

    if i != 0:
        elseif      = "if"
        conditions += eventIfTech.format(has = name + str(i))

    else:
        elseif = "if"
        conditions += eventUnsetVar.format(varname = "checkVarNotForUse",extratab="        ")

    if world.options.researchHardMode.value == 0:
        vanilla = DataTechVanilla.vanillaTechs[tech["name"]]
        for split in vanilla[i].split(" "):
            result = result + eventGiveTech.format(name = split)
    result     += eventSetVar.format(varname = "receive_"+tech["name"]+"_"+str(i+1),extratab = "    ")

    action     += eventAction.format(
        elseif         = elseif,
        conditions     = conditions,
        result         = result
    )
    return action

def createEvents(world: "StellarisWorld"):
    """This function assembles the Events"""
    eventText = eventStart

    for key,item in enumerate(DataEvent.events):
        if item["type"] == "techReceive": #Events that give you technology from received items
            tech        = findTech(item["name"])
            value       = key
            postValue   = -99999999
            num         = 10000 + (key * 10 + 10)
            resource    = "urp_000"
            outResearch = ""

            for i in range(tech["levels"]):
                action = constructTechAction(tech, i, world)

                varCheck = eventUnsetVar.format(varname = "receive_"+tech["name"]+"_"+str(i+1),extratab = "    ")
                has = "tech_progressive_"+tech["name"]+"_"+str(i+1)
                techCheck = eventIfTech.format(has = has)

                if i+1 == tech["levels"]:
                    equalmore = ">="
                else:
                    equalmore = "="

                eventText += eventTemplateReceive.format(
                    num         = num + i + 1,
                    value       = (value * 10 + 10) + (i + 1),
                    postValue   = postValue,
                    resource    = resource,
                    varcheck    = varCheck,
                    action      = action,
                    equalmore   = equalmore,
                    techcheck   = techCheck
                )

        elif item["type"] == "techSend": #Events that send technology location checks to the server
            value       = 0
            postValue   = item["location"]-750000
            num         = postValue + 20000
            action      = eventSetVar.format(varname = "send_" + str(num),extratab = "")
            resource    = "urp_001"
            equalmore   = "="

            for i in finalTechItemsExternal:
                if item["name"] == smoothTechData(i[0]):
                    has = 'tech_external_' + item["name"] + "_" + str(num)
                    break

            for i in finalTechItemsInternal:
                splitItem = str(i[0]).split(" ")

                for j in range(5):
                    addItem = "tech_progressive_"+item["name"]
                    if addItem == splitItem[0]:
                        has = str(splitItem[0])
                        break
            varCheck = eventUnsetVar.format(varname = "send_" + str(num),extratab = "")
            outResearch = eventIfOutTech.format(has = has)
            eventText += eventTemplate.format(
                num         = num,
                value       = value,
                postValue   = postValue,
                resource    = resource,
                action      = action,
                outResearch = outResearch,
                equalmore   = equalmore,
                varCheck    = varCheck
            )

        else: # Shouldn't come up except for testing purposes
            print("|Stellaris: An event didn't generate right! Please check your stuff                               |")
            continue
    writeToFile("events/archipelago_dynamic_events.txt",eventText)
    print("|Stellaris:     Finished generation of event definition files                                         |")

def createEventLocalisations():
    """This function assembles the Event Localizations (names and descriptions)"""
    for lang in languages:
        localisationText = localisationStart.format(lang = lang)

        for key,item in enumerate(DataEvent.events):
            if item["type"] == "techReceive": #Events that give you technology from received items
                tech         = findTech(item["name"])
                value        = key
                num          = 10000+(key*10+10)
                receiveSend  = "received from"
                receivedSent = "received"
                desc         = item["description"]
                for i in range(tech["levels"]):
                    localisationText += localisationEventTemplate.format(
                        num          = num + i + 1,
                        value        = (value * 10 + 10) + (i + 1),
                        desc         = desc,
                        receiveSend  = receiveSend,
                        receivedSent = receivedSent,
                    )

            elif item["type"] == "techSend": #Events that send technology location checks to the server
                value        = key
                num          = item["location"]
                receiveSend  = "sent to"
                receivedSent = "sent"
                desc         = item["description"]

                localisationText = localisationText + localisationEventTemplate.format(
                    num          = num + i + 1,
                    value        = value + 1,
                    desc         = desc,
                    receiveSend  = receiveSend,
                    receivedSent = receivedSent,
                )

            else: #Shouldn't come up except for testing purposes
                print("|Stellaris: An event localisation didn't generate right! Please check your stuff              |")
                continue

        writeToFile("localisation/" + lang + "/archipelago_dynamic_events_l_" + lang + ".yml",
                    localisationText,"utf-8-sig")
    print("|Stellaris:     Finished generation of event localisation files                                       |")
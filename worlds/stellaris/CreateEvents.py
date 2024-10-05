import DataEvent
import DataTech
from templates.TemplateEvent import eventStart, eventTemplate, eventAddTech, eventIfTech, eventNotIfTech
from templates.TemplateLocalisation import localisationStart, localisationEventTemplate
from Utility import writeToFile, languages

def findTech(search): #This function looks through the tech dictionary for technology with the specified name
    for tech in DataTech.techs:
        if tech["name"] == search:
            return tech

def constructTechAction(tech): #This function assembles the Event logic for when to not trigger
    action = ""
    for i in range(tech["tiers"]):
        name = "tech_progressive_" + tech["name"] + "_"
        conditions = ""
        elseif = "if"
        if i != 0:
            elseif = "else_if"
            conditions = conditions + eventIfTech.format(has =  name + str(i))
        conditions = conditions + eventNotIfTech.format(hasnot = name + str(i+1))
        action = action + eventAddTech.format(elseif = elseif, conditions = conditions, name = name + str(i + 1))
    return action

def createEvents(): #This function assembles the Events
    eventText = eventStart
    for key,item in enumerate(DataEvent.items):
        value = item["item_code"]
        if item["type"] == "tech": #Events that give you technology
            tech = findTech(item["name"])
            action = constructTechAction(tech)
        else: #Shouldn't come up except for testing purposes
            action = ""
        eventText = eventText+eventTemplate.format(num=1000*(key+1),value=value,resource="urp_000",action = action)
    writeToFile("events/archipelago_dynamic_events.txt",eventText)

def createEventLocalisations(): #This function assembles the Event Localizations
    for lang in languages:
        localisationText = localisationStart.format(lang=lang)
        for key,item in enumerate(DataEvent.items):
            value = item["item_code"]
            desc = item["description"]
            localisationText = localisationText + localisationEventTemplate.format(num=1000*(key+1), value=value, desc=desc)
        writeToFile("localisation/"+lang+"/archipelago_dynamic_events_l_"+lang+".yml", localisationText, "utf-8-sig")
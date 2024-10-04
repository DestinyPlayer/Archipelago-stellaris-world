import DataEvent
import DataTech
from templates.TemplateEvent import eventStart, eventTemplate, eventAddTech, eventIfTech, eventNotIfTech
from templates.TemplateLocalisation import localisationStart, localisationEventTemplate
from Utility import writeToFile, languages

def findTech(search):
    for tech in DataTech.techs:
        if tech[0] == search:
            return tech

def constructTechAction(item,key,tech):
    action = ""
    for i in range(tech[1]):
        name = "tech_progressive_" + tech[0] + "_"
        conditions = ""
        elseif = "if"
        if i != 0:
            elseif = "else_if"
            conditions = conditions + eventIfTech.format(has =  name + str(i))
        conditions = conditions + eventNotIfTech.format(hasnot = name + str(i+1))
        action = action + eventAddTech.format(elseif = elseif, conditions = conditions, name = name + str(i + 1))
    return action

def createEvents():
    eventText = eventStart
    for key,item in enumerate(DataEvent.items):
        value = item[0]
        if item[1] == "tech":
            tech = findTech(item[2])
            action = constructTechAction(item,key,tech)
        else:
            action = ""
        eventText = eventText+eventTemplate.format(num=1000*(key+1),value=value,resource="urp_000",action = action)
    writeToFile("events/archipelago_dynamic_events.txt",eventText)

def createEventLocalisations():
    for lang in languages:
        localisationText = localisationStart.format(lang=lang)
        for key,item in enumerate(DataEvent.items):
            value = item[0]
            desc = item[3]
            localisationText = localisationText + localisationEventTemplate.format(num=1000*(key+1), value=value, desc=desc)
        writeToFile("localisation/"+lang+"/archipelago_dynamic_events_l_"+lang+".yml", localisationText, "utf-8-sig")
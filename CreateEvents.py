import DataEvent
from templates.TemplateEvent import eventStart, eventTemplate
from templates.TemplateLocalisation import localisationStart, localisationEventTemplate
from Utility import writeToFile, languages

def createEvents():
    eventText = eventStart
    for evnum in range(len(DataEvent.items)):
        value = DataEvent.items[evnum]
        eventText = eventText+eventTemplate.format(evnum=1000+evnum+1,value=value,resource="urp_000")
    writeToFile("events/archipelago_dynamic_events.txt",eventText)

def createEventLocalisations():
    for lang in languages:
        localisationText = localisationStart.format(lang=lang)
        for evnum in range(len(DataEvent.items)):
            player = int(str(DataEvent.items[evnum])[0])
            value = DataEvent.items[evnum]
            localisationText = localisationText + localisationEventTemplate.format(evnum=1000+evnum+1,value=value,player=DataEvent.players[player-1],desc=DataEvent.itemsDesc[evnum])
        writeToFile("localisation/"+lang+"/archipelago_dynamic_events_l_"+lang+".yml", localisationText, "utf-8-sig")

createEvents()
createEventLocalisations()
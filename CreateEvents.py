import EventData
from templates.EventTemplate import eventStart, eventTemplate
from templates.LocalisationTemplate import localisationStart, localisationTemplate

languages = [
    "braz_por","english","french","german","japanese","korean","polish","russian","simp_chinese","spanish"
]

def writeToFile(path,text,encoding=None):
    path = "mod/testresource/"+path
    if encoding != None:
        f = open(path, "w", encoding=encoding)
    else:
        f = open(path, "w")
    f.write(text)
    f.close()

def createEvents():
    eventText = eventStart
    for evnum in range(len(EventData.items)):
        value = EventData.items[evnum]
        eventText = eventText+eventTemplate.format(evnum=1000+evnum+1,value=value,resource="urp_000")
    writeToFile("events/archipelago_dynamic_events.txt",eventText)

def createLocalisations():
    for lang in languages:
        localisationText = localisationStart.format(lang=lang)
        for evnum in range(len(EventData.items)):
            player = int(str(EventData.items[evnum])[0])
            value = EventData.items[evnum]
            localisationText = localisationText + localisationTemplate.format(evnum=1000+evnum+1,value=value,player=EventData.players[player-1],desc=EventData.itemsDesc[evnum])
        writeToFile("localisation/"+lang+"/archipelago_dynamic_events_l_"+lang+".yml", localisationText, "utf-8-sig")

createEvents()
createLocalisations()
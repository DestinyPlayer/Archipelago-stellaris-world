import string

from . import DataTech

finalTechItemsInternal = []
finalTechItemsExternal = []
finalLocations         = []
events                 = []

def unScrewTechData(tech):
    tech = str(tech)
    tech = tech.replace(" ","_")
    tech = tech.split("_")
    tech.remove("tech")
    tech.remove("progressive")
    for i in range(3):
        tech.pop(len(tech) - 1)
    finalTech = tech[0]
    for i in range(len(tech) - 1):
        finalTech += "_" + tech[i + 1]
    return finalTech

def smoothTechData(tech):
    tech      = str(tech)
    tech      = tech.translate(str.maketrans('','',string.punctuation))
    tech      = tech.replace(" ","_")
    tech      = tech.lower()
    finalTech = tech
    return finalTech

def fillInTechData():
    global events

    #Tech Receive
    for tech in DataTech.techs:
        events.append({
            "type":        "techReceive",
            "name":        tech["name"],
            "description": "Progressive "+tech["name"].replace("_"," ")+" technology"
        })

    finalTechItemsCombined = finalTechItemsExternal + finalTechItemsInternal
    finalTechItemsCombined.sort(key=lambda x: x[1])

    #Tech Send
    for finalTech in finalTechItemsCombined:
        if finalTech in finalTechItemsInternal:
            finalEventTech = smoothTechData(finalTech[0])
            events.append({
                "type":        "techSend",
                "name":        finalEventTech,
                "description": "Progressive "+finalEventTech.replace("_"," ")+" technology",
                "location":    finalTech[1],
                "internal":    True,
                "player":      finalTech[3]
            })
        elif finalTech in finalTechItemsExternal and finalTechItemsExternal:
            finalEventTech = smoothTechData(finalTech[0])
            events.append({
                "type":        "techSend",
                "name":        finalEventTech,
                "description": str(finalTech[0]),
                "location":    finalTech[1],
                "internal":    False,
                "player":      finalTech[3]
            })

    print("|Stellaris:     Finished generation of Event Data                                                     |")
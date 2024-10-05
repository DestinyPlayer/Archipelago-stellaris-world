import CreateEvents
import CreateTechs
import Utility

CreateTechs.createTech()
CreateTechs.createTechLocalisations()
CreateTechs.createTechIcons()

CreateEvents.createEvents()
CreateEvents.createEventLocalisations()

Utility.copyOtherLocalisationFiles("archipelago_events_l_english.yml")
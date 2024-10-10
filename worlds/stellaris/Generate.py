import shutil
from typing import TYPE_CHECKING

from . import CreateEvents, CreateTechs, Utility, DataEvent

if TYPE_CHECKING:
    from . import StellarisWorld

def generateMod(world: "StellarisWorld", outputDirectory):
    print("|Stellaris: Generating mod                                                                            |")

    #DataEvent
    DataEvent.fillInTechData()

    #Events
    CreateEvents.createEvents(world)
    CreateEvents.createEventLocalisations()

    # Technology
    CreateTechs.createTech()
    CreateTechs.createOutsideTech()
    CreateTechs.createTechLocalisations()
    CreateTechs.createTechIcons()

    Utility.copyOtherLocalisationFiles("archipelago_events_l_english.yml")
    #shutil.copytree("worlds/stellaris/mod","output/mod")
    print("|Stellaris: Mod generation complete                                                                   |")
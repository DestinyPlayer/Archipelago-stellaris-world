import shutil
from typing import TYPE_CHECKING

from . import CreateEvents, CreateTechs, Utility

if TYPE_CHECKING:
    from . import StellarisWorld

def generateMod(world: "StellarisWorld", outputDirectory):
    print("Generating Stellaris mod")
    CreateTechs.createTech()
    CreateTechs.createTechLocalisations()
    CreateTechs.createTechIcons()

    CreateEvents.createEvents(world)
    CreateEvents.createEventLocalisations()

    Utility.copyOtherLocalisationFiles("archipelago_events_l_english.yml")
    #shutil.copytree("worlds/stellaris/mod","output/mod")
    print("Mod generation complete")
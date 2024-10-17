import shutil
from typing import TYPE_CHECKING

from . import CreateEvents, CreateTechs, Utility, DataEvent, DataTech

if TYPE_CHECKING:
    from . import StellarisWorld

def generateMod(world: "StellarisWorld", outputDirectory):
    print("|Stellaris: Generating mod                                                                            |")

    # Starting setup
    Utility.generateLangFolders()
    #DataTech.addDlcTechs(world)

    # Generating Events List
    DataEvent.fillInTechData()

    # Generating Technology Definitions
    CreateTechs.createTech()
    CreateTechs.createOutsideTech()
    CreateTechs.createOutsideTechLocalisations()
    CreateTechs.createTechLocalisations()
    CreateTechs.createTechIcons()

    # Generating Events Definitions
    CreateEvents.createEvents(world)
    CreateEvents.createEventLocalisations()

    # Finalizing Mod Generation
    Utility.copyOtherLocalisationFiles("archipelago_events_l_english.yml")
    #shutil.copytree("worlds/stellaris/mod","output/mod")
    print("|Stellaris: Mod generation complete                                                                   |")
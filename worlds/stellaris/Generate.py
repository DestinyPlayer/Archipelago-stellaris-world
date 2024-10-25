import shutil
from typing import TYPE_CHECKING, Any
from . import CreateEvents, CreateTechs, Utility, DataEvent, DataTech

if TYPE_CHECKING:
    from . import StellarisWorld

def prepareModFolder(world: "StellarisWorld", directory):
    print("|Stellaris: Preparing mod folder                                                                      |")
    shutil.copytree("worlds\stellaris\mod",directory+"\stellaris-mod")

def finalizeMod(outputDirectory):
    print("|Stellaris: Zipping the mod up                                                                        |")
    shutil.make_archive(outputDirectory+"\stellaris-mod", "zip", outputDirectory+"\stellaris-mod")
    shutil.rmtree(outputDirectory+"\stellaris-mod")


def generateMod(world: "StellarisWorld", outputDirectory):
    print("|Stellaris: Generating mod                                                                            |")

    # Starting setup
    Utility.generateLangFolders(outputDirectory)
    #DataTech.addDlcTechs(world)

    # Generating Events List
    DataEvent.fillInTechData()

    # Generating Technology Definitions
    CreateTechs.createTech(outputDirectory)
    CreateTechs.createOutsideTech(outputDirectory)
    CreateTechs.createOutsideTechLocalisations(outputDirectory)
    CreateTechs.createTechLocalisations(outputDirectory)
    CreateTechs.createTechIcons(outputDirectory)

    # Generating Events Definitions
    CreateEvents.createEvents(world,outputDirectory)
    CreateEvents.createEventLocalisations(outputDirectory)

    # Finalizing Mod Generation
    Utility.copyOtherLocalisationFiles("archipelago_events_l_english.yml",outputDirectory)
    finalizeMod(outputDirectory)

    #shutil.copytree("worlds/stellaris/mod","output/mod")
    print("|Stellaris: Mod generation complete                                                                   |")
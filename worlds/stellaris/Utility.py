import os
import shutil
from . import DataTech

languages = [
    "braz_por",
    "english",
    "french",
    "german",
    "japanese",
    "korean",
    "polish",
    "russian",
    "simp_chinese",
    "spanish"
]

def generateLangFolders():
    for lang in languages:
        path = "worlds/stellaris/mod/archipelago-stellaris-mod/"+"localisation/"+lang
        if not os.path.isdir(path):
            os.mkdir(path)

#This function writes files to the mod folder
def writeToFile(path,text,encoding=None):
    path = "worlds/stellaris/mod/archipelago-stellaris-mod/"+path
    if encoding is not None:
        f = open(path, "w", encoding=encoding)
    else:
        f = open(path, "w")
    f.write(text)
    f.close()

def getTotalResearchCount():
    count = 0
    for tech in DataTech.techs:
        for i in range(tech["levels"]):
            count += 1
    return count

#This function copies over non-procedurally generated localisation files between languages
def copyOtherLocalisationFiles(file):
    for lang in languages:
        if lang == "english":
            continue
        path    = "worlds/stellaris/mod/archipelago-stellaris-mod/localisation/"
        finPath = path + lang + "/" + file.replace("english", lang)
        path   += "english/" + file
        shutil.copyfile(path, finPath)
        f = open(finPath,"r")
        fileText = f.read()
        f.close()
        f = open(finPath,"w")
        f.write(fileText.replace("english",lang))
        f.close()
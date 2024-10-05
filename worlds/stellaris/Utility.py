languages = [
    "braz_por","english","french","german","japanese","korean","polish","russian","simp_chinese","spanish"
]

#This function writes files to the mod folder
def writeToFile(path,text,encoding=None):
    path = "mod/archipelago-stellaris-mod/"+path
    if encoding is not None:
        f = open(path, "w", encoding=encoding)
    else:
        f = open(path, "w")
    f.write(text)
    f.close()
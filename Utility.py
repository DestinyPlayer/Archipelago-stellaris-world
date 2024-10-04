languages = [
    "braz_por","english","french","german","japanese","korean","polish","russian","simp_chinese","spanish"
]

languages = [
    "braz_por","english","french","german","japanese","korean","polish","russian","simp_chinese","spanish"
]

def writeToFile(path,text,encoding=None):
    path = "mod/testresource/"+path
    if encoding is not None:
        f = open(path, "w", encoding=encoding)
    else:
        f = open(path, "w")
    f.write(text)
    f.close()
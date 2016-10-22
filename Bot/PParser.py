from subprocess import check_output
def PParser(url):
    entries=[]
    cally = check_output(["youtube-dl", "-g", str(url)])
    colly = cally.decode("utf-8")
    for entri in colly.split("\n"):
        entries.append(str(entri))

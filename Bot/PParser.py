from subprocess import check_output
def PParser(url, decode=False):
    entries=[]
    cally = check_output(["youtube-dl", "-g", str(url)])
    colly = cally.decode("utf-8")
    for entri in colly.split("\n"):
    	if (decode == True):
    		entries.append(str(entri))
    	else:
    		entries.append(str.encode(entri))
    if (decode == False):
    	del entries[-1]
    return entries

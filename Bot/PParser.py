"""Copyright (C) 2016  Jbdo99&Clem133

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
from subprocess import check_output
import asyncio
@asyncio.coroutine
def PParser(url,meth="-g",decode=False):
    """
    Fonction pour recupérer une liste contenant les urls d une playlist
    Utilisation : PParser(url, methode(-g ou -e))
    """
    entries=[]
    cally = check_output(["youtube-dl", meth, str(url)])
    colly = cally.decode("utf-8")
    for entri in colly.split("\n"):
    	if (decode == True):
    		entries.append(str(entri))
    	else:
    		entries.append(str.encode(entri))
    if (decode == False):
    	del entries[-1]
    return entries

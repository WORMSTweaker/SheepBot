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
from ftplib import FTP
class FTPV():
    def connect(host, login,mdp):
        self.ftp = FTP('ftp.livehost.fr')
        try:
            self.ftp.login(login,mdp)
        except Exception(e):
            raise e
    def FileList(SDirectory="main"):
        if (SDirectory=="main"):
            self.lfile = self.ftp.nlst()
        else:
            self.lfile = self.ftp.nlst(SDirectory)
        return self.lfile
    def FileDict(SDirectory="main"):
        self.dfile={}
        if (SDirectory=="main"):
            for i in range(len(self.ftp.nlst())):
                self.dfile[i]=self.ftp.nlst()[i]
        else:
            for i in range(len(self.ftp.nlst(SDirectory))):
                self.dfile[i]=self.ftp.nlst(SDirectory)[i]
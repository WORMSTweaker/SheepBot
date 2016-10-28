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
import sqlite3


class Playlist():
    def __init__(self):
        self.db = sqlite3.connect('playlist.db')
        self.cursor = self.db.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS playlist(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,lien TEXT)""")
        self.db.commit()

    def addSong(self, lien):
        """
        Ajoute un lien dans la BDD (return : True)
        """
        self.cursor.execute("""INSERT INTO playlist(lien) VALUES(?)""", [lien])
        self.db.commit()
        return True

    def getAllLien(self):
        """
        Recupere tous les liens dans la BDD (return : list)
        """
        self.reponse = []
        self.cursor.execute("""SELECT lien FROM playlist""")
        rows = self.cursor.fetchall()
        for row in rows:
            self.reponse.append('{0}'.format(row[0]))
        return self.reponse

    def getAllId(self):
        """
        Recupere tous les id dans la BDD (return : list)
        """
        self.reponsess = []
        self.cursor.execute("""SELECT id FROM playlist""")
        rows = self.cursor.fetchall()
        for row in rows:
            self.reponsess.append('{0}'.format(row[0]))
        self.reponsess = [int(x) for x in self.reponsess]
        return self.reponsess

    def getAllDic(self, debug=False):
        """
        Recupere tous les liens et id dans la BDD (return : dict)
        """
        self.reponses = {}
        lien = self.getAllLien()
        id = self.getAllId()
        for i in range(len(id)):
            self.reponses[id[i]] = lien[i]
        return self.reponses

    def delSongLien(self, lien):
        """
        Supprime un lien (par le lien) dans la BDD (return : True)
        """
        self.cursor.execute("""DELETE FROM playlist WHERE lien=?""", [lien])
        self.db.commit()

    def delSongId(self, id):
        """
        Supprime un lien (par l id) dans la BDD (return : True)
        """
        self.cursor.execute("""DELETE FROM playlist WHERE id=?""", [id])
        self.db.commit()

    def changeSongLienByLien(self, originallien, newlien):
        """
        Change un lien (par le lien) dans la BDD (return : True)
        """
        self.cursor.execute(
            """UPDATE playlist SET lien = ? WHERE lien = ?""",
            (newlien, originallien))
        self.db.commit()

    def changeSongLienById(self, id, newlien):
        """
        Change un lien (par l id) dans la BDD (return : True)
        """
        self.cursor.execute(
            """UPDATE playlist SET lien = ? WHERE id = ?""", (newlien, id))
        self.db.commit()

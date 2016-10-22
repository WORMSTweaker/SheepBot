<<<<<<< HEAD
import sqlite3
import datetime

class Playlist():
	def __init__(self):
		self.db = sqlite3.connect('playlist.db')
		self.cursor = self.db.cursor()
		self.cursor.execute("""
		CREATE TABLE IF NOT EXISTS playlist(
		     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
		     lien TEXT
		)
		""")
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


	def getAllDic(self,debug = False):
		"""
		Recupere tous les liens et id dans la BDD (return : dict)
		"""
		self.reponses = {}
		lien = self.getAllLien()
		id = self.getAllId()
		for i in range(len(id)):
			self.reponses[id[i]]=lien[i]
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


	def changeSongLienByLien(self,originallien, newlien):
		"""
		Change un lien (par le lien) dans la BDD (return : True)
		"""
		self.cursor.execute("""UPDATE playlist SET lien = ? WHERE lien = ?""", (newlien,originallien))
		self.db.commit()

		
	def changeSongLienById(self,id , newlien):
		"""
		Change un lien (par l id) dans la BDD (return : True)
		"""
		self.cursor.execute("""UPDATE playlist SET lien = ? WHERE id = ?""", (newlien,id))
		self.db.commit()
=======
import sqlite3
import datetime

class Playlist():
	def __init__(self):
		self.db = sqlite3.connect('playlist.db')
		self.cursor = self.db.cursor()
		self.cursor.execute("""
		CREATE TABLE IF NOT EXISTS playlist(
		     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
		     lien TEXT
		)
		""")
		self.db.commit()
	def addsong(self, lien):
		self.cursor.execute("""INSERT INTO playlist(lien) VALUES(?)""", [lien])
		self.db.commit()


	def getall(self):
		self.reponse = []
		self.cursor.execute("""SELECT lien FROM playlist""")
		rows = self.cursor.fetchall()
		for row in rows:
			self.reponse.append('{0}'.format(row[0]))
		return self.reponse



>>>>>>> 3d8b8f512dee960801053d20fff3fc522be27ebc

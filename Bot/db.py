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




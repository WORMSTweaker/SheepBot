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

import asyncio
import discord
import logging
import os
import time
import wikipedia
import sys
import string
import ffmpy
import random
import wolframalpha
import subprocess
import credentials
import re
import inspect
import mcrcon
import youtube_dl
from gtts import gTTS
from db import Playlist
from discord import opus
from random import randint
from cleverbot import Cleverbot
from mcstatus import MinecraftServer
from PParser import PParser
from PyFTP import FTPV

wolfclient = wolframalpha.Client('K58L69-KG2G437U8V')
logging.basicConfig(level=logging.INFO)
client = discord.Client()
servers = list(client.servers)
Stopit = 'pls'
porazika = 'non'
vol = 50
p1 = ""
p2 = ""
cp1 = "X"
cp2 = "O"
touplay = ""
global p1
global p2
global cp1
global cp2
global tourplay

ftp = ""


OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll', 'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
        try:
            opus.load_opus(opus_lib)
            return
        except OSError:
            pass

lunched = 'Nope'
Zika = 'off'
autozik = 'nop'
global autozik
cb = Cleverbot()
playnext = []
Lapeti = []
lepeticreateur = 0
Banchan = []
memo = []
var = {
"oui":"Non!!!",
"meuh":"Ho, une vache",
"ping":"pong!!",
"pong": "ping?",
"!ping":"PONG!!!!!",
"bite":"pfffff, j'en ait 64 alors bon...",
"encul":"Vazy ta dits quoi la?",
"FDP":"FTP?",
"fdp":"FTP?",
"pute":"coquinne vas!",
"merde":":poop: ",
"salop":":point_up_2: ",
"non":"si!",
"NON":"SI!!",
"Non": "sisi",
"Hello":"its me...",
"hello":"its me...",
"Hi":"hello",
"jb":"jb est mort!",
"clem":"Le Dieux clément tout puissant (et pas dutout narcicisique vas vous repondre sous peu)",
"lol":"mdr",
"mdr":"lol",
"LOL":"League Of legends",
"XD":":smile: ",
"sudo":"sudo-mi!",
"pourquoi":"Parce que",
"Ok":":ok_hand: ",
"pk":"pourquoi???",
"pff":"fait chier, nan?",
"oki":"doki",
"nop":"Objection!!",
"roo":"lolololo",
"Raa":"XD",
"raa":"XD",
"Bonjour,":"Salut fdp",
"biatch":"et alors?",
"Oo":"oO",
"oO":"Oo",
"GG":"on s'en fout.",
"Bite":"Sexy",
"putain":"de merde",
"Bouh":"Haaaaaaa",
"bouh":"HHHHAAAAAAAAAAAAAAA!!!",
"tg":"tu veux dire La ferme?",
"Hey":"listen",
"hey":"listen",
"nop":"NOPE",
"HELLO":"du calme...",
"TADA":"Woooaaaa!",
"a+":"a-",
"i was wondering if after all":"NON PAS PLUS",

"test":"testing..."
}



#-- P4 core






class Board():
    """Grille de jeu et methodes pour la modifier"""
    def __init__(self,jeu="p4",p1="X",p2="O"):
        """Initialisation de la grille"""
        self.jeu = jeu
        # dimensions de la grille
        if (self.jeu == "p4"):
            self.nbrCol = 7
            self.nbrLig = 8
        if (self.jeu == "xo"):
            self.nbrCol = 3
            self.nbrLig = 3 
        self.couleurs = [p1, p2]
        # generation de la grille
        self.grille = []
        for i in range(self.nbrCol):
            self.grille.append([])
        # historique
        self.history = []

    def add(self, col, couleur, silent = None):
        """ajouter un jeton
           col = 1.. numéro de la colonne
           retour : la position du jeton (col, ligne)
                     (None, code erreur)  si erreur"""
        # quelques vérifications avant d'ajouter le jeton
        if not couleur in self.couleurs:
            if not silent : print ("Couleur non conforme :",couleur)
            return (None, 0)
        if (col<1) or (col>self.nbrCol):
            if not silent : print ("Valeur colonne non conforme : ",col)
            return (None, 1)
        if len(self.grille[col-1])==self.nbrLig:
            if not silent : print ("Impossible d'ajouter jeton, colonne pleine : ",col)
            return (None, 2)
        self.grille[col-1].append(couleur)
        self.history.append( (couleur, col-1) )
        return (col-1, len(self.grille[col-1])-1)

    def print_l(self,sizel="|       "):
        """Retourné une liste avec chaque ligne en str"""
        ##print( self.grille)
        lretour = []
        for j in range(self.nbrLig-1,-1,-1):
            if j ==0:
                line = str(j+1)+'  '
            else:
                line = str(j+1)+' '

            for i in range(self.nbrCol):
                ##print (len(self.grille[i]),j)
                if len(self.grille[i]) <= j:
                    line = line + sizel
                else:
                    ##print(i,j)
                    line = line + "|  "+self.grille[i][j]+'  '
            line = line + "|"
            lretour.append(line)
        tamp='    '
        for i in range(self.nbrCol):
            tamp = tamp+'   '+str(i+1)+'   '
        lretour.append(tamp)
        return lretour    

    def print(self):




        """imprimer la grille"""
        ##print( self.grille)
        for j in range(self.nbrLig-1,-1,-1):
            line = str(j+1)+' '
            for i in range(self.nbrCol):
                ###print (len(self.grille[i]),j)
                if len(self.grille[i]) <= j:
                    line = line + "|   "
                else:
                    ###print(i,j)
                    line = line + "| "+self.grille[i][j]+' '
            line = line + "|"
            yield from client.send_message(message.channel, line)
        print ('  ',end='')
        for i in range(self.nbrCol):
            yield from client.send_message(message.channel,'  '+str(i+1)+' ')
        yield from client.send_message(message.channel,)




    def print_g(self):
        """imprimer la grille avec pygame"""
        ##print( self.grille)
        pos_y = 9
        for j in range(self.nbrLig-1,-1,-1):
            line = str(j+1)+' '
            pos_x = 9
            pos_y = pos_y + 9
            for i in range(self.nbrCol):
                ###print (len(self.grille[i]),j)
                if len(self.grille[i]) <= j:
                    line = line + "|   "
                    pos_x = pos_x + 9 + 80
                else:
                    ###print(i,j)
                    if (self.grille[i][j] == "X"):
                        fenetre.blit(pion_r, (pos_x,pos_y))
                        pos_x = pos_x + 9
                    if (self.grille[i][j] == "O"):
                        fenetre.blit(pion, (pos_x,pos_y))
                        pos_x = pos_x + 9
                    else:
                        exit()
                        
            line = line + "|"
            print (line)
        print ('  ',end='')
        for i in range(self.nbrCol):
            print ('  '+str(i+1)+' ',end='')
        print()

    def color(self, location):
        """returns the color of the location (col, lig)"""
        ###print("Location : ",location)
        if (len(self.grille[location[0]]) <= location[1]):
            return None
        return self.grille[location[0]][location[1]]

    def check(self, start, debug=False):
        """compter les jetons alignés
           retour : nombre max. alignés"""
        dirs = [(1,0), (0,1), (1,1), (-1,1)]
        maxAlign = 0
        print ("start",start)
        myColor = self.color(start)
        if not myColor: #case vide donnee
            print ("Error 001")
            return 0
        for di in dirs:
            if debug: print ("start direction ",di)
            n = 1
            # search in both directions
            for sign in [1.0,-1.0]:
                for i in range(1, (self.nbrCol+self.nbrLig)):
                    x = int(start[0]+float(i)*di[0]*sign)
                    y = int(start[1]+float(i)*di[1]*sign)
                    if (x<0) or (y<0) or (x>=self.nbrCol) or (y>=self.nbrLig): break
                    if debug: print("check ",x,y)
                    if self.color((x,y))==myColor:
                        n += 1
                        if debug: print("found one ; n = ",n)
                    else:
                        break
            if n > maxAlign: maxAlign = n
        return maxAlign
        



p1 = ""
p2 = ""
cp1 = "X"
cp2 = "O"
touplay = ""
global p1
global p2
global cp1
global cp2
global tourplay

#P4 end


        


wikipedia.set_lang("fr")

mut_mut = ["0","1"]

@client.async_event
def on_ready():
    print('Connected on discord')
    print(client.user.name)
    print(client.user.id)
    hard = discord.Object(id="178882236324642816")
    yield from client.send_message(hard, "On :)")
    yield from client.change_presence(game=discord.Game(name=random.choice(["dibou","rtichau","Broutter","la claire fontaine","bricot"])))
    print ('Ready')
    

            
            
    
    






@client.async_event
def on_resumed():
    hard = discord.Object(id="178882236324642816")
    yield from client.send_message(hard, "Resumed")

@client.async_event
def on_member_remove(member):
    yield from client.send_message(member, 'Byeeeee ;)')

@client.async_event
def on_member_join(member):
    yield from client.send_message(member, 'Salut :)')

@client.async_event
def on_server_remove(server):
    hard = discord.Object(id="178882236324642816")
    yield from client.send_message(hard, 'Removed : '+server.name)




@client.async_event
def on_message(message):
    if message.author.id == client.user.id:
            return
    global mut_mut
    for element in mut_mut:
        if message.author.id == element:
            yield from client.delete_message(message)
            yield from client.send_message(message.author, 'Nope')
            return



    if message.content.startswith('prune'):
        if message.server.name == 'FTW':
            print ('FTW exept')
            return
        pruneday = message.content.replace('prune ','')
        perms = message.channel.permissions_for(message.author)
        for permi in perms:
            if str(permi) == ("('administrator', True)") :
                print ('pruning by : ', message.author)
                yield from client.send_message(message.channel, 'Pruning...')
                pruned = yield from client.prune_members(message.server,days=int(pruneday))
                yield from client.send_message(message.channel, 'Pruned : '+str(pruned))
                
            




    if message.content.startswith('chan Off'):
        yield from client.send_typing(message.channel)
        Banchan.append(message.channel.id)
        yield from client.send_message(message.channel, "Reponse perso desactivée sur"+message.channel.id)

    if message.content.startswith('chan On'):
        yield from client.send_typing(message.channel)
        Banchan.remove(message.channel.id)
        yield from client.send_message(message.channel, "Reponse perso réeactivée sur : "+message.channel.id)

    if message.content.startswith('persoff'):
        Stopit = 'pls'
    if message.content.startswith('person'):
        Stopit = 'UUUUIIIII'





    if message.content.startswith('ftp'):
    	global ftp
    	yield from client.delete_message(message)
    	host = message.content.replace('ftp ','')
    	ftp = FTPV(host)

    if message.content.startswith('ftpco'):
    	global ftp
    	yield from client.delete_message(message)
    	login = message.content.replace('ftpco ','')
    	mdp = login.split()[1]
    	ftp.connect(login,mdp)

    if message.content.startswith('ftpl'):
    	global ftp
    	lake = ""
    	for lik in ftp.FileList():
    		lake= "| "+lik
    	yield from client.start_private_message(message.author)
    	yield from client.delete_message(message)
    	yield from client.send_message(message.author, lake)


    


#musik Yeah

    if message.content.startswith('reco'):
        global player
        global porazika
        global Zika
        yield from client.delete_message(message)
        if lunched == 'yep':
            playnext = []
            player.stop()
        porazika = 'ui'
        yield from voice.disconnect()
        yield from asyncio.sleep(0.5)
        voice = yield from client.join_voice_channel(message.author.voice.voice_channel)
        Zika = 'on'
        porazika = 'noup'



    if message.content.startswith('join'):
        voice = yield from client.join_voice_channel(message.author.voice.voice_channel)
        yield from client.delete_message(message)
        Zika = 'on'


    if message.content.startswith('listZik'):
        p=Playlist()
        loul = p.getAllLien()
        for mUzi in loul:
            yield from client.send_message(message.channel, mUzi)
        return




    if message.content.startswith('vol'):
        global vol
        vol = message.content.replace('vol ','')
        print(vol,'%')
        player.volume = int(vol)/100
        









    if message.content.startswith('autoZik'):
        global voice
        global porazika
        global Zika
        global lunched
        global musikal
        global autozik
        global playnext
        global vol
        yield from client.delete_message(message)
        if autozik == 'on':
            print ('conflit')
            return
        
        autozik = 'on'
        if Zika == 'off':
            voice = yield from client.join_voice_channel(message.author.voice.voice_channel)
            print ('connected')
            Zika = 'on'
        if lunched == 'yep':
            playnext = []
            player.stop()
        p=Playlist()
        loul = p.getAllLien()
        while True:
            if Zika == 'off':
                return
            yield from client.send_typing(message.channel)
            player = yield from voice.create_ytdl_player(random.choice(loul))
            player.volume = int(vol)/100
            player.start()
            if not True:
                return
            print ('playing : ', player.title)
            yield from client.change_presence(game=discord.Game(name=player.title))
            hard = discord.Object(id="178882236324642816")
            yield from client.send_message(hard, player.title)
            while player.is_playing():
                if porazika == 'ui':
                    autozik = 'nop'
                    print ('ended')
                    player.stop()
                    return
                yield from asyncio.sleep(0.3)
            print ('next song')
            

    if message.content.startswith('addik'):
        global voice
        global Zika
        global lunched
        global musikal
        global playnext
        p = Playlist()
        lip = message.content.replace('addik ','')
        p.addSong(lip)
        hard = discord.Object(id="178882236324642816")
        yield from client.send_message(hard, "added a Zik")


    if message.content.startswith('infoZik'):
        yield from client.send_typing(message.channel)
        dure = str(player.duration)
        likes = str(player.likes)
        dislikes = str(player.dislikes)
        vues = str(player.views)
        yield from client.send_message(message.channel, "Nom :  "+player.title+"\nURL : "+player.url+"\n Description : \n"+player.description+"\n \n Durée :  "+dure+"s"+"\n Likes/Dislikes : "+likes+"/"+dislikes+"\n Vues : "+vues)






    if message.content.startswith('Zik'):
        global voice
        global Zika
        global lunched
        global musikal
        global playnext
        global porazika
        global vol
        porazika = 'ui'
        yield from asyncio.sleep(0.5)
        if Zika == 'off':
            voice = yield from client.join_voice_channel(message.author.voice.voice_channel)
            Zika = 'on'

        musikal = message.content.replace('Zik ','')
        if musikal.startswith('https://www.youtube.com/playlist'):
            yield from client.send_message(message.channel, "Playlist non prise en charge")
            return
        if musikal.startswith('https://www.youtube.com/channel'):
            yield from client.send_message(message.channel, "veuillez entrez une video :)")
            return


        if lunched == 'yep':
            playnext.append(musikal)
            playnext.append(musikal)
            print('added song')
            yield from client.send_message(message.channel, "added to playlist :)")
            return
        playnext.append(musikal)

        if musikal.startswith('https://www.youtube.com/playlist'):
            yield from client.send_message(message.channel, "Playlist non prise en charge")
            return
        if musikal.startswith('https://www.youtube.com/channel'):
            yield from client.send_message(message.channel, "veuillez entrez une video :)")
            return


        for lipo in playnext:
            playnext.remove(lipo)
            tobirater = yield from client.send_message(message.channel, "Wait for it...")
            yield from client.send_typing(message.channel)
            player = yield from voice.create_ytdl_player(lipo)
            player.volume = int(vol)/100
            player.start()
            print ('playing : ', player.title)
            yield from client.change_presence(game=discord.Game(name=player.title))
            hard = discord.Object(id="178882236324642816")
            yield from client.send_message(hard, player.title)
            yield from client.edit_message(tobirater,':notes: :notes: :notes: :notes: :notes: ')
            lunched = 'yep'
            while player.is_playing():
                yield from asyncio.sleep(0.5)
        lunched = 'Nope'
        playnext = []
        porazika = 'noup'
        autozik = 'nop'
        yield from lient.change_presence(game=discord.Game(name=random.choice(["dibou","rtichau","Broutter","la claire fontaine","bricot"])))




    if message.content.startswith('TTS'):
        global voice
        global Zika
        global lunched
        global musikal
        global playnext
        global porazika
        porazika = 'ui'
        yield from asyncio.sleep(0.5)
        if Zika == 'off':
            voice = yield from client.join_voice_channel(message.author.voice.voice_channel)
            Zika = 'on'

        TTS = message.content.replace('TTS ','')

        if lunched == 'yep':
            yield from client.send_message(message.channel, "Attendez la fin de la lecture en cour")
            return

        tts = gTTS(text=TTS, lang='fr')
        tts.save("TTS.mp3")
        player = voice.create_ffmpeg_player('TTS.mp3')
        player.start()
        lunched = 'yep'
        while not player.is_done():
            yield from asyncio.sleep(1)
        lunched = 'Nope'
        playnext = []
        porazika = 'noup'
        autozik = 'nop'







    if message.content.startswith('Pause'):
        global player
        yield from client.delete_message(message)
        player.pause()

    if message.content.startswith('Resume'):
        global player
        yield from client.delete_message(message)
        player.resume()
    if message.content.startswith('Stop'):
        global player
        yield from client.delete_message(message)
        player.stop()

    if message.content.startswith('end'):
        global player
        yield from client.delete_message(message)
        lunched = 'Nope'
        playnext = []
        porazika = 'ui'
        yield from asyncio.sleep(3)
        porazika = 'noup'



    if message.content.startswith('deco'):
        global player
        Zika = 'off'
        yield from client.delete_message(message)
        yield from voice.disconnect()


#change statut + Help + Wikipedia




    if message.content.startswith('Wolf'):
            yield from client.send_typing(message.channel)
            res = wolfclient.query(message.content.replace('Wolf ',''))
            print('computed!')
            for pod in res.pods:
                print('{p.title}  :  {p.text}'.format(p=pod))
                if pod.text:
                    yield from client.send_message(message.channel, '{p.title} :  {p.text}'.format(p=pod))
                elif pod.img:
                    yield from client.send_message(message.channel, '{p.title} :\n{p.img}'.format(p=pod))
            



    if message.content.startswith('rcon'):
        print("rcon")
        rconeri = message.content.replace('rcon ','')
        rconeri = rconeri.split(",")
        rcon = mcrcon.MCRcon()

        yield from client.send_message(message.channel,"connecting...")
        port = int(rconeri[1])
        rcon.connect(rconeri[0],port)
        rcon.login(rconeri[2])
        response = rcon.command(rconeri[3])
        if response:
            yield from client.send_message(message.channel,+("  %s" % response))
        rcon.disconnect()

    if message.content.startswith('Statut'):
        statou = message.content.replace('Statut ','')
        server = MinecraftServer.lookup(statou)
        status = server.status()
        yield from client.send_message(message.channel,"The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))




    if message.content.startswith('Cbot'):
            print (message.content)
            yield from client.send_typing(message.channel)
            yield from asyncio.sleep(0.5)
            yield from client.send_message(message.channel, cb.ask(message.content.replace('Cbot ','')))


    if message.content.startswith('Help'):
            yield from client.send_typing(message.channel)
            yield from asyncio.sleep(1)
            yield from client.send_message(message.channel, ' Commandes : \n \n - persoff / person : désactive / active les réponses perso \n - Zik *lien_youtbe_ou_soundcloud* : joue la musique / l\'ajoute à la queue \n - join : summon le bot dans le channel de l\'auteur du msg \n - Pause : Met la musique en pause \n - Resume : continue la musique \n - Stop : musique suivante / Stop si aucune musique dans la queue \n - deco : déconnecte le bot du chan vocal  \n - Cbot *nimortequoi* : permet de parler avec le bot \n - wiki *recherche Wikipédia* : recherche Wikipédia \n - dit *un_truc* : fait dire ce que vous voulez au bot \n - 42 : réponse a tout \n - memo add *votre memo* : ajoute un memo \n - memo show : montre vos memos \n -memo remove *votre memo* : supprime le memo \n - remind *nb de minute* : ajoute un rappel dans un temps définit en minute \n - spam *nb* : spam le chan \n - dance / 2dance : Fait danser le bot \n - p4start : créer un p4 \n - play : lance le p4 précédemment créer \n - pfc *pierre/feuille/ciseaux* : joue a pierre feuille ciseaux \n - random *nb* : donne un nombre en entre 0 est le nb choisit \n - me / me-id : donne votre nom et votre id \n - bot *statut* : change le statut du bot  \n -  Sheep random : :smiley: ')


    if message.content.startswith('wiktype'):
            yield from client.send_typing(message.channel)
            wik = wikipedia.search(message.content.replace('wikitype ',''))
            yield from client.send_message(message.channel, wik)

    if message.content.startswith('wiki'):
            yield from client.send_typing(message.channel)
            hard = discord.Object(id="178882236324642816")
            yield from client.send_message(hard, "Wikipeding ")
            yield from asyncio.sleep(1)
            wiki = wikipedia.summary(message.content.replace('wiki ',''))
            wikia = wiki.split(".")
            for element in wikia:
                yield from client.send_message(message.channel, element)



# dit 42



    if message.content.startswith('dit'):
        yield from client.send_message(message.channel, message.content.replace('dit',''))


    if message.content.startswith('42'):
        yield from client.send_message(message.channel,random.choice(['Oui','Non','Mais oui c''est clair!','Peut étre..','Nope','oui','non','jsp','oui','non','non','oui','oui','non','VTFF','Té...leportation!','Hum tt de facon,  personne connais l\'origine','Ceci est un message de Jbdo99']))



#Mute
    if message.content.startswith('Mute'):
            Dirlo = 177394669766836224
            print ('mute')
            print (message.author)
            print (message.content)
            Viagra = message.content.replace('Mute ','')
            Viagra = int(Viagra)
            if Viagra == Dirlo:
                print ('Nope')
                yield from client.send_message(message.channel, 'Nope Biatch')
                return
            
            mut_mut.append(Viagra)
            yield from client.send_message(message.channel, 'Ok')
            hard = discord.Object(id="178882236324642816")
            yield from client.send_message(hard, "Muting : "+Viagra)

    if message.content.startswith('de-Mute'):
            print ('de-mute')
            print (message.author)
            print (message.content)
            mut_mut.remove(message.content.replace('de-Mute ',''))
            yield from client.send_message(message.channel, 'pffff, dommage')
            hard = discord.Object(id="178882236324642816")
            yield from client.send_message(hard, "De-muted")

#memo + remind

    if message.content.startswith('memo'):
            lasuite = message.content.replace('memo ','')
            if lasuite.startswith('add'):
                memo.append(message.author.id + lasuite.replace('add ',''))
                yield from client.send_message(message.channel, 'added')
                print('added')
                return
            if lasuite.startswith('show'):
                yield from client.send_message(message.channel, 'trucs a faire :')
                for Memor in memo:
                    if Memor.startswith(message.author.id):
                        yield from client.send_message(message.channel, Memor.replace(message.author.id,''))
                        print ('Memo')
                return
            if lasuite.startswith('remove'):
                memo.remove(message.author.id + message.content.replace('memo remove ',''))
                yield from client.send_message(message.channel, 'removed')
                print('removed')
                return
            if message.content == 'memo':
                yield from client.send_message(message.channel, 'commandes : add, remove, show')


    if message.content.startswith('remind'):
            aho = message.content.replace('remind ','')
            aho,yp = aho.split(".")
            Sec = int(aho)
            Sec = Sec*60
            print('dring?')
            yield from asyncio.sleep(Sec)
            print('dring')
            yield from client.send_message(message.channel, 'DRIIIIIINNNGGG!!! : '+yp)











# PENSER A MODIFIER!!!!

    if message.content.startswith('spam'):
            rt = message.content.replace('spam ','')
            rt = int(rt)
            bz = 0
            print ('spam',message.author)
            if rt > 20:
                yield from client.send_message(message.channel, 'Nope, pas plus de 20!!')
                print (message.channel)
                return
            if message.channel.name == 'general':
                yield from client.send_message(message.channel, 'Nope, pas ici!!!')
                print (message.channel)
                return
            hard = discord.Object(id="178882236324642816")
            yield from client.send_message(hard, "Spamming")
            while bz < rt :
                yield from client.send_message(message.channel, random.choice(["SPAM!!!","spam","Hello","yo","Hey!!","I love spamming","spam!!!","spam","SPAAAAMMM","sssssssSSSSSSSSSSSSPPPPPPPPPAAAAAAAAMMMMMMM","SPAM!!","¤SPAM¤","§SPAM§","SPAM","/o/","\o\\","\o/","SPARTA","^^",":robot:",":space_invader:", ":poop:", ":snake:", ":8ball:", ":skull:", ":trophy:", ":rainbow:", ":iphone:", ":computer:", ":keyboard:", ":mouse_three_button:", ":joystick:", ":moneybag:", ":dollar:", ":euro:", ":money_with_wings:", ":skull_crossbones:", ":shield:", ":electric_plug:", ":exclamation:", ":warning:", ":mega:", ":ram:", ":grinning:", ":scream:", ":spy:",":sheep:"]) + random.choice(["SPAM!!!","spam","Hello","yo","Hey!!","I love spamming","spam!!!","spam","SPAAAAMMM","sssssssSSSSSSSSSSSSPPPPPPPPPAAAAAAAAMMMMMMM","SPAM!!","¤SPAM¤","§SPAM§","SPAM","/o/","\o\\","\o/","SPARTA","^^",":robot:",":space_invader:", ":poop:", ":snake:", ":8ball:", ":skull:", ":trophy:", ":rainbow:", ":iphone:", ":computer:", ":keyboard:", ":mouse_three_button:", ":joystick:", ":moneybag:", ":dollar:", ":euro:", ":money_with_wings:", ":skull_crossbones:", ":shield:", ":electric_plug:", ":exclamation:", ":warning:", ":mega:", ":ram:", ":grinning:", ":scream:", ":spy:",":sheep:"]) + random.choice(["SPAM!!!","spam","Hello","yo","Hey!!","I love spamming","spam!!!","spam","SPAAAAMMM","sssssssSSSSSSSSSSSSPPPPPPPPPAAAAAAAAMMMMMMM","SPAM!!","¤SPAM¤","§SPAM§","SPAM","/o/","\o\\","\o/","SPARTA","^^",":robot:",":space_invader:", ":poop:", ":snake:", ":8ball:", ":skull:", ":trophy:", ":rainbow:", ":iphone:", ":computer:", ":keyboard:", ":mouse_three_button:", ":joystick:", ":moneybag:", ":dollar:", ":euro:", ":money_with_wings:", ":skull_crossbones:", ":shield:", ":electric_plug:", ":exclamation:", ":warning:", ":mega:", ":ram:", ":grinning:", ":scream:", ":spy:",":sheep:"]) + random.choice(["SPAM!!!","spam","Hello","yo","Hey!!","I love spamming","spam!!!","spam","SPAAAAMMM","sssssssSSSSSSSSSSSSPPPPPPPPPAAAAAAAAMMMMMMM","SPAM!!","¤SPAM¤","§SPAM§","SPAM","/o/","\o\\","\o/","SPARTA","^^",":robot:",":space_invader:", ":poop:", ":snake:", ":8ball:", ":skull:", ":trophy:", ":rainbow:", ":iphone:", ":computer:", ":keyboard:", ":mouse_three_button:", ":joystick:", ":moneybag:", ":dollar:", ":euro:", ":money_with_wings:", ":skull_crossbones:", ":shield:", ":electric_plug:", ":exclamation:", ":warning:", ":mega:", ":ram:", ":grinning:", ":scream:", ":spy:",":sheep:"]) + random.choice(["SPAM!!!","spam","Hello","yo","Hey!!","I love spamming","spam!!!","spam","SPAAAAMMM","sssssssSSSSSSSSSSSSPPPPPPPPPAAAAAAAAMMMMMMM","SPAM!!","¤SPAM¤","§SPAM§","SPAM","/o/","\o\\","\o/","SPARTA","^^",":robot:",":space_invader:", ":poop:", ":snake:", ":8ball:", ":skull:", ":trophy:", ":rainbow:", ":iphone:", ":computer:", ":keyboard:", ":mouse_three_button:", ":joystick:", ":moneybag:", ":dollar:", ":euro:", ":money_with_wings:", ":skull_crossbones:", ":shield:", ":electric_plug:", ":exclamation:", ":warning:", ":mega:", ":ram:", ":grinning:", ":scream:", ":spy:",":sheep:"]) + random.choice(["SPAM!!!","spam","Hello","yo","Hey!!","I love spamming","spam!!!","spam","SPAAAAMMM","sssssssSSSSSSSSSSSSPPPPPPPPPAAAAAAAAMMMMMMM","SPAM!!","¤SPAM¤","§SPAM§","SPAM","/o/","\o\\","\o/","SPARTA","^^",":robot:",":space_invader:", ":poop:", ":snake:", ":8ball:", ":skull:", ":trophy:", ":rainbow:", ":iphone:", ":computer:", ":keyboard:", ":mouse_three_button:", ":joystick:", ":moneybag:", ":dollar:", ":euro:", ":money_with_wings:", ":skull_crossbones:", ":shield:", ":electric_plug:", ":exclamation:", ":warning:", ":mega:", ":ram:", ":grinning:", ":scream:", ":spy:",":sheep:"]) + random.choice(["SPAM!!!","spam","Hello","yo","Hey!!","I love spamming","spam!!!","spam","SPAAAAMMM",'MESAGE SUBLIMINAL',"sssssssSSSSSSSSSSSSPPPPPPPPPAAAAAAAAMMMMMMM","SPAM!!","¤SPAM¤","§SPAM§","SPAM","/o/","\o\\","\o/","SPARTA","^^",":robot:",":space_invader:", ":poop:", ":snake:", ":8ball:", ":skull:", ":trophy:", ":rainbow:", ":iphone:", ":computer:", ":keyboard:", ":mouse_three_button:", ":joystick:", ":moneybag:", ":dollar:", ":euro:", ":money_with_wings:", ":skull_crossbones:", ":shield:", ":electric_plug:", ":exclamation:", ":warning:", ":mega:", ":ram:", ":grinning:", ":scream:", ":spy:",":sheep:"]))                    
                bz = bz + 1
                print (bz)




# Time to dance \o/


    if message.content.startswith('dance'):
            dan = 0
            mlg = yield from client.send_message(message.channel,'\o\\ \o\\ \o\\ \o\\ \o\\ \o\\ \o\\ \o\\ \o\\ ')
            while dan < 10:
                yield from client.edit_message(mlg,'/o/ /o/ /o/ /o/ /o/ /o/ /o/ /o/ /o/')
                yield from asyncio.sleep(1)
                yield from client.edit_message(mlg, '\o\\ \o\\ \o\\ \o\\ \o\\ \o\\ \o\\ \o\\ \o\\ ')
                yield from asyncio.sleep(1)
                dan = dan + 1

    if message.content.startswith('2dance'):
            dan = 0
            mlg = yield from client.send_message(message.channel,'Lets Danceee')
            while dan < 8:
                yield from client.edit_message(mlg,'_o\\ _o\\ _o\\ _o\\ _o\\ _o\\ _o\\ _o\\ _o\\ ')
                yield from asyncio.sleep(0.6)
                yield from client.edit_message(mlg,'\o\\ \o\\ \o\\ \o\\ \o\\ \o\\ \o\\ \o\\ \o\\ ')
                yield from asyncio.sleep(0.6)
                yield from client.edit_message(mlg, '|o| |o| |o| |o| |o| |o| |o| |o| |o|')
                yield from asyncio.sleep(0.6)
                yield from client.edit_message(mlg, '/o/ /o/ /o/ /o/ /o/ /o/ /o/ /o/ /o/')
                yield from asyncio.sleep(0.6)
                yield from client.edit_message(mlg, '/o\_ /o\_ /o\_ /o\_ /o\_ /o\_ /o\_ /o\_ /o\_')
                yield from asyncio.sleep(0.6)
                dan = dan + 1
            yield from client.edit_message(mlg,' \'__\'')

    if message.content.startswith('bg'):
            dan = 0
            mlg = yield from client.send_message(message.channel,'clement')
            while dan < 8:
                yield from client.edit_message(mlg,'Clement')
                yield from asyncio.sleep(0.21)
                yield from client.edit_message(mlg,'cLement')
                yield from asyncio.sleep(0.21)
                yield from client.edit_message(mlg, 'clEment')
                yield from asyncio.sleep(0.21)
                yield from client.edit_message(mlg, 'cleMent')
                yield from asyncio.sleep(0.21)
                yield from client.edit_message(mlg, 'clemEnt')
                yield from asyncio.sleep(0.21)
                yield from client.edit_message(mlg, 'clemeNt')
                yield from asyncio.sleep(0.21)
                yield from client.edit_message(mlg, 'clemenT')
                yield from asyncio.sleep(0.21)
                dan = dan + 1
            yield from client.edit_message(mlg,'clément!')


#P4, on message

    if message.content.startswith('change p1'):
        cp1 = message.content.replace('change p1 ','')



    if message.content.startswith('change p2'):
        cp2 = message.content.replace('change p2 ','')



    if message.content.startswith('p4start'):
            global p1
            global p2
            global cp1
            global cp2
            global tourplay
            yield from client.send_message(message.channel, "La parti de puissance 4 va commencer. Merci de vous trouver dans le channel dédié a cet usage !")
            if(p1 == ""):
                yield from client.send_message(message.channel, "Merci de choisir le joueur 1 avec la commande p1")
            if (p2 == ""):
                yield from client.send_message(message.channel, "Merci de choisir le joueur 2 avec la commande p2")
            else:
                if (p1 == p2):
                   yield from client.send_message(message.channel, "Vous ne pouvez pas jouer avec vous meme ! Tapez p4restart") 
                else:
                    Jeu = Board(p1=cp1,p2=cp2)
                    yield from lient.change_presence(game=discord.Game(name="Puissance 4"))
                    tourplay = "p1"
                    yield from client.send_message(message.channel, "Au tour de P1 !")

    if message.content.startswith('p4restart'):
            global p1
            global p2
            global cp1
            global cp2
            global tourplay
            yield from client.send_message(message.channel, "Remise a zero des joueurs et du jeu...")
            p1 = ""
            p2 = ""
            cp1 = "X"
            cp2 = "O"
            touplay = ""



    if (message.content.startswith('play')):
        global p1
        global p2
        global cp1
        global cp2
        global trend
        global tourplay
        global t
        global Jeu
        if (str(message.author) == p1 and tourplay =="p1"):
            collone = int(message.content.replace('play ',''))
            dernierJeton = Jeu.add(int(collone), cp1)
            trump=[]
            if (len(cp1)==1 and len(cp2)==1):
                trump=Jeu.print_l()
            else:
                trump=Jeu.print_l(sizel="|             ")
            for trend in trump:
                trend = trend + t + "\n"
            yield from client.send_message(message.channel, trend)
            suiteMax = Jeu.check(dernierJeton)
            if suiteMax == 4:
                yield from client.send_message(message.channel, "P1 a gagné ! Pour relancer, tapez p4restart")
            tourplay = "p2"
        if (str(message.author) == p2 and tourplay =="p2"):
            collone = int(message.content.replace('play ',''))
            dernierJeton = Jeu.add(int(collone), cp2)
            trump=[]
            if (len(cp1)==1 and len(cp2)==1):
                trump=Jeu.print_l()
            else:
                trump=Jeu.print_l(sizel="|             ")
            for t in trump:
                trend = trend + t + "\n"
            yield from client.send_message(message.channel, trend)
            suiteMax = Jeu.check(dernierJeton)
            if suiteMax == 4:
                yield from client.send_message(message.channel, "P2 a gagné ! Pour relancer, tapez p4restart")
            tourplay = "p1"
        else:
            print("ERREUR")



    if message.content.startswith('p1'):
            global p1
            if (p1 == ""):
                namem = message.author
                xyb = "Le joueur 1 est : "+str(namem)
                p1 = str(message.author)
                print (p1)
                print (xyb)
                yield from client.send_message(message.channel, xyb)
            else:
                yield from client.send_message(message.channel, "P1 deja choisi ! Pour relancer, tapez p4restart")


    if message.content.startswith('p2'):
            global p1
            global p2
            global cp1
            global cp2
            if (p2 == ""):
                namem = message.author
                xyz = "Le joueur 2 est : "+str(namem)
                p2 = str(message.author)
                yield from client.send_message(message.channel, xyz)
            else:
                yield from client.send_message(message.channel, "P2 deja choisi ! Pour relancer, tapez p4restart")
                

#P4 on message end

#THIS IS NOT THE END

#hastag





# le beau code opti :)
# pierre feuille ciseaux

    if message.content.startswith('pfc'):
        rep = random.choice(["pierre","feuille","ciseaux"])
        yield from client.send_message(message.channel, rep)
        messa = message.content.replace('pfc ','')
        print ('pfc')
        if rep == "pierre":
            if messa == "feuille":
                yield from client.send_message(message.channel, "ta gagné :)")
            if messa == "pierre":
                yield from client.send_message(message.channel, "egalité!")
            if messa == "ciseaux":
                yield from client.send_message(message.channel, "Perdue !!!!")
            print ('pierre')

        if rep == "feuille":
            if messa == "feuille":
                yield from client.send_message(message.channel, "egalité")
            if messa == "pierre":
                yield from client.send_message(message.channel, "Perdue !!!!!")
            if messa == "ciseaux":
                yield from client.send_message(message.channel, "ta gagné :)")
            print ('feuille')


        if rep == "ciseaux":
            if messa == "feuille":
                yield from client.send_message(message.channel, "Perdue!!!!!")
            if messa == "pierre":
                yield from client.send_message(message.channel, "ta gagné!!")
            if messa == "ciseaux":
                yield from client.send_message(message.channel, "égalité!!!")
            print ('ciseaux')



#OSEF

    if message.content.startswith('random'):
            Rand = message.content.replace('random ','')
            Rand = int(Rand)
            
            yield from client.send_message(message.channel, randint(0,Rand))
            print ('random',message.author)

            
    if message.content.startswith('Me-id'):
            yield from client.send_message(message.channel, message.author.id)    
            print ('id',message.author)

#test
    if message.content.startswith('Msg'):
            yield from client.send_typing(message.channel)
            yield from asyncio.sleep(3)
            sentmsg = yield from client.send_message(message.channel,'Hi')
            yield from asyncio.sleep(3)
            yield from client.delete_message(sentmsg)


# change statut, Off et Hey bot(prgm test)!

    if message.content.startswith('bot'):
            yield from client.change_presence(game=discord.Game(name=message.content.replace('bot ','')))
            yield from client.delete_message(message)
            print (message.content)
            return
    if message.content.startswith('Reboot'):
            yield from client.send_typing(message.channel)
            yield from asyncio.sleep(0.5)
            yield from client.send_message(message.channel, 'Rebooooottt.....')
            print ('Off by',message.author)
            hard = discord.Object(id="178882236324642816")
            yield from client.send_message(hard, "Off by "+message.author.name)
            yield from client.close()



    if message.content.startswith('Hey bot'):
            print (message.author)
            yield from client.start_private_message(message.author)
            yield from client.delete_message(message)
            yield from client.send_message(message.author, 'Hello!')


#Useless

    #Sheep Gif :)
    if message.content.startswith('Sheep random'):
            yield from client.send_message(message.channel,random.choice(["http://i.giphy.com/cS8ljLbg3NFPq.gif","http://i.giphy.com/SmsPkjwylhpPW.gif","http://i.giphy.com/3o7WTFsxglCE1NxnEc.gif","http://i.giphy.com/xThuW0HsMlHu90FNQc.gif","http://i.giphy.com/xThuWpV1xwmzLYWQTe.gif","http://i.giphy.com/l2R07IjgM202WpXmE.gif","https://media.giphy.com/media/fUMhF7Vp5iLVm/giphy.gif","http://i.giphy.com/l3971JV3FaExDZbe8.gif","http://i.giphy.com/l396KzSQ2emojNHG0.gif","http://i.giphy.com/l2R04xY6r2nPf8Lhm.gif","http://i.giphy.com/l2QZYUOALzAW7U6wU.gif","http://i.giphy.com/3osxYpa03BAZ0sSUAo.gif","http://i.giphy.com/3osxYcpnc18ZATBX4k.gif","http://i.giphy.com/STZH9QHOS5q7K.gif","http://i.giphy.com/JR1gFcWnidhGU.gif","http://i.giphy.com/pD4mUFQR0ovmg.gif","http://i.giphy.com/oUVZQaOyjWJ6U.gif","http://i.giphy.com/zDoEG6ZxKUcPS.gif"]))
    if message.content.startswith('Sheep money'):
            yield from client.send_message(message.channel, 'http://i.giphy.com/l3971JV3FaExDZbe8.gif')        
    if message.content.startswith('Sheep eat'):
            yield from client.send_message(message.channel, 'http://i.giphy.com/l0D7owZkScVOuGbhC.gif')        
    if message.content.startswith('Sheep school'):
            yield from client.send_message(message.channel, 'http://i.giphy.com/l396KzSQ2emojNHG0.gif')        
    if message.content.startswith('Sheep search'):
            yield from client.send_message(message.channel, 'http://i.giphy.com/l3V0C9CT3UFAQ49Jm.gif')        
    if message.content.startswith('Sheep post'):
            yield from client.send_message(message.channel,random.choice(["http://i.giphy.com/3o7WTFsxglCE1NxnEc.gif","http://i.giphy.com/xThuW0HsMlHu90FNQc.gif","http://i.giphy.com/xThuWpV1xwmzLYWQTe.gif"]))
                  
    if message.content.startswith('Sheep crazy'):
            yield from client.send_message(message.channel, 'http://i.giphy.com/3osxYcpnc18ZATBX4k.gif')        
    if message.content.startswith('Sheep deal'):
            yield from client.send_message(message.channel, 'http://i.giphy.com/l2R07IjgM202WpXmE.gif')





#custom responce
    global Stopit
    if Stopit == 'pls':
        return
    global Banchan
    for Bno in Banchan:
        if Bno == message.channel.id:
            return

    if (message.content.split(' ')[0] in var.keys()):
            yield from client.send_typing(message.channel)
            yield from asyncio.sleep(0.5)
            yield from client.send_message(message.channel, var[message.content.split(' ')[0]])
  
    if message.content.startswith('yo'):
            yield from client.send_message(message.channel,random.choice(["Yop","Hi","Hello","yo","Hey!!"]))
    if message.content.startswith('salut'):
            yield from client.send_message(message.channel,random.choice(['Salut!!!','Yo','Yop','Hello']))




print('presque pret')

client.run('clemen.landier2@gmail.com','3690741')

# END

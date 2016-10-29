"""
   Checking if modules are available
"""
import pip
import sys

class Checking():
 def check():
  if not 'asyncio' in sys.modules.keys():
   pip.main(['install', 'asyncio'])

  if not 'discord' in sys.modules.keys():
   pip.main(['install', 'git+https://github.com/Rapptz/discord.py.git'])

  if not 'logging' in sys.modules.keys():
   pip.main(['install', 'logging'])

  if not 'wikipedia' in sys.modules.keys():
   pip.main(['install', 'wikipedia'])

  if not 'wolframalpha' in sys.modules.keys():
   pip.main(['install', 'git+https://github.com/jaraco/wolframalpha.git'])

  if not 'credentials' in sys.modules.keys():
   pip.main(['install', 'credentials'])

  if not 'inspect' in sys.modules.keys():
   pip.main(['install', 'inspect'])

  if not 'youtube_dl' in sys.modules.keys():
   pip.main(['install', 'youtube_dl'])

  if not 'gTTS' in sys.modules.keys():
   pip.main(['install', 'gTTS'])

  if not 'cleverbot' in sys.modules.keys():
   pip.main(['install', 'cleverbot'])

  if not 'ffmpy' in sys.modules.keys():
   pip.main(['install', 'ffmpy'])

  if not 'mcstatus' in sys.modules.keys():
   pip.main(['install', 'mcstatus'])

  #Not necessary, but useful for discord module
  if not 'PyNaCl' in sys.modules.keys():
   pip.main(['install', 'PyNaCl'])
 
  print("All modules availables! (Probably)")
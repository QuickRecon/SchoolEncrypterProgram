from easygui.easygui import *

#try:
from Settings import *
from Encrypter import *
from Decrypter import *
import os

settingsFilename = "./appsettings.cfg"
settings = Settings(settingsFilename)
encrypter = Encrypter()
encrypter.genkeypair()

print("hello")
#except:
    #exceptionbox()

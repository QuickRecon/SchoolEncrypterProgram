from easygui.easygui import *

#try:
from Settings import *
from Encrypter import *
import os

settingsFilename = "./appsettings.cfg"
settings = Settings(settingsFilename)
encrypter = Encrypter
Encrypter.genkeypair()

print("hello")
#except:
    #exceptionbox()

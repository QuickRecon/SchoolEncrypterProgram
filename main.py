#from easygui.easygui import *

#try:
from Encrypter import *
import os

message = 421234761237234131412198376523847956238975624897653498763498763457896345897634598767854

encrypter = Encrypter()
encrypter.genkeypair()
print(encrypter.converttexttoblockarray(message))
encrypted = encrypter.encrypt(message, encrypter.publickey)

print(message)
print(encrypted)
print(encrypter.decrypt(encrypted, encrypter.publickey))


#except:
    #exceptionbox()

from easygui import *


class Settings(EgStore):

    def __init__(self, filename):  # filename is required
        #-------------------------------------------------
        # Specify default/initial values for variables that
        # this particular application wants to remember.
        #-------------------------------------------------
        self.firstrun = True
        self.privatekey = ""
        self.publickeys = {}

        #-------------------------------------------------
        # For subclasses of EgStore, these must be
        # the last two statements in  __init__
        #-------------------------------------------------
        self.filename = filename  # this is required
        self.restore()            # restore values from the storage file if possible
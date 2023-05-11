"""
Documentation
Description:       Python Library : winAppDriver.py
                   Class Contains methods to start WinAppDriver server and create bridge to access java api
Created-By:        Prasenjit Nandy
"""

from threading import Thread
from library.desktop.winUtil import winUtil

class winAppDriver(Thread):

    def run(self, relativePathOfConfig=None):
        winUtil.initialize()



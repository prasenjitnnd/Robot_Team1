"""
Documentation
Description:       Python Library : winPlugin.py
                   Class Contains method to start robot-windows-plugin , which communicates to jvm contains windows api
Created-By:        Prasenjit Nandy
"""
import os
import subprocess
from threading import Thread

class winPlugin(Thread):
    global startJVMProcess
    def run(self):
        newPath = os.path.abspath(os.getcwd()).split("\\robot\\", 1)[0]
        jarFilePath = newPath + '\\robot\\resource\\external\\robot-windows-pluggin\\wad 0.1.jar'
        winPlugin.startJVMProcess = subprocess.Popen(['java', '-jar', jarFilePath], stdin=subprocess.PIPE,
                                                     stdout=subprocess.PIPE)

        # subprocess.call(['java', '-jar', jarFilePath])
        print("Robot-Windows-Plugin process end ...")


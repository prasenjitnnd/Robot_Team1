"""
Documentation
Description:       Python Library : __init__.py
                   Holds methods to initialize and teardown automation resources for Windows Dialogue
Created-By:        Prasenjit Nandy
"""
import os
import threading
from pathlib import Path
from threading import Thread
from library.desktop.winAppDriver import winAppDriver
from library.desktop.winPlugin import winPlugin


class windowsAutomation(Thread):
    global obj1, obj2
    global thread_winPlugin, thread_winAppDriver

    def run(self):

        relativePathOfConfig = "global\\config.properties"
        # set environment variable for config.properties file path
        os.environ['ANALYTICS_ROBOT_GLOBAL_CONF_PATH'] = str(
            Path(os.path.dirname(os.path.abspath(__file__))).parent.parent) + "\\resource\\" + relativePathOfConfig

        print('Successfully set environment variable ANALYTICS_ROBOT_GLOBAL_CONF_PATH as :' + os.environ[
            'ANALYTICS_ROBOT_GLOBAL_CONF_PATH'])
        windowsAutomation().setEnvVarForAPIParam()
        # creating thread process for initializing Java Plugin & start WAD server
        obj1 = winPlugin()
        obj2 = winAppDriver()
        obj1.start()
        obj2.start()

    def setEnvVarForAPIParam(self):
        os.environ["STLAuto_Locator_Param"] = ''
        os.environ["STLAuto_TextToType_Param"] = ''


    def initialize(self):
        relativePathOfConfig = "global\\config.properties"
        # set environment variable for config.properties file path
        os.environ['ANALYTICS_ROBOT_GLOBAL_CONF_PATH'] = str(
            Path(os.path.dirname(os.path.abspath(__file__))).parent.parent) + "\\resource\\" + relativePathOfConfig

        print('Successfully set environment variable ANALYTICS_ROBOT_GLOBAL_CONF_PATH as :' + os.environ[
            'ANALYTICS_ROBOT_GLOBAL_CONF_PATH'])


        thread_winPlugin = threading.Thread(target=winPlugin(), args=( ))
        thread_winAppDriver = threading.Thread(target=winAppDriver(), args=( ))
        thread_winPlugin.start()
        thread_winPlugin.join()
        thread_winAppDriver.start()

    def tearDownWinAutomation(self):
        thread_winPlugin.join()
        thread_winAppDriver.join()

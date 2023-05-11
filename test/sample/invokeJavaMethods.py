
import time
from threading import Thread
from library.desktop import windowsAutomation, winPlugin
from library.desktop.winPyRoboKeywords import winPyRoboKeywords
from library.desktop.winUtil import winUtil


# class tc(Thread):
#     def run(self):
#         # winUtil().typeUsingFindElementByName("E-mail","prasenjit.nandy@lexmark.com")
#         winPyRoboKeywords().type_using_find_element_byName("E-mail","prasenjit.nandy@lexmark.com")

# windowsAutomation().start()
# # windowsAutomation().initialize()
# time.sleep(15)
# tc().start()
# winPlugin.startJVMProcess.terminate()

def invoke(loc,text):
    windowsAutomation().start()
    # windowsAutomation().initialize()
    time.sleep(15)
    # tc().start()
    winPyRoboKeywords().type_using_find_element_byName(loc,text)
    winPlugin.startJVMProcess.terminate()
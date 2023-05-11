"""
Documentation
Description:       Python Library : winPyRoboKeywords.py
                   Class Contains exposed API to be invoked from Robot Resource file. Methods with @keyword tag can be invoked from robot
Created-By:
"""
import os
import time
from robot.api.deco import keyword
from library.desktop import windowsAutomation
from library.desktop.winUtil import typeUsingFindElementByName, clickUsingFindElementByName, \
    typeUsingFindElementByAccessibilityID, clickUsingFindElementByAccessibilityID, typeUsingFindElementByID, \
    typeUsingFindElementByXpath, typeUsingFindElementByCSS, clickUsingFindElementByID, clickUsingFindElementByXpath, \
    clickUsingFindElementByCSS


class winPyRoboKeywords:
    @keyword
    def initialize_windows_automation(self):
        windowsAutomation().start()
        time.sleep(15)

    @keyword
    def type(self, locator_strategy, locator_value, text_to_type):
        os.environ["STLAuto_Locator_Param"] = locator_value
        os.environ["STLAuto_TextToType_Param"] = text_to_type
        if locator_strategy == 'by.name':
            typeUsingFindElementByName().start()

        if locator_strategy == 'by.id':
            typeUsingFindElementByID().start()

        if locator_strategy == 'by.xpath':
            typeUsingFindElementByXpath().start()

        if locator_strategy == 'by.css':
            typeUsingFindElementByCSS().start()

        if locator_strategy == 'by.accessibilityID':
            typeUsingFindElementByAccessibilityID().start()

    @keyword
    def click(self,locator_strategy, locator):
        os.environ["STLAuto_Locator_Param"] = locator
        if locator_strategy == 'by.name':
            clickUsingFindElementByName().start()

        if locator_strategy == 'by.id':
            clickUsingFindElementByID().start()

        if locator_strategy == 'by.xpath':
            clickUsingFindElementByXpath().start()

        if locator_strategy == 'by.css':
            clickUsingFindElementByCSS().start()

        if locator_strategy == 'by.accessibilityID':
            clickUsingFindElementByAccessibilityID().start()

    @keyword
    def wait(self):
        time.sleep(10)


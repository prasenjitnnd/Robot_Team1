"""
Documentation
Description:       Python Library : printPyRoboKeywords.py
                   Class Contains method to interact with Moja device using UPS library
Created-By:        Prasenjit Nandy
"""
from robot.api.deco import keyword

from library.printer import moja
from library.printer.moja import device


class printPyRoboKeywords():
    global ups

    @keyword
    def initialize_moja(self, printer_ip):
        printPyRoboKeywords.ups=device.initialize(printer_ip)

    @keyword
    def click_using_visible_text_in_moja(self,text_to_press):
        device.click_oppanel_using_text(printPyRoboKeywords.ups,text_to_press)

    @keyword
    def wait_until_text_found_in_moja(self, text):
        device.wait_until_text_found(printPyRoboKeywords.ups,text)

    @keyword
    def press_KEYCODE_BACK_in_moja(self):
        device.press_KEYCODE_BACK(printPyRoboKeywords.ups)

    @keyword
    def press_KEYCODE_HOME_in_moja(self):
        device.press_KEYCODE_HOME(printPyRoboKeywords.ups)

    @keyword
    def wait_until_text_id_found_in_moja(self, text_id):
        device.wait_until_text_id_found(printPyRoboKeywords.ups,text_id)

    @keyword
    def click_oppanel_using_text_id_in_moja(self, text_id):
        device.click_oppanel_using_text_id(printPyRoboKeywords.ups,text_id)



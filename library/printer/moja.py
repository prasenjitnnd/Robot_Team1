"""
Documentation
Description:       Python Library : moja.py
                   Class Contains method to interact with Moja device using UPS library
Created-By:        Prasenjit Nandy
"""
from lxk_universal_panel_step import UPS

class device():

    def initialize(ip):
        print(ip)
        ups = UPS(printer_ip=ip)
        ups.initialize()
        return ups

    def click_oppanel_using_text(upsObj,text_to_press):
        upsObj.regex('on text "'+text_to_press+'" do "press"')

    def wait_until_text_found(upsObj,text):
        upsObj.regex('on text "'+text+'" Do "wait_until_found"')

    def press_KEYCODE_BACK(upsObj):
        upsObj.regex('do "press key KEYCODE_BACK"')

    def press_KEYCODE_HOME(upsObj):
        upsObj.regex('do "press key KEYCODE_HOME"')

    def wait_until_text_id_found(upsObj,text_id):
        upsObj.ups.regex('Find widget "text-id=\''+text_id+'\'" Do "wait_until_found"')

    def click_oppanel_using_text_id(upsObj,text_id):
        upsObj.ups.regex('Find widget "text-id=\''+text_id+'\'" do "press"')

from datetime import time
from lxk_universal_panel_step import UPS

# def interact() :
#     print('')
#     ups = UPS(printer_ip='10.195.7.109')
#     ups.initialize()
#     # time.sleep(5)
#     ups.regex('do "press key KEYCODE_HOME"')
#     ups.regex('Find widget "text-id=\'idle_text\'" do "press"')
#
# interact()
from library.printer.moja import device

ups = device.initialize("10.195.7.109")
device.press_KEYCODE_HOME(ups)
# moja_device.click_oppanel_using_text(ups,"PIN Login")

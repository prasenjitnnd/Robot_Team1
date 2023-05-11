# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from   lxk_universal_panel_step import UPS

def printerinteract() :
    print('10.195.7.37')
    ups = UPS(printer_ip='10.195.7.37')
    ups.initialize()
    time.sleep(5)
    ups.regex('do "press key KEYCODE_HOME"')
    time.sleep(2)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    printerinteract()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

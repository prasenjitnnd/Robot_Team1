Documentation     A sample file to interact with moja Printer.
...               created-by : Prasenjit Nandy

*** Settings ***
Library  SeleniumLibrary
Resource    ../../resource/keywords/common/printer/printPyRoboKeywords.robot

Force Tags      Printer

*** Test Cases ***
LoginTest
    initialize moja device      10.195.7.109
    press KEYCODE HOME
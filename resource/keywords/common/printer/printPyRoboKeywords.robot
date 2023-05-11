Documentation     A resource file with reusable keywords and variables.
...
...               Basic keywords for Printer interaction
*** Settings ***
Library     ../../../../library/printer/printPyRoboKeywords.py

*** Variables ***

*** Keywords ***
initialize moja device
     [Arguments]   ${printer_ip}
     initialize moja    ${printer_ip}

click using visible text in moja device
    [Arguments]   ${text_to_press}
    click using visible text in moja   ${text_to_press}

wait until text found in moja device
    [Arguments]   ${text}
    wait_until_text_found_in_moja    ${text}

press KEYCODE HOME
    [Arguments]
    press KEYCODE HOME in moja

press KEYCODE BACK
    [Arguments]
    press KEYCODE BACK in moja

wait until text id found in moja device
    [Arguments]   ${text_id}
    wait until text id found in moja   ${text_id}

click oppanel using text id in moja device
    [Arguments]    ${text_id}
    click_oppanel_using_text_id_in_moja    ${text_id}





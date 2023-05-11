*** Settings ***
Library     ../../../../library/desktop/winPyRoboKeywords.py
Library     ../../../../test/sample/invokeJavaMethods.py

*** Variables ***

*** Keywords ***
initialize windows session
    initialize windows automation
enter text
    [Arguments]   ${locator_strategy}   ${locator_value}   ${text_to_type}
    type     ${locator_strategy}    ${locator_value}    ${text_to_type}
click on
    [Arguments]   ${locator_strategy}   ${locator}
    click     ${locator_strategy}    ${locator}
wait for 10 sec
    wait


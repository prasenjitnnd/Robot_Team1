*** Settings ***
Resource    ../../resource/keywords/common/desktop/winPyRoboKeywords.robot


*** Variables ***
${locator_strategy_byname}         by.name
${locator_t&c}                     I agree to the license terms and conditions
${locator_install}                 Install
${locator_close}                   Close



*** Test Cases ***
Login To LPMC Dialogue
    initialize windows session
    click on       ${locator_strategy_byname}     ${locator_t&c}
    wait for 10 sec
    click on       ${locator_strategy_byname}     ${locator_t&c}
    wait for 10 sec
    click on        ${locator_strategy_byname}      ${locator_close}
    wait for 10 sec

*** Settings ***
Resource    ../../resource/keywords/common/desktop/winPyRoboKeywords.robot


*** Variables ***
${locator_username}                E-mail
${username}                        prasenjit.nandy@lexmark.com
${locator_next}                    Next
${locator_password}                Password
${password}                        P@ssw0rd
${locator_login}                   Log In
${locator_strategy_byname}         by.name

*** Test Cases ***
Login To LPMC Dialogue
    initialize windows session
    enter text      ${locator_strategy_byname}     ${locator_username}      ${username}
    wait for 10 sec
    click on        ${locator_strategy_byname}      ${locator_next}
    wait for 10 sec
    enter text      ${locator_strategy_byname}      ${locator_password}      ${password}
    wait for 10 sec
    click on        ${locator_strategy_byname}      ${locator_login}
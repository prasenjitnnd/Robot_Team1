# Pulled Resources from CPM test
*** Settings ***
Library  SeleniumLibrary
Variables    ../../objectrepo/locatorsCUI11.py
Variables    ../../global/variables/config.py

*** Variables ***
${loginyear}                    © 2021, Lexmark. All rights reserved.
${cpmyear}                      © 2021 Lexmark.
${next}                         Next
${login}                        Log In
${PORTAL TITLE}                 Lexmark Log In
${invalid_password_text}        Invalid password.
${invalid_user_text}            Invalid Username or Email.
${loginyear}                    © 2021, Lexmark. All rights reserved.
${cpmyear}                      © 2021 Lexmark.
${tab1name}                     Print Queue
${tab2name}                     Delegates
${tab3name}                     Print Job History
${tab4name}                     Download Print Management Client
${next}                         Next
${login}                        Log In
${id}
${job_name_actual}              defect_trend.jpg
${job_status_actual}            Ready
${job_color_actual}             Black and white
${job_duplex_actual}            On (long edge)
${job_nup_actual}               3
${job_copies_actual}            15
${default_title_actual}         Set Default Print Settings
${delete_dlg_title_actual}      Delete Print Jobs


*** Keywords ***

Open Browser To Login Page
    #check_chrome_webdriver
    Open Browser    ${URL}    ${BROWSER}

Maximise Browser
    Maximize Browser Window
    Title Should Be     Lexmark Log In

Check Copyright in Login
    Element Text Should Be      xpath:/html/body/div/div[2]/section/div[2]/div/p     ${loginyear}

Check Username field is enabled and displayed
    ${username_text}    set variable    id:user_email
    element should be enabled   ${username_text}
    element should be visible   ${username_text}
    ${password_text}    set variable    id:user_password
    element should not be visible   ${password_text}

Input Username
    [Arguments]    ${USER}
    Input Text    id:user_email    ${USER}

Verify Next Button is enabled and verify value
    ${nextbtn}  set variable    btn-email-next
    element should be enabled   ${nextbtn}
    element should be visible   ${nextbtn}
    #element attribute value should be   ${nextbtn}     value   ${next}

Click Next button
    Click Button    btn-email-next

Check Password field is enabled and displayed
    ${password_text}    set variable    id:user_password
    element should be enabled   ${password_text}
    element should be visible   ${password_text}

Input Password
    [Arguments]    ${PASSWORD}
    Input Text    id:user_password    ${PASSWORD}

Verify Login Button is enabled and verify value
    ${loginbtn}  set variable    btn-email-login
    element should be enabled   ${loginbtn}
    element should be visible   ${loginbtn}
    element attribute value should be   ${loginbtn}     value   ${login}

Click Login Button
    Click Button    btn-email-login
    Wait Until Keyword Succeeds    35 sec    5 sec    page should contain      Cloud Services Home




Open CPM Portal and Blank user name login verification

    [Arguments]    ${username_blank}
    set selenium timeout    20
    #check_chrome_webdriver
    Open Browser    ${URL}    ${BROWSER}
    wait until page contains    E-mail
    Maximize Browser Window
    Input Text    ${txt_username}   ${username_blank}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      ${btn_next}
    Click Button    ${btn_next}
    Wait Until Keyword Succeeds    35 sec    5 sec    page should contain element     ${lbl_errormessage}
    page should contain element     ${lbl_errormessage}
    element text should be      ${lbl_errormessage}      ${invalid_user_text}
    close browser

Open CPM Portal and Invalid user name login verification
    [Arguments]    ${username_invalid}
    set selenium timeout    20
    #check_chrome_webdriver
    Open Browser    ${URL}    ${BROWSER}
    wait until page contains    E-mail
    Maximize Browser Window
    Input Text    ${txt_username}   ${username_invalid}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      ${btn_next}
    Click Button    ${btn_next}
    Wait Until Keyword Succeeds    35 sec    5 sec    page should contain element      ${lbl_errormessage}
    page should contain element     ${lbl_errormessage}
    element text should be      ${lbl_errormessage}      ${invalid_user_text}
    close browser

Open CPM Portal and Blank password verification
    [Arguments]    ${username}      ${password_blank}
    set selenium timeout    20
    #check_chrome_webdriver
    Open Browser    ${URL}    ${BROWSER}
    wait until page contains    E-mail
    Maximize Browser Window
    Input Text    ${txt_username}   ${username}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      ${btn_next}
    Click Button    ${btn_next}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      ${txt_password}
    Input Text    ${txt_password}   ${password_blank}
    Click Button    ${btn_login}
    Wait Until Keyword Succeeds    35 sec    5 sec    page should contain element      ${lbl_errormessage}
    page should contain element     ${lbl_errormessage}
    element text should be      ${lbl_errormessage}      ${invalid_password_text}
    close browser

Open CPM Portal and Invalid password verification
    [Arguments]    ${username}      ${password_invalid}
    set selenium timeout    20
    #check_chrome_webdriver
    Open Browser    ${URL}    ${BROWSER}
    wait until page contains    E-mail
    Maximize Browser Window
    Input Text    ${txt_username}   ${username}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      ${btn_next}
    Click Button    ${btn_next}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      ${txt_password}
    Input Text    ${txt_password}   ${password_invalid}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      ${btn_login}
    Click Button    ${btn_login}
    Wait Until Keyword Succeeds    35 sec    5 sec    page should contain element      ${lbl_errormessage}
    page should contain element     ${lbl_errormessage}
    element text should be      ${lbl_errormessage}      ${invalid_password_text}
    close browser

Open CPM portal and Login Verification
    [Arguments]    ${username}      ${password}
    set selenium timeout    20
    #check_chrome_webdriver
    Open Browser    ${URL}    ${BROWSER}
    wait until page contains    E-mail
    Maximize Browser Window
    Title Should Be     ${PORTAL TITLE}
    Element Text Should Be      ${txt_lgnyear}     ${loginyear}
    element should be enabled   ${txt_username}
    element should be visible   ${txt_username}
    element should not be visible   ${txt_password}
    Input Text    ${txt_username}   ${username}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      ${btn_next}
    element should be enabled   ${btn_next}
    element should be visible   ${btn_next}
    #element attribute value should be   ${btn_next}     value   ${next}
    Click Button    ${btn_next}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      ${txt_password}
    element should be enabled   ${txt_password}
    element should be visible   ${txt_password}
    Input Text    ${txt_password}   ${password}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      ${btn_login}
    element should be enabled   ${btn_login}
    element should be visible   ${btn_login}
    element attribute value should be   ${btn_login}     value   ${login}
    Click Button    ${btn_login}


Dashboard Should Open
    set selenium timeout    20
    Wait Until Keyword Succeeds    35 sec    5 sec    page should contain      Cloud Services Home
    Title Should Be     Dashboard | Lexmark Cloud Services

Logout
    ${usermenu}     set variable    userMenu
    ${logout}       set variable    link-logout
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      userMenu
    click element   ${usermenu}
    Wait Until Keyword Succeeds    35 sec    5 sec    element should be visible      link-logout
    click element   ${logout}
    Wait Until Keyword Succeeds    35 sec    5 sec    title should be       Lexmark Log In
    close all browsers

# Pulled from Dashboard-UI test
Documentation     A resource file with reusable keywords and variables.
...
...               The system specific keywords created here form our own
...               domain specific language. They utilize keywords provided
...               by the imported Selenium2Library.

*** Settings ***
Library           SeleniumLibrary
Variables         ../../objectrepo/ISS_variables-COMPLETE.py
Variables         ../../global/variables/config.py

*** Variables ***
${spinner}    //*[contains(@id,'cui-busy-spinner')]/cui-image/img

*** Keywords ***
Open Browser To Landing Page
    Open Browser    ${URL}    ${BROWSER}
    Set Selenium Speed    ${SELENIUM_DEFAULT_DELAY}

Input Username
    #[Arguments]    ${username}
    Input Text    user_email    ${USER}
    Click Element     id=btn-email-next

Input Password
    [Arguments]    ${password}
    Input Text    user_password    ${PASSWORD}

Submit Credentials
    Click Element     id=btn-email-login

Landing Page Should Be Open
    Set Selenium Timeout     60
    Set Selenium Implicit Wait     5
    Wait For Condition     return document.title == "Dashboard | Lexmark Cloud Services"
    Title Should Be    Dashboard | Lexmark Cloud Services
    Wait Until Page Does Not Contain     Loading Dashboard...

Click Print Management Link
    Wait Until Page Contains     Dashboard | Lexmark Cloud Services
    Click Element    id=card-6
    Sleep     10s
    Wait Until Page Does Not Contain     Loading print queue...
    Switch Window    url=${PRINT_MANAGEMENT_URL}/#/printmanagement/printqueue/${ORG_ID}
    Wait Until Page Contains     Print Management | Lexmark Cloud Services
    Title Should Be    Print Management | Lexmark Cloud Services
    Close Window

Click Printer Configuration Link
    Switch Window    url=${URL}/#/overview
    Wait Until Page Contains     Dashboard | Lexmark Cloud Services
    Click Element    id=card-8
    Sleep     10s
    Switch Window    url=${PRINTER_CONFIG_URL}/#/accounts
    Wait Until Page Contains     Fleet Management | Lexmark Cloud Services
    Title Should Be    Fleet Management | Lexmark Cloud Services
    Close Window

Click User Accounts Link
    Switch Window    url=${URL}/#/overview
    Wait Until Page Contains     Dashboard | Lexmark Cloud Services
    Click Element    id=card-12
    Sleep     10s
    Switch Window    url=${USER_ACCOUNTS_URL_REDIRECT}
    Wait Until Page Contains     Account Management | Lexmark Cloud Services
    Title Should Be    Account Management | Lexmark Cloud Services
    Close Window

Click Reports Link
    Switch Window    url=${URL}/#/overview
    Wait Until Page Contains     Dashboard | Lexmark Cloud Services
    Click Element    id=card-10
    Sleep     10s
    Switch Window    url=${REPORTING_URL}
    Wait Until Page Contains     Analytics | Lexmark Cloud Services
    Title Should Be    Analytics | Lexmark Cloud Services
    Close Window

Click My Account Link
    Switch Window    url=${URL}/#/overview
    Wait Until Page Contains     Dashboard | Lexmark Cloud Services
    Scroll Element Into View     xpath=/html/body/lxk-dashboard-ui/div/cui-header/div/div/div/header/cui-header-user-menu
    Wait Until Page Contains Element     xpath=/html/body/lxk-dashboard-ui/div/cui-header/div/div/div/header/cui-header-user-menu
    Click Element    xpath=/html/body/lxk-dashboard-ui/div/cui-header/div/div/div/header/cui-header-user-menu
    Click Element    id=link-my-account
    Sleep     10s
    Switch Window     url=${MY_ACCOUNT_URL}/#/account
    Wait Until Page Contains     Personal Information
    Title Should Be    My Account | Lexmark Cloud Services
    Close Window

Click Help Link
    Switch Window    url=${URL}/#/overview
    Wait Until Page Contains     Dashboard | Lexmark Cloud Services
    Click Link    id=headerHelpLink
    Set Selenium Timeout    120
    Sleep     10s
    Switch Window    url=${FULL_HELP_URL}
    Wait Until Page Contains     Lexmark Cloud Services Information Center
    Title Should Be    Lexmark Cloud Services Information Center
    Close Window

Click Privacy Policy Link
    Set Selenium Timeout     60
    Switch Window    url=${URL}/#/overview
    Click Link    xpath=//a[@href="${PRIVACY_POLICY_URL}"]
    Switch Window    url=${PRIVACY_POLICY_URL_SECURE}
    Title Should Be    Privacy Notice | Lexmark United States
    Close Window

Click Terms of Use Link
    Switch Window    url=${URL}/#/overview
    Click Link    xpath=//a[@href="${TERMSOFUSE_URL}"]
    Switch Window    url=${TERMSOFUSE_URL}
    Close Window

Click Logout
    Switch Window    url=${URL}/#/overview
    Wait Until Page Contains Element     xpath=/html/body/lxk-dashboard-ui/div/cui-header/div/div/div/header/cui-header-user-menu/div/a
    Click Element    xpath=/html/body/lxk-dashboard-ui/div/cui-header/div/div/div/header/cui-header-user-menu/div/a
    Click Element    id=link-logout


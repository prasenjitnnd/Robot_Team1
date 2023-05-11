Documentation     A sample file with login-logout in application.
...               created-by : Prasenjit Nandy

*** Settings ***
Library  SeleniumLibrary
Resource    ../../resource/keywords/common/cloud_LoginLogout.robot

Force Tags      Login

*** Test Cases ***
LoginTest
    Open Browser To Login Page
    Maximise Browser
    Check Copyright in Login
    Check Username field is enabled and displayed
    Input Username      ${USER}
    Verify Next Button is enabled and verify value
    Click Next button
    Check Password field is enabled and displayed
    Input Password      ${PASSWORD}
    Verify Login Button is enabled and verify value
    Click Login Button
    Dashboard Should Open
    Logout


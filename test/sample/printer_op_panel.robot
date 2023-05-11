*** Settings ***
Documentation   UPS Sanity Test Script - 2-Line Panel
Library         CommonLibrary.keywords.UPS    ${PRINTER_IP}
Resource        pre-setup.robot
Test Setup	Pre-setup Printer Configuration

*** Test Cases ***
TOOLS-3269
    [Documentation]    Workflow
    UPS: Do "press key KEYCODE_HOME"
    #In area "list" On text "Copy" Do "h-select"
    #Do "press key KEY_Backspace"
    #Do "delay 2 seconds"
    UPS: In area "list" On text "Copy" Do "h-select"
    UPS: In area "list" On text "Copies" Do "h-select"
    UPS: Find widget "type='IntegerModel'" Do "verify value='1'"
    UPS: Find widget "type='IntegerModel'" Do "h-select:data_type=int:set value='50'"
    UPS: In area "list" On text "Copies" Do "h-select"
    UPS: Find widget "type='IntegerModel'" Do "verify value='50'"
    UPS: Find widget "type='IntegerModel'" Do "h-select:data_type=int:set value='1'"
    UPS: In area "list" On text "Copy from" Do "h-select"
    UPS: In area "list" On text "Letter (8.5 x 11 in.)" Do "verify selected='true'"
    UPS: In area "list" On text "Legal (8.5 x 14 in.)" Do "h-select"
    UPS: In area "list" On text "Copy from" Do "h-select"
    UPS: In area "list" On text "Legal (8.5 x 14 in.)" Do "verify selected='true'"
    UPS: In area "list" On text "Letter (8.5 x 11 in.)" Do "h-select"
    UPS: In area "list" On text "Copy from" Do "h-select"
    UPS: In area "list" On text "Letter (8.5 x 11 in.)" Do "verify selected='true'"
    UPS: Do "press key KEYCODE_HOME"

TOOLS-3270
    [Documentation]    Settings
    UPS: Do "press key KEYCODE_HOME"
    UPS: In area "list" On text "Settings" Do "h-select"
    UPS: In area "list" On text "Fax" Do "h-select"
    UPS: In area "list" On text "Fax Defaults" Do "h-select"
    UPS: In area "list" On text "Fax Setup" Do "h-select"
    UPS: In area "list" On text "General Fax Settings" Do "h-select"
    UPS: In area "list" On text "Fax Name" Do "h-select"
    UPS: In area "objects:index=2" Find widget "TextEntry" do "clear"
    UPS: In area "objects:index=2" Find widget "TextEntry" do "type 'MyFax101'"
    UPS: Do "press key KEY_Enter"
    UPS: Do "delay 5 seconds"
    UPS: In area "list" On text "Fax Name" Do "h-select"
    UPS: Find widget "type='TextEntry'" Do "verify text='MyFax101'"
    UPS: Do "press key KEYCODE_HOME"
    UPS: In area "list" On text "Settings" Do "h-select"
    UPS: In area "list" On text "Device" Do "h-select"
    UPS: In area "list" On text "Preferences" Do "h-select"
    UPS: In area "list" On text "Display Language" Do "h-select"
    UPS: In area "list" On text "English" Do "verify selected='true'"
    UPS: In area "list" On text "English" Do "h-select"
    UPS: Do "delay 5 seconds"
    UPS: Do "press key KEYCODE_HOME"

TOOLS-3271
    [Documentation]    Settings - Date and Time
    UPS: Do "press key KEYCODE_HOME"
    UPS: In area "list" On text "Settings" Do "h-select"
    UPS: In area "list" On text "Device" Do "h-select"
    UPS: In area "list" On text "Preferences" Do "h-select"
    UPS: In area "list" On text "Date and Time" Do "h-select"
    UPS: In area "list" On text "Configure" Do "h-select"
    UPS: In area "list" On text "Manually Set Date and Time" Do "h-select"
    UPS: Do "press key KEYCODE_1"
    UPS: Do "press key KEY_Right"
    UPS: Do "press key KEYCODE_3"
    UPS: Do "press key KEYCODE_1"
    UPS: Do "press key KEY_Right"
    UPS: Do "press key KEYCODE_2"
    UPS: Do "press key KEYCODE_0"
    UPS: Do "press key KEYCODE_1"
    UPS: Do "press key KEYCODE_9"
    UPS: Do "press key KEY_Enter"
    UPS: Do "delay 5 seconds"
    UPS: Do "press key KEYCODE_1"
    UPS: Do "press key KEY_Right"
    UPS: Do "press key KEYCODE_5"
    UPS: Do "press key KEYCODE_9"
    UPS: Do "press key KEY_Right"
    UPS: Do "press key KEY_Enter"
    UPS: Do "delay 5 seconds"
    UPS: Do "press key KEYCODE_HOME"

TOOLS-3272
    [Documentation]    Test wait_until_not_found
    UPS: Do "press key KEYCODE_HOME"
    UPS: In area "list" On text "Settings" Do "h-select"
    UPS: In area "list" On text "Copy" Do "h-select"
    UPS: In area "list" On text "Copy Defaults" Do "h-select"
    UPS: In area "list" On text "Collate" Do "h-select"
    UPS: In area "list" On text "On [1,2,1,2,1,2]" Do "h-select"
    UPS: On text "Submitting\\nchanges" Do "wait_until_not_found:max_sec=20"
    UPS: In area "list" On text "Content Type" Do "verify count=1"
    UPS: Do "press key KEYCODE_HOME"

TOOLS-3273
    [Documentation]    Test wait_until_found
    UPS: Do "press key KEYCODE_HOME"
    UPS: In area "list" On text "Settings" Do "h-select"
    UPS: In area "list" On text "Copy" Do "h-select"
    UPS: In area "list" On text "Copy Defaults" Do "h-select"
    UPS: In area "list" On text "Collate" Do "h-select"
    UPS: In area "list" On text "On [1,2,1,2,1,2]" Do "h-select"
    UPS: On text "Content Type" Do "wait_until_found"
    UPS: Do "press key KEYCODE_HOME"

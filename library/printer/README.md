#Instruction to setup Environment and develop automation tests for Printer Device Application

Setup environment in Printers
``````````````````````````````````````````````````````````````````````
    Make the Printer Dev Certified
    Deploy Printer Automation License using : https://cdp.lexmark.com/licensing-server/
    Search Locators in Printer op-pannel using : http://$IP/webservices/automation/data/panel.xml
``````````````````````````````````````````````````````````````````````

How to write Robot Keywords?
``````````````````````````````````````````````````````````````````````
    winPyRoboKeywords.py listed with base commands used to create kewords in Resource folder
    __init__.py initialize moja (using UPS py lib) and Non-Moja (using EACT java lin : not iplemented yet)
``````````````````````````````````````````````````````````````````````
UPS Documentation
    
    This is the official documentation of UPS.
    Here are the 3 ways to view it:
    1. From browser:
    http://web-fwtest.lrdc.lexmark.com/tools/ftl-tools/LettuceRunner_Steps/text/README_universal.txt
    2. From browser with user logged-in to gerrit account:
    http://gerrit.rds.lexmark.com/gitweb?p=lettuce-runner.git;a=blob;f=features/utils/README_universal.txt;hb=refs/heads/stable-incoming
    3. From lettuce-runner code repo using any text editor or browser:
    lettuce-runner/features/steps/panel/README_universal.txt

    Presentation Slides with Videos:
    https://docs.google.com/presentation/d/1PQlH5r9UgYEV2y-PXgNfYDzfTX-jzG6iHTIP4CHAfEo/edit#slide=id.g37437013a5_0_2

    Quick Examples:
    features/tests/ftl-tools-tests/sanity-steps-tests/universal-panel-step-android.feature
    features/tests/ftl-tools-tests/sanity-steps-tests/universal-panel-step-non-android-2.4.feature
    features/tests/ftl-tools-tests/sanity-steps-tests/sanity-android/universal-panel-steps.feature
    features/tests/ftl-tools-tests/sanity-steps-tests/sanity-2.4/universal-panel-steps-nontouch.feature
    features/tests/ftl-tools-tests/sanity-steps-tests/sanity-2Line/universal-panel-steps-2line.feature
    features/tests/ftl-tools-tests/sanity-steps-tests/sanity-2.8/universal-panel-steps-2.8.feature

    Code Repository of lettuce-runner:
    git clone ssh://<shortname>@gerrit.rds.lexmark.com:29418/lettuce-runner

    What is lettuce-runner?
    lettuce-runner is our Sentry3R test tool based on lettuce framework
    http://lettuce.it/index.html. Testing is done by running a feature file
    composed of different steps. A step is anything that performs something.
    For example:
    * Press button "<button-name>"
    * Verify that button "<button-name>" has state "<enabled|disabled>"
    * Verify that textview "<textview-name>" has value "<expected-text-value>"
    Universal Panel Step (UPS) is just one of the many steps in lettuce-runner.
    It is special because it replaces all existing steps about panel testing
    (both navigation and verification). It is fast and very efficient. It is
    generic by design and requires less maintenance. See presentation slides
    for an outline of its advantages over the old steps. Any old panel step can
    be expressed and converted to UPS. Our goal is to convert all old steps in
    hundreds of feature files used for testing. That is a big task. So we start
    first by replacing all old panel steps that are causing intermittent
    failures or are very slow.

    How is it possible to automate panel testing?
    Firmware UI has provided an automation framework so that we can do this. Of
    course that is disabled by default. It can be enabled by using a special
    license. Once enabled, we can use it. The automation framework provides 2
    things. First it exposes to us what is on the panel screen through the
    panel.xml accessble via:
        http://$IP/webservices/automation/data/panel.xml
    Second, it provides webservices that allow us to do things such a pressing
    a widget, swiping, and entering text on the screen:
        http://$IP/webservices/automation/request/swipe?x0={}&x1={}&y0={}&y1={}&t={}
        http://$IP/webservices/automation/request/touchAndRelease?x={}&y={}
        http://$IP/webservices/automation/request/pressAndReleaseKey?key={}
        http://$IP/webservices/automation/request/enterText?text={}
    Here is the link to the firmware UI panel automation framework:
    https://twiki.lpdev.prtdev.lexmark.com/bin/view/UI/GuiAutomationWebServices

    UPS Technical Declaration:
    @step('(|In area "([^"]*)" )(|On text "([^"]*)" )(|Find widget "([^"]*)" )(Do "([^"]*)")')
    def find_widget_and_do_action(step, area_phrase, areanode_whereclause, \
                                        text_phrase, textnode_whereclause, \
                                        widget_phrase, widgetnode_whereclause, \
                                        action_phrase, action)

    What are these UPS Parameters?
    As noted above, UPS has 4 inputs or parameters. The goal of a UPS is to
    locate a widget (TextView, Button, etc.) and perform an action on it. The
    on-text phrase and find-widget phrase allow you to specify the text or
    other attributes of your widget. You have to use either one or both. The
    in-area phrase provides scrolling support when you need it. So it is
    optional. The action phrase is always mandatory. That is what you will do
    after you find your target widget. However there are actions that do not
    need a widget such as "press key <key-code>". These actions are not
    associated with any widget and so you can use them independently without
    any on-text or find-widget phrase.

    UPS Rules In Different Panel Sizes
    Athough UPS syntax is the same across different panel sizes, there are
    are differences in rules and semantics. Some specifiers or actions are
    specific only to certain panel sizes. Below is the link to the matrix.
    https://docs.google.com/spreadsheets/d/1n6vs-uHnLo0400v_VTzzXcbzuFf_O0vbYWvUW-gTMMA/edit#gid=0

    Questions? Requests for Additional Features?
    Send an email to cebu_ftl_tools_scrum@lexmark.com.

    Patches and Contributions
    If you are planning to contribute to UPS, please do not edit the code and
    post a review. Any change to UPS should be done in consultation with the
    tools team. UPS follows a very strict design to maintain its generic nature
    and consistent wording (syntax) and meaning (semantics) across all panel
    sizes. Also different teams and projects are using UPS. We would like to
    avoid breakage and most esp inconsistency which is usually not easily
    detectable. If you find something you need not found in UPS, most likely
    there is a reason why aside from no time to implement it.

    Documentation Sections:
    This documentation is divided into 2 sections. Each section will discuss
    how each UPS parameter is used in their respective domains.
    1. Android Panels
    2. Non-Android Panels
       __    _  _  ____  ____  _____  ____  ____     ____   __    _  _  ____  __    ___
      /__\  ( \( )(  _ \(  _ \(  _  )(_  _)(  _ \   (  _ \ /__\  ( \( )( ___)(  )  / __)
     /(__)\  )  (  )(_) ))   / )(_)(  _)(_  )(_) )   )___//(__)\  )  (  )__)  )(__ \__ \
    (__)(__)(_)\_)(____/(_)\_)(_____)(____)(____/   (__) (__)(__)(_)\_)(____)(____)(___/


    For 10", 7", 4.3" android panels, and any panel as long as it follows the
    same panel.xml design.

    This section is divided into 4 parts, each a parameter of UPS.
    1. In-area Phrase
    2. On-text Phrase
    3. Find-widget Phrase
    4. Action Phrase

    In-area Phrase
        * Format: In area <area-name>[:<specifier>=<value>]
        * Purpose 1: Performs auto-scroll if area is scrollable
        * Purpose 2: Narrows down the search area for finding the widget
        * Specifiers:
          * :index=<1-9>
          * :force_scroll=true
          * :swipe_offsetx=<value>
          * :swipe_offsety0=<value>
          * :swipe_offsety1=<value>
          There can be one or more specifiers which can be specified
          one after the other. The purpose of specifiers is to allow for
          special behavior by overriding default values.
        * Examples:
          * In area "ViewPager" On text "Settings" Do "press"
          * In area "android:id/list" On text "Device" Do "nothing"
          * In area "ExpandableListView" On text "Visible Home Screen Icons" Do "nothing"
          * In area "EditText:index=1:force_scroll=true" On text "Dec" Do "press"

        * Purpose 1: To Automatically Scroll
          Specify in-area phrase if your widget is not guaranteed to be visible
          without scrolling first.

        * Purpose 2: To Narrow Down Search Area
          The area-name is usually the scroll node but it can be any other node
          esp when you want to narrow down the search area because you want to
          use your favorite resource-id or class attribute that is non-unique.
          It may not be globally unique but it is unique in the area you
          specified.

        * How do you know from panel.xml what are scroll nodes?
          Navigate the panel to the intended screen then open in browser:
          http://$IP/webservices/automation/data/panel.xml.
          Search for <scrollable="true">. Child nodes under each scroll node
          have <text="*"> attribute containing text displayed on the panel.
          Those texts are your breadcrumbs that lead to your scroll node.

        * What is the purpose of :index specifier?
          That is for the case when there are multiple matches for your
          area phrase that can't be resolved to be unique using any
          combination of its attributes. So the only way is for you
          to identify which match you want is to provide an index.

        * What is the purpose of :force_scroll specifier?
          Forced scroll is for scrolling areas not really scrollable
          as indicated in panel.xml. This is particularly helpful for
          setting date/time picker widgets.
          Examples:
          * In area "EditText:index=1:force_scroll=true" On text "Dec" Do "press"
          * In area "EditText:index=2:force_scroll=true" On text "31" Do "press"
          * In area "EditText:index=3:force_scroll=true" On text "2016" Do "press"
          * In area "EditText:index=4:force_scroll=true" On text "01" Do "press"
          * In area "EditText:index=5:force_scroll=true" On text "59" Do "press"

        * What is the purpose of :swipe_nn specifier?
          That is for flexibility of the swiping. By default swiping is done
          at rightmost part of the scroll area. Notice that sometimes rows have
          widgets that are towards that rightmost edge. These are edit settings
          buttons, etc. Although it has not yet been reported, there may be
          times that swiping will not happen on that x coordinate. Why? Because
          it may unintentionally click the rightmost widget instead of swiping.
          No swiping occurs but you will see the effect of a button click event
          instead, for example the settings page shows instead of scrolling to
          the next pane. No report has been made yet, but just in case that
          happens, we want the user to have the option to transfer the swiping
          x coordinate to the leftmost x or any point x in the scroll area.

          swipe_offsetx = -1 (rightmost x-1) the default if not specified
          swipe_offsetx = -2 (rightmost x-2)
          swipe_offsetx = -3 (rightmost x-3) and so on ...
          swipe_offsetx =  0 (leftmost  x+0)
          swipe_offsetx =  1 (leftmost  x+1)
          swipe_offsetx =  2 (leftmost  x+2)
          swipe_offsetx =  3 (leftmost  x+3) and so on ...

          Why are we talking about rightmost x-1 instead of rightmost x alone?
          Good question. Rightmost x won't work. Maybe bec it's where the blue
          thin line scrollbar is located? We use 1 pixel prior to it. So our
          starting point for rightmost is rightmost x-1. That is to say,
          specifying swipe_offsetx=-1 is the same as not specifying it at all.

          Tip:
          If rightmost x-1 doesn't work (the default), maybe leftmost x will.
          So the tip is first to use n=0 before you try any other value.
          Example:
          In area "esf.ssaUi:id/lvDestinationPanel:swipe_offsetx=0"

          If no issue has been reported yet, why are you providing this
          swipe_offsetx workaround? You really have good questions! Originally
          the default swiping x coordinate is the leftmost x. So originally the
          workaround was written for transferring it to rightmost x-1. Now we
          are doing the exact opposite. If the new default of using the
          rightmost x-1 will prove to be perfect, we may need to remove this
          swipe_offsetx specifier support.

          UPDATE: swipe_offsetx is now disabled. You can't use it. We will
          reenable it only when the need arises.

        * What is the purpose of :swipe_offsety0 and :swipe_offsety1 specifier?

                          |                            |
            +--------------------------------------------------+
            | Android     |                            |       |
            |             |                            |       |   y0 = -1
          -------------------------------------------------------- y0 = 0 (default)
            |             | swipe area              |  |       |   y0 = +1
            |             |                         |  |       |
            |             | bounds=[x0,y0][x1,y1]   |  |       |
            |             |                         |  |       |
            |             |                         V  |       |   y1 = -1 (default)
          -------------------------------------------------------- y1 = 0
            |             |                            |       |   y1 = +1
            |             |                            |       |
            +--------------------------------------------------+
                          |                            |
                          x0                           x1

          By default, UPS Android uses the following coordinates to vertically
          swipe:

          * x_adjusted = x1 + (-1)
            Meaning UPS Android is always vertically swiping at the right side
            of the 'swipable' area; the offset of one pixel less than x1 (-1)
            is constant.

          * y0_adjusted = y0 + swipe_offsety0
            swipe_offsety0 is set using the specifier :swipe_offsety0=([+-]?\d+)
            and the variable swipe_offsety0 can be either positive or negative.
            Default value is zero (0). Apparently in most cases, the value for
            swipe_offsety0 will be positive to stay in the 'swipable' area.

          * y1_adjusted = y1 + swipe_offsety1
            swipe_offsety1 is set using the specifier :swipe_offsety1=([+-]?\d+)
            and the variable swipe_offsety1 can be either positive or negative.
            Default value is negative one (-1). Apparently in most cases, the
            value for swipe_offsety1 will be negative to stay in the 'swipable'
            area.

          The default offset value for y1_adjusted is negative one (-1) because
          no adjustment or offset will not work on all cases.

          This specifier is used when the default offsets zero (0) and negative
          (-1), for coordinates y0 and y1 respectively, does not work.

          Example:
          In area "android.widget.ListView:swipe_offsety0=1" on text "Delete" do "press"
          In area "android.widget.ListView:swipe_offsety1=-2" on text "Delete" do "press"
          In area "android.widget.ListView:swipe_offsety0=1:swipe_offsety1=-2" on text "Delete" do "press"

        * How do you swipe in home screen?
          Home screen is quite unique in a few ways. First it is swiped
          horizontally and secondly it is constantly changing -- at least the
          top menu bar -- due to constant flashing of the IP address or the
          IRs, etc. So detecting whether the screen changes or not (for
          determining if we can still swipe forward or not) was a challenge.
          Thankfully that has been resolved by excluding the top menu bar node
          in the comparison. Hence, home swiping operates like any other
          swiping, i.e., with the use of in-area phrase.

          Example:
          In area "ViewPager" on text "MySpecialApp" Do "press"

          Just like any other swiping, if it can't find your node on the screen
          it swipes forward to the end. Then it will attempt to swipe backward
          fast to the starting position before it swipes a little slower to
          search again in previously unsearched panes. Indeed, it will give up
          only if it has exhausted the swipe gestures forward and backward.

        * Possible values of area-name:
          * class attribute - use its exact text or substring
            Examples:
            * android.support.v4.view.ViewPager or ViewPager (Home Screen Scroll)
            * android.widget.ListView or ListView (Admin Settings Main Scroll)
            * android.widget.ExpandableListView or ExpandableListView (Admin Settings Sub Scroll)
            * android.support.v7.widget.RecyclerView or RecyclerView (Workflow Main Scroll)
            * android.widget.ScrollView or ScrollView (Workflow Sub Scroll)
            * android.widget.ListView or ListView (Scan Center Main & Sub Scrolls, scrollable in 4.3 panel)

            Brevity should be preferred. Shorter names make the step readable.
            So a substring like ViewPager (not android.support.v4.view.ViewPager)
            should be used when indicating class attribute.

            Please note that you can't use "viewpager" or "ViEwPaGeR".
            To make xpath run a little faster, I chose to not to do a case
            insensitive search. This applies to all rules in this universal
            panel step.

            What is the disadvantage of using class attribute?
            It is searched as substring. To illustrate, if your screen has
            ListView and ExpandableListView, then using ListView returns 2
            matches. You can use ExpandableListView since it is unique. But
            when you refer to the ListView, you should use its resource-id.
            See next section below.

          * resource-id attribute - use its exact text
            Examples:
            * com.lxk.home:id/pager (Home Screen Scroll)
            * android:id/list (Admin Settings Main Scroll)
            * com.lxk.adminSettings:id/menu_expandablelist (Admin Settings Sub Scroll)
            * com.lxk.workflow:id/recyclerlist (Workflow Main Scroll)
            * com.lxk.workflow:id/scroller (Workflow Sub Scroll)
            * esf.ssaUi:id/lvNavigationPanel (Scan Center Main Scroll, scrollable in 4.3 panel)
            * esf.ssaUi:id/lvDestinationPanel (Scan Center Sub Scroll for destinations)

            Your first option should be using class attribute. When that
            doesn't work because you get "multiple matches" error, then use
            the resource-id.

            Why is life so hard, you ask? Why can't I just specify a text from
            the panel for scrolls? Well ... baby, there's none. Maybe today is
            just your unlucky day. =)

          * any single or combination of exact text from any one or multiple
            attributes. (Not recommended since this makes the step not
            readable.)
            Examples:
            * "resource-id='value1'"
            * "resource-id='value1'&&class='value2'"
            * "resource-id='value1'&&class='value2'&&another-attribute='value3'"

            A good combination is that of resource-id and class attributes.
            There is a good chance that that combination makes a unique pair.
            Take for example your idol Taylor Swift. There are too Taylor
            Swifts including males. But there's only one in the world that
            captured your heart born 13 Dec 1989. =)

        * What do I use if resource-id and class attribute are both unique?
          You are not listening! You should prefer class attribute (the
          substring, not the full string) because it's almost always much
          shorter than resource-id.

        * Should I generally avoid using an in-area phrase?
          Yes, unless you need to do auto-scroll (and that other "narrow search
          area" purpose mentioned above). But there is a 3rd case where it is
          useful. When you want to do non-existence testing. For example, you
          want to make sure a deleted value no longer exists in a list:
          In area "ListView" on text "MyDeletedValue" find widget "TextView" Do "verify none such exists"

        * If I should generally avoid in-area phrase, then why are you writing
          this very verbose guide for it?
          Good question! When you read on below on find-widget phrase, it
          refers to this section. Yep, they share the same list of possible
          values: class attribute, resouce-id attribute and any one or more
          combination of attributes.

        * I really like in-area phrase. I want to use it all the time.
          Maybe you just forgot to take your medicines this morning.

        * I still have more questions, who do I call?
          Ghostbusters? x8680 or better cebu_ftl_tools_scrum@lexmark.com.

    On-text Phrase
        * Format: On text "<text>"
        * Purpose: For specifiying a text widget by using its text as it
          appears on the screen. This is an optional phrase that allows you to
          specify a screen text nearest to your widget. This also effectively
          narrows down the search area for the widget.
        * Algorithm: The search starts from the node which has this text
          (itself and its decendants) and move all the way up to root of the
          xml or the enclosing area node you specified via in-area phrase.

        * Most Preferred Usage of This Universal Panel Step:
          Always provide a on-text phrase as much as possible. Because the text
          you are using is from the screen, the step reads very natural. Below
          is the most straightforward usage of this step:

          On text "x" Do "y"      <-- the neatest thing in the house

          Always try that one before trying any variations of this universal
          panel step. Pressing the widget or the text beside the widget has the
          same effect or at least that is the expected behavior. So most of the
          time you don't really have to worry whether it's a button,
          radiobutton, checkbox, etc. You just have to refer to the text beside
          it anyway. This simplifies life a lot.

        * How is single quote or double quote inputted?
          We are using the standard xml escape character method:
          * Single quote is inputted as &apos; (yep apos for apostrophe)
          * Double quote is inputted as &quot;
          Example:
          The steps below are incorrect:
              On text "Gian's Fax" Do "press"
              On text "Gian said "Hi"" Do "press"
          To correct:
              On text "Gian&apos;s Fax" Do "press"
              On text "Gian said &quot;Hi&quot;" Do "press"
          These rules apply to all phrases: in-area, on-text, find-widget, and
          action phrases. Only action phrase supports both escaped single and
          double quote being present at the same time, the rest do not. They
          only support either one. This is due to xpath limitation. If you have
          such need, only then will we add support upon request.
          Example:
          This action is incorrect:
              Find widget "TextView" Do "verify text='Gian's Fax says "Hi"'"
          To correct:
              Find widget "TextView" Do "verify text='Gian&apos;s Fax says &quot;Hi&quot;'"

    Find-widget Phrase
        * Format: Find widget "<widget-name>"
        * Widget-name follows the same set of possible values as that of
          in-area phrase except that instead of area-names, we are using
          widget-names like TextView, Button, RadioButton, Spinner, EditText,
          etc.
        * Specifiers: Unlike in-area phrase, find-widget phrase does not
          have specifiers.

    Action Phrase
        * Format: Do "<action>"
        * Purpose: To perform an action.
        * Action can be any of the following:

          "press"
             Most panel steps only involve press, almost all. Whether it's
             clicking a button, checking/selecting a CheckBox or RadioButton
             or ToggleButton, it's all press! For checkable/selectable widgets,
             pressing reverses the current value so you have to know the
             current value first. So for such widgets, you should use action
             "set <checked|selected>='<true|false>'"

          "press:offsetx=<x>:offsety=<y>"
             Sometimes there are elements on screen that are not in the xml.
             You can't possibly press them bec you can find their widget nodes!
             A workaround is to use the nearest widget that is in the xml and
             then use pressing by offset, either by x-axis or y-axis or both.
             These offsets are integers (i.e., can be positive or negative).
             Examples:
             * On text "MyXMLVisibleText" Do "press:offsetx=50"
             * On text "MyXMLVisibleText" Do "press:offsety=-100"
             * On text "MyXMLVisibleText" Do "press:offsetx=50:offsety=-100"

          "press:time_sec=<n>"
             This imitates a long press for n seconds. This can be
             used with specifiers "press:offsetx=<x>:offsety=<y>". This
             executes a single long press.

             Currently for UPS Android, this does not have a known use case.

          "nothing"
             Why would you find a widget and do nothing with it?
             Maybe you just want to expose the widget to view (e.g., widgets in
             the middle/bottom of a long ListView) and so confirm if it's
             really there or you do something complicated after it.

          "verify none such exists"
             This is useful for non-existence testing as mentioned earlier.
             For example, you want to make sure a deleted value no longer
             exists in a list or simply verifying that a specific widget should
             not be there.
             Examples:
             * In area "ListView" on text "My Deleted Value" find widget "TextView" Do "verify none such exists"
               Here, auto-scroll is performed since you specified in-area
               phrase. It scrolls the whole area before giving up.
             * On text "My Deleted Value" find widget "TextView" Do "verify none such exists"
             * On text "My Deleted Value" Do "verify none such exists"

          "delay <n> seconds"
             WARNING: This will be deprecated (aka removed) soon.
             Instead of hard delay please always use the conditional wait
             actions "wait_until_found" or "wait_until_not_found".

          "wait_until_found"
             This is useful for apps team where apps like Scan Center loads at
             an indeterminate amount of time. This will attempt to find the
             widget every 5 seconds for a max of n seconds specified in the
             screen timeout set in the device. Beyond that, an error will be
             flagged. You can't use the in-area phrase in conjuction with this
             wait action, only the on-text and find-widget phrases.
             Example:
             On text "MyHintText" Do "wait_until_found"

          "wait_until_not_found:max_sec=<n>"
             Use this wait when the device is busy and will not start the
             screen timeout clock. Examples are when device is scanning,
             printing, sending. You need to specify a reasonable max value of
             wait in seconds, a value carefully considered from your previous
             multiple test runs. Again here, you can't use the in-area phrase
             in conjuction with this wait action, only the on-text and
             find-widget phrases.
             Example:
             On text "Scanning" Do "wait_until_not_found:max_sec=5"

          "press key <key-code>"
             This is an independent action (no on-text/find-widget phrase).
             NOTE: APPLIES TO ANDROID and NON-ANDROID PANELS
             Press the specified key. There is no internal mapping for your
             convenience. Yep, sorry. So instead of HOME, you use KEYCODE_HOME.
             Instead of BACK, KEYCODE_BACK.
             KEYCODE_ESCAPE
             KEYCODE_CLEAR
             KEYCODE_MOVE_END
             KEYCODE_DEL
             KEY_Enter
             KEY_Cancel
             KEY_Backspace
             KEYCODE_STAR
             KEYCODE_4
             KEYCODE_1
             This is very generic so please refer to the Firmware UI Automation
             Framework link listed at the top of this document for a complete
             reference. Hardkeys and keyboard keys apply.

          "type '<text>'"
             This CAN be an independent action (no on-text/find-widget phrase).
             NOTE: APPLIES TO ANDROID and NON-ANDROID PANELS
             You want to type on the keyboard after finding the widget. This is
             applicable to EditText widget, for example.
             * On Android Panel:
                Tested on 4.3" HW typing 512 characters (Email To: Recipient).
                For very long strings make sure you add a wait action using
                "wait_until_found" after your step since it takes time for the
                UI to process it.
                Example:
                Find widget "text='MyCompleteVeryLongText'" Do "wait_until_found"
             * On 2.4" Panel:
                Tested on sim typing 512 characters (Email Default Message).
                No need for wait since typing is accomplished on
                a per character basis (blocking) unlike in android
                which is sent as a complete string (non-blocking).
                Special note: If a text field is empty, it's not in the xml!
                So what you do is to use type as an independent action.
                That is, do not prepend with "Find widget 'EditBox'", for
                example. This begs the question, why not use type as
                independent action all the time? Yes, you can do that as long
                as there is only one text field on screen, which seems to be
                the case for 2.4".

          "clear"
             NOTE: APPLIES TO ANDROID and NON-ANDROID PANELS
             You want to clear the contents of a input text widget after
             finding it. This is applicable to EditText widget, for example.
             * On Android Panel:
                Tested on 4.3" HW deleting 512 characters (Email To: Recipient).
                For very long strings make sure you add a wait action using
                "wait_until_found" after your step since it takes time for the
                UI to process it. Deleting can only be done on a per character
                basis which makes it slow.
                Example:
                Find widget "resource-id='MyResourceID'&&text=''" Do "wait_until_found"
             * On 2.4" Panel:
                Tested on sim deleting 512 characters (Email Default Message).
                Clearing entire text is done via pressing backspace key only
                once. It is cleared immediately. No wait at all. Manual clear
                (i.e. on per character basis) is not implemented since it is
                not used in testing. The case is always to clear a text field
                first then type the desired text.

          "verify <attribute-name>='<attribute-value>'"
             NOTE: APPLIES TO ANDROID and NON-ANDROID PANELS
             This is useful for verifying widget's text value or if widget
             is enabled, radiobutton is checked, or widget is selected, and any
             other attribute whose value you want to check:
             Examples:
             * verify text='Letter (8.5 x 11 in.)'
             * verify enabled='true'
             * verify checked='false'
             * verify selected='true'

          "set <checked|selected>='<true|false>'"
             This is useful for conditional pressing on checkable/selectable
             widgets.
             Examples:
             * set checked='true'
               will press the widget only if current value is
               checked=false to change its value to true
             * set selected='false'
               will press the widget only if current value is
               selected=true to change its value to false
             You should make sure you are using the right attribute "checked"
             or "selected" since both exist in every widget. Only one of the
             two will work. Avoid guessing by checking both false and true
             values prior to cementing that step into your feature file.

          "set seekbar='<n>':widget='<resource-id>'"
             This is useful for setting the value of a seekbar. The resource-id
             is that of the TextView which contains the value of the seekbar.
             Because setting the seekbar requires checking 2 widgets (namely
             the SeekBar widget and its TextView), you usually need to specify
             an in-area phrase to narrow down the search. This is because the
             resource-id is not guaranteed to be unique esp in seekbar-related
             widgets.

             Examples:
             * In area "com.lxk.workflow:id/darkness_seekbar" find widget "SeekBar" Do "set seekbar='-4':widget='com.lxk.workflow:id/value'"
             * In area "com.lxk.workflow:id/shadow_detail_control" find widget "SeekBar" Do "set seekbar='-4':widget='com.lxk.workflow:id/value'"
             * In area "com.lxk.workflow:id/background_removal_control" find widget "SeekBar" Do "set seekbar='1':widget='com.lxk.workflow:id/value'"
             * In area "com.lxk.workflow:id/sharpness_control" find widget "SeekBar" Do "set seekbar='5':widget='com.lxk.workflow:id/value'"
             * In area "com.lxk.workflow:id/contrast_control" find widget "SeekBar" Do "set seekbar='3':widget='com.lxk.workflow:id/value'"
             * In area "com.lxk.workflow:id/red_balance_control" find widget "SeekBar" Do "set seekbar='-2':widget='com.lxk.workflow:id/value'"
             * In area "com.lxk.workflow:id/green_balance_control" find widget "SeekBar" Do "set seekbar='-1':widget='com.lxk.workflow:id/value'"
             * In area "com.lxk.workflow:id/blue_balance_control" find widget "SeekBar" Do "set seekbar='0':widget='com.lxk.workflow:id/value'"
             * In area "com.lxk.workflow:id/temperature_control" find widget "SeekBar" Do "set seekbar='1':widget='com.lxk.workflow:id/value'"
             * In area "com.lxk.workflow:id/jpeg_quality_container" find widget "SeekBar" Do "set seekbar='71':widget='com.lxk.workflow:id/value'"
             * In area "com.lxk.adminSettings:id/FtpShadowDetail" find widget "SeekBar" Do "set seekbar='2':widget='com.lxk.adminSettings:id/slider_value'"
             * In area "com.lxk.adminSettings:id/FtpSharpness" find widget "SeekBar" Do "set seekbar='3':widget='com.lxk.adminSettings:id/slider_value'"
             * In area "com.lxk.adminSettings:id/FtpTemperature" find widget "SeekBar" Do "set seekbar='4':widget='com.lxk.adminSettings:id/slider_value'"

             Algorithm Note on Seekbar Value Setting:
             Seekbar setting is the slowest action in this universal step. This
             is because it is being set blindly. Not all seekbars have min/max
             range specified in the xml. So the most generic thing to do is to
             do a binary search to get the right value. This means the seekbar
             value is set a few times before it is set aright. If the effective
             domain of values is 100 (e.g. 1-100), there are at most 7 tries to
             set it correctly. That is not too bad though. An average speed of
             setting a seekbar is usually around 10 seconds or less.

    General Examples:

        * Simple Press

          If your action is simply to press then you should try to use
          on-text phrase. With emphasis on "alone", it being your only step
          condition. That is the shortest variant of this universal step.
          Avoid the temptation to add <Find widget "TextView"> since
          TextView is the default class attribute assumed by the step.

          Examples:
          * On text "Settings" Do "press"
          * On text "Preferences" Do "press"
          * On text "Display Language" Do "press"
          * On text "Auto" Do "press"

          When that doesn't work because you get a "multiple matches" error
          only then should you use the find-widget phrase or the in-area
          phrase.

          Example:
          In area "android:id/list" on text "Device" Do "press"

        * Typing a Text

          When your action is other than press, you need to locate the
          correct node (not its accompanying nearby text node) to perform
          the action. Hence you usually need to use the find-widget phrase.

          Example:
          On text "To:" find widget "EditText" Do "type 'gilopez@lexmark.com'"

        * Verifying a Value

          If your action is to verify an attribute value, then most likely you
          need to use the find-widget phrase.

          When your action is to verify text value <Do "verify text='ABC'">
          your target node is usually another TextView. I told you earlier
          you should avoid <Find widget "TextView"> since that is redundant.
          But here it's needed because you mean a different TextView other than
          the accompanying TextView beside it in the on-text phrase. If class
          attribute TextView doesn't work, you should try resource-id attribute
          as illustrated below.

          Examples:
          * On text "Display Language" find widget "TextView" Do "verify text='English'"
            Here we are using class attribute and it locates an incorrect node.
            We know it's incorrect because when <Do "verify attribute='value'">
            action fails the error message will also display the matching
            node's full attribute list. So from the error message, we discover,
            there are more than 1 TextView nodes near "Display Language" text
            node.

          * On text "Display Language" find widget "com.lxk.adminSettings:id/textview_item" Do "verify text='English'"
            Now you hit the nail right on the head when you used resource-id
            attribute.

        * No Nearby Text

          If there is no nearby text or when the nearby text is a dynamic text
          that changes (e.g. on to off) depending on the setting then most
          likely you need to use the find-widget phrase alone. Again with
          emphasis on "alone", it being your only step condition.
          Example:
          Find widget "com.lxk.workflow:id/paper_saver_switch" Do "verify checked='false'"

        * Overkill Usage

          These are not recommended. Maybe you should spend your extra time
          investing in bitcoin.

          These examples are too wordy. You should have found out a simpler
          shorter version. This happens when you don't try the simple variants
          first.
          Examples:
          * In area "com.lxk.adminSettings:id/menu_expandablelist" on text "Display Language" find widget "com.lxk.adminSettings:id/textview_item" Do "verify text='English'"
            Here in-area phrase is not needed since the on-text phrase already
            returns 1 match.
          * In area "resource-id='com.lxk.adminSettings:id/menu_expandablelist'&&class='android.widget.ExpandableListView'" on text "Display Language" find widget "com.lxk.adminSettings:id/textview_item" Do "verify text='English'"
            Here in-area phrase is not needed, much less multiple conditions on
            it.
          * In area "com.lxk.adminSettings:id/menu_expandablelist" on text "Display Language" find widget "resource-id='com.lxk.adminSettings:id/textview_item'&&class='android.widget.TextView'" Do "verify text='English'"
            Here find-widget phrase uses multiple conditions which is
            unnecessary.

        * Recommended for Workflows and Apps to Select Multiple Destinations Fast

          In area "esf.ssaUi:id/lvDestinationPanel" on text "<display-name>" Do "press"
          You can't use ListView since there are 2 of them!
          UPDATE: With the addition :index specifier to in-area phrase you can
          now use ListView.
          In area "ListView:index=2" on text "<display-name>" Do "press"

        * Cases When Redundancy is Sometimes Preferred

          Sometimes the step is not understandable without the accompanying
          on-text phrase. This happens when the widget has no text beside it.
          So for readability you might want to include the nearest header text
          instead.
          Examples:
          * On text "EDGE HANDLING" find widget "esf.ssaUi:id/btnTop" Do "press"
          * On text "EDGE HANDLING" find widget "esf.ssaUi:id/btnBottom" Do "press"
          * On text "EDGE HANDLING" find widget "esf.ssaUi:id/btnPlus" Do "press"
          * On text "EDGE HANDLING" find widget "esf.ssaUi:id/btnMinus" Do "press"
          Here the steps would have worked just fine without the on-text phrase.

        * A Sample Test Creation Case Determining the Best Step Variant to Use

          You want to check the state of the toggle button for Copy Workflow on
          "Pages per Side" view. You try the most simple intuitive step:

          On text "Off" find widget "ToggleButton" Do "verify checked='false'"

          Now you receive this error: "More than 1 matching text nodes found. Count = <3>."
          Yes, 3 widgets also have that exact text! So you decide to just drop
          the on-text phrase and immediately use a nerdy version that you are
          very sure will work at 99% =)

          Find widget "resource-id='com.lxk.workflow:id/paper_saver_switch'&&class='android.widget.ToggleButton'" Do "verify checked='false'"

          Now the step passes and you are happy! No you should not be, that is
          too cryptic! So your good conscience tells you to make it less
          cryptic and you use:

          Find widget "com.lxk.workflow:id/paper_saver_switch" Do "verify checked='false'"

          That worked too! And that is a better choice. Note that "Off" is not
          a fixed text. It turns to "On" on the next toggle. So it is not wise
          to actually use it in the on-text phrase, even if the on-text phrase
          option worked.

        * A Helpful Tip on Short Panel Texts

          Sometimes the text on the panel (OFF) is not the same as in the
          xml (Off). This maybe because what you see on the panel is an image
          not a text. Should you use the on-text phrase, always use the one in
          the xml. Another case is in Scan Center color setting: panel is AUTO,
          xml is Auto.

        * How To Make Your Life Miserable (A Step by Step Guide)

          1. Make yourself attractive.
             On text "x" Do "y"
          2. Doubt your identity and self-worth.
             On text "x" find widget "z" Do "y"
          3. Share your misery with others.
             In area "w" on text "x" find widget "z" Do "y"
          4. Finally be a suicide bomber.
             In area "attrib1='a'&&attrib2='b'" on text "x" find widget "attrib1='c'&&attrib2='d'&&attrib3='e'" Do "y"

          For this case you found out that no 1. above already works and
          delivers the result you want but you just have too much time for
          trouble.

    Reported Issues and Workaround

        * List is Actually Scrollable But panel.xml Says Otherwise

          Panel.xml scroll has scrollable="false" even if it is scrollable.
          Example:
          Scan Center: Create 6 email destinations (6 only) in 7" panel
          Observe:
          1. The first 5 email addresses are in full view.
          2. The 6th - only a very small part of the row is visible, no text
             is visible.
          3. Try to scroll. Yes you can scroll to view the 6th.
          4. Check the panel.xml. esf.ssaUi:id/lvDestinationPanel is
             scrollable="false"
          5. No TextView is present for the 6th row.
          This impacts the scrolling of this code since we only scroll when
          scrollable is true. However this is a rather unlikely combination,
          so this limitation is not handled. But there is an alternative if you
          really want to test the case of 6 rows: Observe that the string you
          are interested (email subject or destination) is also found in the
          content-desc attribute of a LinearLayout of the panel.xml without
          need for scrolling. You can use that in find-widget phrase instead.
          Please note that by intention, UPS does not support manual swiping.
          Swiping is always done automatically when in-area phrase is specified
          provided scrollable="true" for that scroll.

        * Target Row is not Fully Scrolled to View Causing Step Failure

          Example:
          Failing Step:
          In area "com.lxk.adminSettings:id/menu_expandablelist:swipe_offsetx=-1" On text "Sharpness" Find widget "class='android.widget.TextView'&&resource-id='com.lxk.adminSettings:id/slider_value'" do "verify text='3'"

          Problem: Target row (Sharpness) is not in full view so XML of that
          row is not fully-loaded (has missing nodes).

          Resolution: Make an additional step to scroll down to the next
          row (Temperature) so that your target previous row (Sharpness) is
          sure to be scrolled to full view.

          Explanation:
          On-text phrase semantics:
          The on-text phrase is not strict. It simply means "find the matching
          widget nearest this text". We have no intention to redefine it since
          it is serving that purpose. The search starts within on-text widget
          node's (Sharpness) descendants and if it can't find it there
          incrementally increases the search area to that of its parent, then
          grandparent all the way up to in-area node (if provided) or the root
          node. This is the documented behavior.

          In this problem, there is a matching widget (Shadow Detail row) at a
          parent/grandparent level which is not what we want. The one we want
          is not in the xml. So the incorrect node is the one that will be
          assessed and we get this error:

          ---
          ValueError: Action <verify text='3'> has been evaluated and is
          verified to be false.
          Here is the matching widget that was verified:

          {'index': '0', 'selected': 'false', 'checked': 'false', 'text-id': 'TXT_CENTER', 'package': 'com.lxk.adminSettings', 'text': '0', 'long-clickable': 'false', 'enabled': 'true', 'bounds': '[632,348][639,365]', 'content-desc': '', 'clickable': 'false', 'focusable': 'false', 'focused': 'false', 'checkable': 'false', 'resource-id': 'com.lxk.adminSettings:id/slider_value', 'password': 'false', 'class': 'android.widget.TextView', 'scrollable': 'false'}

          If that is not the intended widget, please correct your step.
          Don't know how to fix this error? Pls read the detailed documentation
          Universal Panel Step: lettuce-runner/features/steps/panel/universal.py
          ---

          There is no way to tell via panel.xml if the row has been scrolled to
          full view or only partial view. This limitation of the panel.xml may
          bite us again in the future, so just take note of this workaround.

    HTML Code Support:

        Panel XML could contain HTML ASCII characters (represented as unicode).

        Example for Android:
        From Panel XML,
          text='Release\nHeld Faxes'

        In the example above between strings 'Release' and 'Held Faxes', 
        '\n' looks like unescaped characters '\' and 'n' but is actually a
        single line-feed/new-line character.

        UPS phrases now support the ff HTML code name conventions (nbsp as example):
          1. HTML number (decimal): &#160;
          2. HTML name:             &nbsp;

        Usage example:
          verify text='Release&#10;Held Faxes'

        For HTML ASCII reference, 
          https://ascii.cl/htmlcodes.htm
          https://unicode-table.com/en/

     _  _  _____  _  _       __    _  _  ____  ____  _____  ____  ____     ____   __    _  _  ____  __    ___
    ( \( )(  _  )( \( )___  /__\  ( \( )(  _ \(  _ \(  _  )(_  _)(  _ \   (  _ \ /__\  ( \( )( ___)(  )  / __)
     )  (  )(_)(  )  ((___)/(__)\  )  (  )(_) ))   / )(_)(  _)(_  )(_) )   )___//(__)\  )  (  )__)  )(__ \__ \
    (_)\_)(_____)(_)\_)   (__)(__)(_)\_)(____/(_)\_)(_____)(____)(____/   (__) (__)(__)(_)\_)(____)(____)(___/


    For 2.4", 2-line, and 2.8" non-android panels, and any panel as long as it
    follows the same panel.xml design. In this section, all statements apply to
    all those 3 non-android panels unless a separate section is written for
    2.8" panel which has few differences from 2.4" or 2-line.

    Caution: This section is quite confusing because of the differences. You
    might want to refer to link above for "UPS Rules in Different Panel Sizes".

    In area "*" (for 2.4" and 2-line):
        Like touch panels, in-area phrase is used for automatically
        detecting the size of the list to navigate. The size is important since
        that sets the limit how many time to press the navigation buttons.
        Typical Usage:
        In area "list"
        In area "list:index=2" - when there are 2 or more lists, you have to
        specify which list you want using the index specifier

    In area "*" (for 2.8"):
        Scroll is automatic when scrollUp and scrollDown are present in the
        xml. Otherwise, UPS 2.8 enables swipe if either (in the ff order):
          1.) User provides area phrase
          2.) ListWidget exist in xml
        If both scroll and swipe conditions are not met, UPS 2.8 will not
        scroll nor swipe. So a step like:
          On text "English" Do "press"
        will do the scrolling for you assuming those scrollers are present or
        ListWidget exists.

        The design principle stated in the above paragraph introduces flaws
        or limitations:
          1.) Swipe is not enabled by an object child/node in xml. UI dev does
              not provide such xml below:
                <object>
                <x>0</x>
                <y>36</y>
                <width>320</width>
                <height>204</height>
                <selected>false</selected>
                <scrollable>true</scrollable>
                ...
                ...
              It is only enabled through the condition stated in the paragraph
              above. Hence, when a user uses area phrase to narrow the search,
              UPS 2.8 will try to swipe (if scroll button is not present) if
              the areanode does not exist, even if the areanode is not
              swipable or clickable.
          2.) Given the step below, assume 'Display All Language' is under an
              area called 'Label':
                On text "Display All Language" Do "verify_found"
              Also, assume scroll buttons are not present and ListWdiget is
              present. If the text 'Display All Language' do not exist in xml,
              UPS 2.8 will try to swipe the ListWidget area. Thus, UPS 2.8
              causes unnecessary swiping. The user must provide area phrase to
              address this issue. See the step below:
                In area "Label" on text "Display All Language" Do "verify_found"

        Builds after UPS 2.8 Swipe integration, it has been observed that a
        minimum of 0.5 seconds is required between automation webservices
        requests.

        * What is the purpose of :ascend specifier? (for 2.8")
          This specifier will disable scrolling even if scrollers are present.
          This is bec :ascend should be used rarely. The assumption is you are
          using a pane-specific node as area phrase such as a text node.
          Normally area nodes are nodes that superimpose or transcend
          individual panes such as scrollers or similar containers that exist
          whatever pane you are in. They are not pane-specific.

          Here is one use of ascend:
          In area "text='ID Card':ascend=1" On text "On" Do "verify_found"

          Here "On" is not unique. But it is unique under the parent of
          "ID Card". Specifying :ascend=1 will climb to the parent 1 of
          "ID Card" as your area node. Grandparent will be :ascend=2. We can't
          use plain area phrase such as "ListWidget" since we can't find a way
          of uniquely identifying it among the rest bec of limited attributes
          and hierarchy. :index doesn't work either bec :index changes as you
          scroll up or down. That's bec some rows of the previous pane can be
          carried over to the current pane when you are at the first or last
          pane. Only in 2.8". Android doesn't have this problem.

    On text "*":
        Simply just the text as it appears on the panel as stored in the text
        attribute.

        Examples:
        * On text "Copy"
        * On text "Settings"

        Note: (for 2.4" and 2-line)
        For text that is a member of a list you have to specify an
        in-area phrase as noted above, otherwise an error is raised:
        In area "list" On text "Copy" Do "v-select"

    Find widget "*":
        Find widget "ListItem" - the default attribute is the type attribute
        when no attribute name is specified

        Find widget "helpText='Adjust copy scale.'" - to explicitly specify an
        attribute name; use single quotes for the value

        Find widget "type='ListItem'&&name='option_0'" - for two or more
        attributes use the && separator

    Do "*":
        * Selecting

          * Select in an Itemized List (for 2.4" and 2-line)

            To select vertically or horizontally in a list:
            Do "v-select"
            Do "h-select"

            Examples
            * In area "list:index=1" On text "Copies" Do "v-select"
            * In area "list" On text "Troubleshooting" Do "v-select"
            * In area "objects:index=3" Find widget "Label" Do "h-select:option_count=18:menu_entry=false set text='A4'"

            * What is the purpose of :menu_entry=false specifier?
              By default enter key is pressed on h-select and v-select actions.
              To turn-off that pressing, that is how you do it.

            To select in a list until an attribute is set to a particular
            value:
            Do "h-select:set attrib='value'"
            Currently there is no known meaningful use of this alone but
            combined with :data_type=int or :option_count=<n> specifier, it can
            be useful. See next section. If not set, the default :set specifier
            is :set selected='true'". That is what happens if you only specify
            Do "v-select" or Do "h-select"

          * Select an Integer Value (for 2.4" and 2-line)

            Here there is really no list to select from but we navigate the
            left/right buttons to set it to desired integer value.
            Do "h-select:data_type=int:set settingValue='3'"
            Do "h-select:data_type=int:set settingValue='50'"
            Do "h-select:data_type=int:set settingValue='-1'"

            Examples
            * In area "list:index=2" find widget "helpText='Adjust copy scale.'" Do "h-select:data-type=int:set settingValue='100'"
            * In area "list:index=2" find widget "helpText='Select number of copies.'" Do "h-select:data_type=int:set settingValue='50'"

          * Select in a Non-Itemized List (for 2.4" and 2-line)

            Also here there is really no list to select from but we navigate
            the left/right buttons to set it to achieve the desired setting.
            You have to specify the total number of options so it knows the
            limit of how many times to press left/right button before giving
            up.
            Do "h-select:option_count=2"

            Useful for yes/no button and the like:
            On text "Yes" Do "h-select:option_count=2"

        * Selecting (for 2.8")

            Exactly the same as above except that instead of it internally
            using keyboard keys it uses scroller widgets to navigate to your
            desired value. Here are the rules and syntax:

            * Select in an Itemized List
              Use press, not select. In 2.8", the list is not itemized but
              scroll is automatically supported when scrollers are present.
              Hence there is no need for a select action. Just use press.

            * Select an Integer Value
              select:data_type=int[:menu_entry=false][:forward_key=<name>][:backward_key=<name>]:set <attribute='<value>'
              Here you have to specify :set specifier.

            * Select in a Non-Itemized List
              select:option_count=<n>[:menu_entry=false][:forward_key=<name>][:backward_key=<name>]:set <attribute='<value>'
              Also here you have to specify :set specifier.

            You need to check the xml. You don't need to specify the
            :forward_key and :backward_key specifier because by default they
            are scrollDown and scrollUp (name attribute) respectively. If your
            sceen does not use the default scrollers, you need to specify them.

            In summary, the 2 differences from other panels are that:
            1. you use select (not v/h-select), and
            2. you specify :forward_key and :backward_key when your scrollers
            are not scrollDown and scrollUp

            For example:
            1. Number of Copies:
               Find widget "name='numericButton'" Do "select:data_type=int:forward_key=incrementButton:backward_key=decrementButton:set text='50'"
            2. Minute Setting of Date/Time:
               Find widget "name='minuteLabel'" Do "select:data_type=int:forward_key=minuteUp:backward_key=minuteDown:set text='59'"

        * Long Press (for 2.8")

          In some cases, long press accesses another workflow (pop-up screen).
          For example, pressing and holding the spacebar character in the
          keyboard opens up they Keyboard Type list.
           On text "English" do "press:time_sec=1"

          There are only two (2) press specifiers for 2.8":
          1. ":set attrib='value'"
          2. ":time_sec=n"
          Action Do "press:set selected='true':time_sec=1" is allowed but the
          1 second hold time will not be used.

        * Verifying Values

          To verify an attribute value:
          Do "verify text='Legal (8.5 x 14 in.)'"
          Find widget "EditBox" Do "verify value='mail.lexmark.com'"

        * Verifying Count (for 2.4" and 2-line)

          To verify count:
          Do "verify count=n" - to verify that there are n matching widgets

          For 2 specific values, count can mirror android actions:
          Do "verify count=1" - in android this is similar to action Do "nothing"
          Do "verify count=0" - in android this is similar to action Do "verify none such exists"

        * Verifying Count (for 2.8")

          Do "verify_found" - in android this is similar to action Do "nothing"
          Do "verify_not_found" - in android this is similar to action Do "verify none such exists"

        * Conditional Wait
          "wait_until_found"
             This will attempt to find the widget every 5 seconds for a max 
             of n seconds specified in the screen timeout set in the device. 
             Beyond that, an error will be flagged. You can't use the in-area 
             phrase in conjuction with this wait action, only the on-text and 
             find-widget phrases.
             Example:
             On text "MyHintText" Do "wait_until_found"

          "wait_until_not_found:max_sec=<n>"
             Use this wait when the device is busy and will not start the
             screen timeout clock. Examples are when device is scanning,
             printing, sending. You need to specify a reasonable max value of
             wait in seconds, a value carefully considered from your previous
             multiple test runs. Again here, you can't use the in-area phrase
             in conjuction with this wait action, only the on-text and
             find-widget phrases.
             Example:
             On text "Scanning" Do "wait_until_not_found:max_sec=5"

    Step Conversion:

        We are adding support for converting 2.4" and 2-line step for Settings
        menu to 2.8" for the following constructs below. This will allow
        feature file reuse for most cases. If you want more constructs to be
        supported file a request to tools team. Only heavily used constructs
        will be approved. Lesser used constructs for unusual settings like
        those used for Date and Time will likely not be approved.

        1. In area "list" On text "English" Do "h-select" (or v-select)
           will be converted to:
           On text "English" Do "press"

        2. In area "list" On text "English" Do "verify selected='true'"
           will be converted to:
           On text "English" Do "verify selected='true'"

        In-area phrase will be removed since scrolling is automatic in 2.8".
        Action "press" is used since "v/h-select" actions are invalid in 2.8".

        Caution: The step conversion happens before the step is processed by
        UPS. So on step failures, the error messages that you will see will be
        on the converted step, not on the unconverted step.

    HTML Code Support:

        Panel XML could contain HTML ASCII characters (represented as unicode).

        Example for 2-line:
        From Panel XML,
          <text><![CDATA[No prompt]]></text>

        In the example above between strings 'No' and 'prompt', it looks like 
        a standard whitespace character, but is actually a unicode nbsp 
        character (\u00A0).

        UPS phrases now support the ff HTML code name conventions (nbsp as example):
          1. HTML number (decimal): &#160;
          2. HTML name:             &nbsp;

        Usage example:
          On text "No&nbsp;prompt"
          Do "verify text='No&#160;prompt'"

        For HTML ASCII reference, 
          https://ascii.cl/htmlcodes.htm
          https://unicode-table.com/en/

``````````````````````````````````````````````````````````````````````

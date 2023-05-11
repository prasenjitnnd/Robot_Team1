#stl-cloud-automation

Setup environment for python
``````````````````````````````````````````````````````````````````````
install Python 3.xx
Add Below in Path @Env Var
    C:\Users\<user>\AppData\Local\Programs\Python\Python310
    C:\Users\<user>\AppData\Local\Programs\Python\Python310\Scripts
``````````````````````````````````````````````````````````````````````

Setup pipenv for dependency management
``````````````````````````````````````````````````````````````````````
pip install pipenv
pipenv –-version
pip3 install –-upgrade pipenv
pip3 install --upgrade setuptools
pip3 install --upgrade distlib
``````````````````````````````````````````````````````````````````````
Setup stl-analytics-automation Project & Development Guidelines
```````````````````````````````````````````````````````````````````````
Configure git in system
Clone project in local directory
From cmd / Pycharm / Eclipse / Anaconda run command : pipenv install
Verify dependencies added using : 'pipenv run pip list' command
RightClick on Root Directory and select 'Mark As Source Directory'

**Need to Install Below manually**
pip install lxk_universal_panel_step --extra-index-url=http://pypi.lrdc.lexmark.com --trusted-host=pypi.lrdc.lexmark.com

**Command to execute test**
robot -d ".\report" .\test\sample\test.robot
robot -d ".\report" .\test\sample
robot -d ".\report" .\test

**Development Guidelines**
Global Variables should be declared in UPPER CASE in resource-->global-->variables-->config.py
Local Variables will be in lower case
Test Case should have proper domumentation and Tag associated



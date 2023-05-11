"""
Documentation
Description:       Python Library : winUtil.py
                   Class Contains static method to call APIs from JVM
Created-By:        Prasenjit Nandy
"""
import os
import subprocess
from threading import Thread

from py4j.java_gateway import JavaGateway, GatewayParameters

class winUtil:
  global java_object

  @staticmethod
  def initialize():
    gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25337))  # connect to the JVM
    winUtil.java_object = gateway.jvm.com.lexmark.robot.window()  # invoke constructor
    print('Connected to JVM package:com.lexmark.robot.window Successfully')
    winUtil().startWadServer()
    winUtil.java_object.initialize()

  @staticmethod
  def startWadServer():
    newPath = os.path.abspath(os.getcwd()).split("\\robot\\", 1)[0]
    batFilePath = newPath + '\\robot\\resource\\external\\robot-windows-pluggin\\resource\\startWinDriver.bat'
    subprocess.call([batFilePath])
    print("WinAppDriver server started ...")

class typeUsingFindElementByName(Thread):
    def run(self):
      locator = os.getenv("STLAuto_Locator_Param")
      text = os.getenv("STLAuto_TextToType_Param")
      winUtil.java_object.typeUsingFindElementByName(locator, text)

class typeUsingFindElementByAccessibilityID(Thread):
    def run(self):
      locator = os.getenv("STLAuto_Locator_Param")
      text = os.getenv("STLAuto_TextToType_Param")
      winUtil.java_object.typeUsingFindElementByAccessibilityID(locator, text)


class typeUsingFindElementByID(Thread):
  def run(self):
    locator = os.getenv("STLAuto_Locator_Param")
    text = os.getenv("STLAuto_TextToType_Param")
    winUtil.java_object.typeUsingFindElementByID(locator, text)\


class typeUsingFindElementByXpath(Thread):
    def run(self):
      locator = os.getenv("STLAuto_Locator_Param")
      text = os.getenv("STLAuto_TextToType_Param")
      winUtil.java_object.typeUsingFindElementByXpath(locator, text)

class typeUsingFindElementByCSS(Thread):
    def run(self):
      locator = os.getenv("STLAuto_Locator_Param")
      text = os.getenv("STLAuto_TextToType_Param")
      winUtil.java_object.typeUsingFindElementByCSS(locator, text)


class clickUsingFindElementByName(Thread):
    def run(self):
      locator = os.getenv("STLAuto_Locator_Param")
      winUtil.java_object.clickUsingFindElementByName(locator)


class clickUsingFindElementByAccessibilityID(Thread):
  def run(self):
    locator = os.getenv("STLAuto_Locator_Param")
    winUtil.java_object.clickUsingFindElementByAccessibilityID(locator)

class clickUsingFindElementByID(Thread):
    def run(self):
      locator = os.getenv("STLAuto_Locator_Param")
      winUtil.java_object.clickUsingFindElementByID(locator)


class clickUsingFindElementByXpath(Thread):
  def run(self):
    locator = os.getenv("STLAuto_Locator_Param")
    winUtil.java_object.clickUsingFindElementByXpath(locator)

class clickUsingFindElementByCSS(Thread):
  def run(self):
    locator = os.getenv("STLAuto_Locator_Param")
    winUtil.java_object.clickUsingFindElementByCSS(locator)





package com.lexmark.robot;

import java.io.FileNotFoundException;
import java.io.IOException;
import org.openqa.selenium.By;
import com.lexmark.robot.pluggin.util;
import com.lexmark.robot.pluggin.windows;

public class window {

//.py api created	
	public void initialize() throws FileNotFoundException, InterruptedException, IOException {
		windows.initialize(util.getKeyValue("Application_ID"));
	}
	
	public void print() {
		System.out.println("API invoked from python scripts...");
	}
	
	public static boolean  close() {
		try {
		windows.winDriver.close();
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean  closeApp() {
		try {
			windows.winDriver.closeApp();
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	//.py api created	
		public static boolean typeUsingFindElementByID(String idAttributeValue, String value) {
			try {
				windows.winDriver.findElement(By.id(idAttributeValue)).sendKeys(value);
			return true;
			}catch(Exception e) {
				return false;
			}
		}
	//.py api created	
		public static boolean clickUsingFindElementByID(String idAttributeValue) {
			try {
				windows.winDriver.findElement(By.id(idAttributeValue)).click();
			return true;
			}catch(Exception e) {
				return false;
			}
		}
		
		
		//.py api created	
		public static boolean typeUsingFindElementByXpath(String xpathAttributeValue, String value) {
			try {
				windows.winDriver.findElement(By.xpath(xpathAttributeValue)).sendKeys(value);
			return true;
			}catch(Exception e) {
				return false;
			}
		}
	//.py api created	
		public static boolean clickUsingFindElementByXpath(String xpathAttributeValue) {
			try {
				windows.winDriver.findElement(By.name(xpathAttributeValue)).click();
			return true;
			}catch(Exception e) {
				return false;
			}
		}
		
		//.py api created	
		public static boolean typeUsingFindElementByCSS(String cssAttributeValue, String value) {
			try {
				windows.winDriver.findElement(By.cssSelector(cssAttributeValue)).sendKeys(value);
			return true;
			}catch(Exception e) {
				return false;
			}
		}
	//.py api created	
		public static boolean clickUsingFindElementByCSS(String cssAttributeValue) {
			try {
				windows.winDriver.findElement(By.cssSelector(cssAttributeValue)).click();
			return true;
			}catch(Exception e) {
				return false;
			}
		}
		
		
		
		
		
	
	
	
	
	
//.py api created	
	public static boolean typeUsingFindElementByName(String nameAttributeValue, String value) {
		try {
			windows.winDriver.findElement(By.name(nameAttributeValue)).sendKeys(value);
		return true;
		}catch(Exception e) {
			return false;
		}
	}
//.py api created	
	public static boolean clickUsingFindElementByName(String nameAttributeValue) {
		try {
			windows.winDriver.findElement(By.name(nameAttributeValue)).click();
		return true;
		}catch(Exception e) {
			return false;
		}
	}
	
//.py api created	
		public static boolean typeUsingFindElementByAccessibilityID(String accessibilityAttributeValue, String value) {
			try {
				windows.winDriver.findElementByAccessibilityId(accessibilityAttributeValue).sendKeys(value);
			return true;
			}catch(Exception e) {
				return false;
			}
		}
//.py api created	
		public static boolean clickUsingFindElementByAccessibilityID(String accessibilityAttributeValue) {
			try {
				windows.winDriver.findElementByAccessibilityId(accessibilityAttributeValue).click();
			return true;
			}catch(Exception e) {
				return false;
			}
		}	
	
	public static boolean clearTextUsingFindElementByName(String nameAttributeValue) {
		try {
			windows.winDriver.findElement(By.name(nameAttributeValue)).clear();
		return true;
		}catch(Exception e) {
			return false;
		}
	}
	
	
	public static boolean  context(String name) {
		try {
			windows.winDriver.context(name);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public  boolean equals(Object obj) {
		try {
			windows.winDriver.equals(obj);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElement(By by) {
		try {
			windows.winDriver.findElement(by);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElement(String by , String using) {
		try {
			windows.winDriver.findElement(by, using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementByAccessibilityId (String using) {
		try {
			windows.winDriver.findElementByAccessibilityId(using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementByClassName (String using) {
		try {
			windows.winDriver.findElementByClassName(using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementByCssSelector(String using) {
		try {
			windows.winDriver.findElementByCssSelector(using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementById (String using) {
		try {
			windows.winDriver.findElementById(using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementByLinkText (String using) {
		try {
			windows.winDriver.findElementByLinkText(using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementByName (String using) {
		try {
			windows.winDriver.findElementByName(using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementByPartialLinkText (String using) {
		try {
			windows.winDriver.findElementByPartialLinkText(using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementByTagName (String using) {
		try {
			windows.winDriver.findElementByTagName(using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementByWindowsUIAutomation (String selector) {
		try {
			windows.winDriver.findElementByWindowsUIAutomation(selector);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementByXPath (String using) {
		try {
			windows.winDriver.findElementByXPath(using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElements(By by) {
		try {
			windows.winDriver.findElements(by);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElements(String by , String using) {
		try {
			windows.winDriver.findElements(by,using);
		return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	
	
	public static boolean findElementsByAccessibilityId (String using) {
		try {
			windows.winDriver.findElementsByAccessibilityId(using);
			return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementsByClassName (String using) {
		try {
			windows.winDriver.findElementsByClassName(using);
			return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementsByCssSelector (String using) {
		try {
			windows.winDriver.findElementsByCssSelector(using);
			return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementsById (String using) {
		try {
			windows.winDriver.findElementsById(using);
			return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean  findElementsByLinkText(String using) {
		try {
			windows.winDriver.findElementsByLinkText(using);
			return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementsByName (String using) {
		try {
			windows.winDriver.findElementsByName(using);
			return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementsByPartialLinkText (String using) {
		try {
			windows.winDriver.findElementsByPartialLinkText(using);
			return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementsByTagName (String using) {
		try {
			windows.winDriver.findElementsByTagName(using);
			return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementsByWindowsUIAutomation (String selector) {
		try {
			windows.winDriver.findElementsByWindowsUIAutomation(selector);
			return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
	public static boolean findElementsByXPath (String using) {
		try {
			windows.winDriver.findElementsByXPath(using);
			return true;
		}catch(Exception e) {
			return false;
		}
		
	}
	
		
	
	
}

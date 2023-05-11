package com.lexmark.robot.pluggin;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

import org.openqa.selenium.remote.DesiredCapabilities;

import io.appium.java_client.windows.WindowsDriver;
import io.appium.java_client.windows.WindowsElement;

public class windows {
	public static DesiredCapabilities appCapabilities = null;
	public static WindowsDriver winDriver = null;
	static Thread t1 = null;
	public static Object lpmcClientAuthApplication;
	
	public static void initialize(String appID) throws InterruptedException, FileNotFoundException, IOException {
			startWinDriver();
			Thread.sleep(5000);
			appCapabilities = new DesiredCapabilities();
			appCapabilities.setCapability("app", appID);
			winDriver = new WindowsDriver<WindowsElement>(new URL(util.getKeyValue("WAD_Address")), appCapabilities);
			Thread.sleep(2000);
		}
	
	
	public static void startWinDriver() {
		t1 = new Thread(new Runnable() {
		       public void run() { 
		           try {
					util.startWinDriver();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
		       }		
		    });
		t1.start();
		 
	}
	
	protected static void closeProcess() {
		t1.stop();
	}

}

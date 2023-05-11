package com.lexmark.robot.pluggin.test;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;

import com.lexmark.robot.pluggin.util;
import com.lexmark.robot.pluggin.windows;

import io.appium.java_client.windows.WindowsDriver;
import io.appium.java_client.windows.WindowsElement;

public class loginToLpmcAuth {

	public static void main(String[] args) throws InterruptedException, FileNotFoundException, IOException {
		
		util.getKeyValue("Application_ID");
		windows.initialize(util.getKeyValue("Application_ID"));
		windows.winDriver.findElement(By.name("E-mail")).sendKeys("kt@test.onelxk.co");
		windows.winDriver.findElement(By.name("Next")).click();
		Thread.sleep(10000);
		windows.winDriver.findElement(By.name("Password")).sendKeys("abcd123");
		windows.winDriver.findElement(By.name("Log In")).click();
		Thread.sleep(2000);
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	}

}

package com.lexmark.robot.pluggin;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Properties;

import org.apache.commons.exec.CommandLine;

public class util {

	public static Properties prop = null;
	
	protected static void startWinDriver() throws FileNotFoundException, IOException {
		Runtime rt = Runtime.getRuntime();
	    String[] command = new String[3];
	    int exitVal = -1;
	    ArrayList<Object> output = new ArrayList();
	    String commandOutput = "";
	    command[0] = "cmd";
	    command[1] = "/c";
	    String batchFileCommand = "cd "+ System.getProperty("user.dir")+"\\resource" + " && startWinDriver.bat";
	    command[2] = batchFileCommand;
	    try {
	      Process pr = rt.exec(command);
	      BufferedReader input = new BufferedReader(new InputStreamReader(pr.getInputStream()));
	      String line = null;
	      System.out.println("Appium Windows Driver Starting @http://localhost:4723/");
	      while ((line = input.readLine()) != null) {
	        
	        commandOutput = String.valueOf(String.valueOf(commandOutput)) + line + "\n";
	      } 
	      
	      exitVal = pr.waitFor();
	      output.add(Integer.valueOf(exitVal));
	      output.add(commandOutput);
	    } catch (Exception exception) {}
	}
	
	public static String getKeyValue(String key) throws FileNotFoundException, IOException {
		String val = null;
		String envVarValue = null;
		
		envVarValue = System.getenv("ANALYTICS_ROBOT_GLOBAL_CONF_PATH");
		
		if(envVarValue==null)
		envVarValue = System.getProperty("user.dir")+"\\resource\\config.properties";
		
		
		System.out.println(envVarValue);
		prop = new Properties();
		prop.load(new FileInputStream(new File(envVarValue)));
		val = (String) prop.get(key).toString().trim();
		return val;
	}
}

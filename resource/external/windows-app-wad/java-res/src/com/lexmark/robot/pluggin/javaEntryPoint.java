package com.lexmark.robot.pluggin;

import java.io.FileNotFoundException;
import java.io.IOException;
import com.lexmark.robot.window;
import py4j.GatewayServer;

public class javaEntryPoint {
	
    private window obj;

        public javaEntryPoint() {
        	obj = new window();
        }


    public static void main(String[] args) throws NumberFormatException, FileNotFoundException, IOException {
            GatewayServer gatewayServer = new GatewayServer(new 
            javaEntryPoint(),Integer.parseInt(util.getKeyValue("GatewayServer_Port")));
            gatewayServer.start();
            System.out.println("Gateway Server Started");
        }


}

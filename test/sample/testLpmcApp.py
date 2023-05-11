from py4j.java_gateway import JavaGateway, GatewayParameters

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=25337))   # connect to the JVM
java_object = gateway.jvm.com.lexmark.robot.window()  # invoke constructor
java_object.initialize()
java_object.print()
java_object.typeUsingFindElementByName("E-mail","kt@test.onelxk.co")
java_object.clickUsingFindElementByName("Next")
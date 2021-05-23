import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")
 
Connected = False   #global variable for the state of the connection
 
broker_address= "127.0.0.1"
port = 1883
#user = "den"
#password = "1"
 
client = mqttClient.Client("Python")               #create new instance
#client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.connect(broker_address, port=port)          #connect to broker
 
client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(0.1)
 
try:
    direction=1
    value=0
    while True:
 
        if direction == 1:
                value+=1
        else:
                value-=1
        if value == 10 or value == 0:
                direction*=-1
        temp = "temperature,site=room1 value="+str(value)
        print(temp)
        client.publish("sensors",temp)
        time.sleep(2)
 
except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()

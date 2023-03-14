Christian Ko

## What is MQTT?

<span style="color:blue">Comments in blue</span>


Message Queueing Telemetry Transport (MQTT) is a lightweight ~~publish-subscribe~~ <span style="color:blue">*removed since you give detail on it later*</span> protocol used for connecting devices over limited bandwidth or unreliable networks. Because it is lightweight, open, and simple, it is often used for M2M (machine-to-machine) and IoT (Internet of Things) communication. MQTT runs on TCP/IP protocol. <span style="color:blue">*Give some detail on TCP/IP*</span>

Andy Stanford-Clark and Arlen Nipper created MQTT in 1999, which was originally intended to control oil pipelines remotely via satellite. It was designed for minimal battery loss and bandwidth. MQTT was later standardized under OASIS, an organization that focuses on adoption of open standards. 

<span style="color:blue">*mention there is a tutorial aspect or game-based example to this article in the intro*</span>

## How does it work?

The MQTT architecture runs on a publish and subscribe (pub/sub) system. Unlike the traditional model in which a client directly communicates with a server, the pub/sub model separates the client that sends a message (the publisher) from other clients that receives the message (the subscriber). Instead, clients connect to a server, the broker, that handles receiving and sending communications ~~to clients~~. Publishers and subscribers are clients ~~. A client~~ <span style="color:blue">*",which..."*</span> is any device that can use MQTT over TCP/IP, like a microcontroller or a computer. 

Once connected to a broker, clients can publish messages. These messages have a payload, which is the data to transmit, and a topic that interested clients can subscribe to. Topics are strings that are hierarchically structured with the slash (/) character as delimiters, similar to folder structures in a computer file system. For example, “UCLA/HSSEAS/ECE/113” or “United States/California/Westwood”. Once a message is published and read, the broker processes it according to the Quality of Service (QoS) level indicated. 

In order to receive messages, clients can subscribe to various topics, and once subscribed, can start receiving messages directed to those topics. 

![Figure 1](https://github.com/ECE-180D-WS-2023/Knowledge-Base-Wiki/blob/main/Images/mqtt.png)
        Figure 1. Example of an MQTT system

As Figure 1 shows, the smoke alarm is one client that publishes to the “SMOKE SENSOR” topic, which phone 1 and 2 are subscribed to, and the sprinklers are another client that subscribes to the “SPRINKLER SYSTEM” topic, which phone 2 publishes to.


## Using MQTT

The general flow for creating an MQTT client and using it is as follows:
1. Create a client instance
2. Connect to a broker
3. Subscribe on connect
4. Loop to stay connected to the broker
5. Publish as needed
6. Disconnect from the broker at session end

<span style="color:blue">*I'd mention the language and library you are describing, as there might be some differences in implementations*</span>

A client instance can be constructed using the `Client()` function. If needed, you can set a last will message, which will be sent to the broker if the connection between the client and the broker is ever lost without calling the `disconnect()` function.

`connect()` or `connectasync()` connects the client to the broker. `connectasync()` is used to delay the connection until `loop_start()` is called. The relevant argument these functions take is the hostname or IP address of the broker. Use `disconnect()` to end the connection to the broker cleanly, although any queued messages will not be sent if the connection ends. 

`loop_start()` and `loop_stop()` are used to process all incoming and outgoing network data.

Of course, in order to publish and subscribe, you would use `publish(topic, payload, qos)` and `subscribe(topic, qos)`.

topic is the topic to publish or subscribe to.

<span style="color:blue">*Make sure these are full sentences and capitalized correctly**</span>

payload is the message to be sent. It should be a string, but if an int or float is passed here, it will be converted to a string automatically. QoS is 0, 1, or 2, with 0 being the default value.

QoS Levels:

0 - The message will be sent once, without confirmation.

1 - The message will be sent at least once, so there is confirmation that the message was delivered to the broker or the subscriber.

2 - The message will be sent exactly once.

For most purposes in this class, a QoS level of 1, with code to handle duplicate messages is sufficient, as QoS <span style="color:blue">*Quality of Service*?</span> 0 can mean lost messages, while QoS 2 takes too long.


For this class <span style="color:blue">* Don't explicitly mention the class, but perhaps say "For game communications..."*</span>, most game state machines can be represented as follows:

![Figure 2](https://github.com/ECE-180D-WS-2023/Knowledge-Base-Wiki/blob/main/Images/flow.png)
        Figure 2. MQTT Game Flow

<span style="color:blue">Walk through this figure in detail in words. You could have a whole section on a high-level game implementation.</span>

Example pseudocode: <span style="color:blue">*This is python not pseudocode. Full blocks of code should be at the end. You need a formal conclusion before it, and reference that a code example is given at the end of the article. *</span>
```
import paho.mqtt.client as mqtt

RECEIVED_DATA = False
DATA = ""

# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    client.subscribe("kfc/chicken", qos=1)
    client.subscribe("kfc/soda", qos=1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(’Unexpected Disconnect’)
    else:
        print(’Expected Disconnect’)

def on_message(client, userdata, message):
    if (message.topic == "kfc/chicken"):
	print("yummm " + str(message.payload))
	RECEIVED_DATA = True
	DATA = "message.payload"

# 1. create a client instance.
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 2. connect to a broker using one of the connect*() functions.
client.connect_async(’mqtt.eclipseprojects.io’)

# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()

while True: # perhaps add a stopping condition using some break or something.

    # start game logic

        while (not RECEIVED_DATA):
	    # update game
	    pass

    # more game logic
    RECEIVED_DATA = True
    DATA = "message.payload"

client.loop_stop()
client.disconnect()
```

# Sources

https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html

https://www.hivemq.com/blog/mqtt-essentials-part-1-introducing-mqtt/

https://ably.com/topic/mqtt

https://www.paessler.com/it-explained/mqtt

https://github.com/eclipse/paho.mqtt.python

https://www.integrasources.com/blog/mqtt-protocol-iot-devices/ (Figure 1)


***

![](https://github.com/ECE-180D-WS-2023/Knowledge-Base-Wiki/blob/main/Images/Screen%20Shot%202023-02-09%20at%2011.44.10%20PM.png)

Word Count (02-09)

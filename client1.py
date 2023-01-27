import paho.mqtt.client as mqtt
import numpy as np
import tabulate as tab

# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
  print("Connection returned result: " + str(rc))

  # Subscribing in on_connect() means that if we lose the connection and
  # reconnect then subscriptions will be renewed.
  client.subscribe("rps1", qos = 1)
  client.subscribe("rps2", qos = 1)
  client.subscribe("rps_results", qos = 1)


# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
  if rc != 0:
    print('Unexpected Disconnect')
  else:
    print('Expected Disconnect')

received_data1 = False
received_data2 = False
move1 = ""
move2 = ""
result = ""

# The default message callback.
# (won't be used if only publishing, but can still exist)
def on_message(client, userdata, message):
  if message.topic == "rps1":
    global received_data1
    global move1
    received_data1 = True
    move1 = message.payload.decode()
  if message.topic == "rps2":
    global received_data2
    global move2
    received_data2 = True
    move2 = message.payload.decode()
  if message.topic == "rps_results":
    print(message.payload)

# 1. create a client instance.
client = mqtt.Client()
# add additional client options (security, certifications, etc.)
# many default options should be good to start off.
# add callbacks to client.
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

# 2. connect to a broker using one of the connect*() functions.
# client.connect_async("test.mosquitto.org")
client.connect_async('mqtt.eclipseprojects.io')

# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()

# 4. use subscribe() to subscribe to a topic and receive messages.

# 5. use publish() to publish messages to the broker.
# payload must be a string, bytearray, int, float or None.
while True:
  move = input("Choose Your Move (Rock, Paper, Scissors): ")
  client.publish("rps1", move, qos = 1)
  while not received_data1 or not received_data2:
    pass

  if (move1 == "Rock" or move1 == "Paper" or move1 == "Scissors" or 
      move2 == "Rock" or move2 == "Paper" or move2 == "Scissors"):

    if (move1 == "Rock" and move2 == "Rock"):
      result = "Draw"
    elif (move1 == "Paper" and move2 == "Paper"):
      result = "Draw"
    elif (move1 == "Scissors" and move2 == "Scissors"):
      result = "Draw"

    elif (move1 == "Rock" and move2 == "Scissors"):
      result = "Player 1 Wins"
    elif (move1 == "Paper" and move2 == "Rock"):
      result = "Player 1 Wins"
    elif (move1 == "Scissors" and move2 == "Paper"):
      result = "Player 1 Wins"

    elif (move1 == "Scissors" and move2 == "Rock"):
      result = "Player 2 Wins"
    elif (move1 == "Rock" and move2 == "Paper"):
      result = "Player 2 Wins"
    elif (move1 == "Paper" and move2 == "Scissors"):
      result = "Player 2 Wins"
  else:
    result = "Invalid Move"

  client.publish("rps_results", result, qos = 1)
  received_data1 = False
  received_data2 = False

# 6. use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()
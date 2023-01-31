import paho.mqtt.client as mqtt
import numpy as np
import pygame

from pygame.locals import (
  RLEACCEL,
  K_UP,
  K_LEFT,
  K_RIGHT,
  K_ESCAPE,
  K_RETURN,
  KEYUP,
  KEYDOWN,
  QUIT,
)

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

clock = pygame.time.Clock()

class Rock(pygame.sprite.Sprite):
  def __init__(self):
    super(Rock, self).__init__()
    self.surf = pygame.image.load("rock.png").convert()
    self.surf = pygame.transform.scale(self.surf, (200, 200))
    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

class Paper(pygame.sprite.Sprite):
  def __init__(self):
    super(Paper, self).__init__()
    self.surf = pygame.image.load("paper.png").convert()
    self.surf = pygame.transform.scale(self.surf, (200, 200))
    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

class Scissors(pygame.sprite.Sprite):
  def __init__(self):
    super(Scissors, self).__init__()
    self.surf = pygame.image.load("scissors.png").convert()
    self.surf = pygame.transform.scale(self.surf, (200, 200))
    self.surf.set_colorkey((255, 255, 255), RLEACCEL)

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

# The default message callback.
# (won't be used if only publishing, but can still exist)
def on_message(client, userdata, message):
  if message.topic == "rps1":
    global received_data1
    global player1_move
    received_data1 = True
    player1_move = message.payload.decode()
    print("p1 used" + str(player1_move))
  if message.topic == "rps2":
    global received_data2
    received_data2 = True
    print("p2 used" + str(player2_move))
  if message.topic == "rps_results":
    global gameEnd
    gameEnd = True
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

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rock, Paper, Scissors!')

font = pygame.font.Font(None, 32)

rock = Rock()
paper = Paper()
scissors = Scissors()

running = True
player1_move = ""
player2_move = ""
result = ""
gameEnd = False

# 3. call one of the loop*() functions to maintain network traffic flow with the broker.
client.loop_start()

# 4. use subscribe() to subscribe to a topic and receive messages.

# 5. use publish() to publish messages to the broker.
# payload must be a string, bytearray, int, float or None.
while running:
  for event in pygame.event.get():
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        running = False

      elif event.key == K_LEFT:
        if (player2_move == ""):
          client.publish("rps2", "rock", qos = 1)
          print("p2 used rock")
        player2_move = "rock"
      elif event.key == K_UP:
        if (player2_move == ""):
          client.publish("rps2", "paper", qos = 1)
          print("p2 used paper")
        player2_move = "paper"
      elif event.key == K_RIGHT:
        if (player2_move == ""):
          client.publish("rps2", "scissors", qos = 1)
          print("p2 used scissors")
        player2_move = "scissors"

      elif event.key == K_RETURN:
        if (gameEnd == True):
          player1_move = ""
          player2_move = ""
          gameEnd = False

    elif event.type == QUIT:
      running = False

  screen.fill((220, 200, 150))

  arena = pygame.Surface((980, 300))
  arena.fill((21,96,189))
  arena_center = ((SCREEN_WIDTH - arena.get_width())/2, (SCREEN_HEIGHT - arena.get_height() - 360)/2)
  arena_left = ((SCREEN_WIDTH - rock.surf.get_width() - 580)/2, (SCREEN_HEIGHT - rock.surf.get_height() - 400)/2)
  arena_right = ((SCREEN_WIDTH - rock.surf.get_width() + 580)/2, (SCREEN_HEIGHT - rock.surf.get_height() - 400)/2)

  text_bg = pygame.Surface((960, 50))
  text_bg.fill((67,127,202))
  text_bg_center = ((SCREEN_WIDTH - text_bg.get_width())/2, (SCREEN_HEIGHT - text_bg.get_height() - 130)/2)
  
  rock_center = ((SCREEN_WIDTH - rock.surf.get_width() - 620)/2, (SCREEN_HEIGHT - rock.surf.get_height() + 440)/2)
  paper_center = ((SCREEN_WIDTH - paper.surf.get_width())/2, (SCREEN_HEIGHT - paper.surf.get_height() + 180)/2)
  scissors_center = ((SCREEN_WIDTH - scissors.surf.get_width() + 620)/2, (SCREEN_HEIGHT - scissors.surf.get_height() + 440)/2)

  player1_text = font.render("Player 1", True, (255,255,255))
  player2_text = font.render("Player 2", True, (255,255,255))

  result_text = font.render(result, True, (255,255,255))
  result_text_center = ((SCREEN_WIDTH - result_text.get_width())/2, (SCREEN_HEIGHT - result_text.get_height() - 125)/2)

  result_text_left = ((SCREEN_WIDTH - player1_text.get_width() - 580)/2, (SCREEN_HEIGHT - player1_text.get_height() - 125)/2)
  result_text_right = ((SCREEN_WIDTH - player2_text.get_width() + 580)/2, (SCREEN_HEIGHT - player2_text.get_height() - 125)/2)

  instructions1 = font.render("Left Arrow: Rock", True, (255,255,255))
  instructions2 = font.render("Up Arrow: Paper", True, (255,255,255))
  instructions3 = font.render("Right Arrow: Scissors", True, (255,255,255))

  instructions_pos1 = ((SCREEN_WIDTH - instructions1.get_width())/2, (SCREEN_HEIGHT - instructions1.get_height() + 480)/2)
  instructions_pos2 = ((SCREEN_WIDTH - instructions2.get_width())/2, (SCREEN_HEIGHT - instructions2.get_height() + 530)/2)
  instructions_pos3 = ((SCREEN_WIDTH - instructions3.get_width())/2, (SCREEN_HEIGHT - instructions3.get_height() + 580)/2)

  screen.blit(arena, arena_center)
  screen.blit(rock.surf, rock_center)
  screen.blit(paper.surf, paper_center)
  screen.blit(scissors.surf, scissors_center)
  screen.blit(text_bg, text_bg_center)
  screen.blit(player1_text, result_text_left)
  screen.blit(player2_text, result_text_right)
  screen.blit(instructions1, instructions_pos1)
  screen.blit(instructions2, instructions_pos2)
  screen.blit(instructions3, instructions_pos3) 
  screen.blit(result_text, result_text_center)

  pygame.display.flip()
  clock.tick(30)

  while (not received_data1 or not received_data2) and running:
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_ESCAPE:
          running = False

      elif event.type == QUIT:
        running = False

    for event in pygame.event.get():
      if event.type == KEYDOWN:
        if event.key == K_LEFT:
          if (player2_move == ""):
            client.publish("rps2", "rock", qos = 1)
            print("p2 used rock")
          player2_move = "rock"
        elif event.key == K_UP:
          if (player2_move == ""):
            client.publish("rps2", "paper", qos = 1)
            print("p2 used paper")
            player2_move = "paper"
        elif event.key == K_RIGHT:
          if (player2_move == ""):
            client.publish("rps2", "scissors", qos = 1)
            print("p2 used scissors")
            player2_move = "scissors"

### update player 1 move ###
    if (player1_move == "rock"):
      screen.blit(rock.surf, arena_left)
      pygame.display.flip()
    elif (player1_move == "paper"):
      screen.blit(paper.surf, arena_left)
      pygame.display.flip()
    elif (player1_move == "scissors"):
      screen.blit(scissors.surf, arena_left)
      pygame.display.flip()
    else:
      pass

### update player 2 move ###
    if (player2_move == "rock"):
      screen.blit(rock.surf, arena_right)
      pygame.display.flip()
    elif (player2_move == "paper"):
      screen.blit(paper.surf, arena_right)
      pygame.display.flip()
    elif (player2_move == "scissors"):
      screen.blit(scissors.surf, arena_right)
      pygame.display.flip()
    else:
      pass
    pass

### game logic ###
  if (player1_move == "rock" and player2_move == "scissors"):
    result = "Player 1 Wins"
  elif (player1_move == "rock" and player2_move == "paper"):
    result = "Player 2 Wins"
  elif (player1_move == "rock" and player2_move == "rock"):
    result = "Draw"

  elif (player1_move == "paper" and player2_move == "scissors"):
    result = "Player 2 Wins"
  elif (player1_move == "paper" and player2_move == "paper"):
    result = "Draw"
  elif (player1_move == "paper" and player2_move == "rock"):
    result = "Player 1 Wins"

  elif (player1_move == "scissors" and player2_move == "scissors"):
    result = "Draw"
  elif (player1_move == "scissors" and player2_move == "paper"):
    result = "Player 1 Wins"
  elif (player1_move == "scissors" and player2_move == "rock"):
    result = "Player 2 Wins"
  else:
    pass

  client.publish("rps_results", result, qos = 1)
  continue
# 6. use disconnect() to disconnect from the broker.
pygame.quit()
client.loop_stop()
client.disconnect()
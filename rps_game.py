import pygame
import random as rand

from pygame.locals import (
	RLEACCEL,
	K_UP,
	K_LEFT,
	K_RIGHT,
	K_ESCAPE,
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

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Rock, Paper, Scissors!')

font = pygame.font.Font(None, 32)

rock = Rock()
paper = Paper()
scissors = Scissors()

running = True
player_move = ""
ai_move = ""
result = ""
chance = rand.randint(1,3)
#player_wins = 0
#ai_wins = 0
#stat_incremented = False

while running:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
			elif event.key == K_LEFT:
				player_move = "rock"
				chance = rand.randint(1,3)
			elif event.key == K_UP:
				player_move = "paper"
				chance = rand.randint(1,3)
			elif event.key == K_RIGHT:
				player_move = "scissors"
				chance = rand.randint(1,3)

		elif event.type == QUIT:
			running = False

	if (chance == 1):
		ai_move = "rock"
	elif (chance == 2):
		ai_move = "paper"
	elif (chance == 3):
		ai_move = "scissors"
	else:
		pass

	screen.fill((220, 200, 150))

	arena = pygame.Surface((980, 300))
	arena.fill((21,96,189))
	arena_center = ((SCREEN_WIDTH - arena.get_width())/2, (SCREEN_HEIGHT - arena.get_height() - 360)/2)

	text_bg = pygame.Surface((960, 50))
	text_bg.fill((67,127,202))
	text_bg_center = ((SCREEN_WIDTH - text_bg.get_width())/2, (SCREEN_HEIGHT - text_bg.get_height() - 130)/2)
	
	rock_center = ((SCREEN_WIDTH - rock.surf.get_width() - 620)/2, (SCREEN_HEIGHT - rock.surf.get_height() + 440)/2)
	paper_center = ((SCREEN_WIDTH - paper.surf.get_width())/2, (SCREEN_HEIGHT - paper.surf.get_height() + 180)/2)
	scissors_center = ((SCREEN_WIDTH - scissors.surf.get_width() + 620)/2, (SCREEN_HEIGHT - scissors.surf.get_height() + 440)/2)

	arena_left = ((SCREEN_WIDTH - rock.surf.get_width() - 580)/2, (SCREEN_HEIGHT - rock.surf.get_height() - 400)/2)
	arena_right = ((SCREEN_WIDTH - rock.surf.get_width() + 580)/2, (SCREEN_HEIGHT - rock.surf.get_height() - 400)/2)

	player_text = font.render("Player", True, (255,255,255))
	ai_text = font.render("CPU", True, (255,255,255))

	result_text_left = ((SCREEN_WIDTH - player_text.get_width() - 580)/2, (SCREEN_HEIGHT - player_text.get_height() - 125)/2)
	result_text_right = ((SCREEN_WIDTH - ai_text.get_width() + 580)/2, (SCREEN_HEIGHT - ai_text.get_height() - 125)/2)

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
	screen.blit(player_text, result_text_left)
	screen.blit(ai_text, result_text_right)
	screen.blit(instructions1, instructions_pos1)
	screen.blit(instructions2, instructions_pos2)
	screen.blit(instructions3, instructions_pos3)

	if (player_move == "rock"):
			screen.blit(rock.surf, arena_left)
	elif (player_move == "paper"):
			screen.blit(paper.surf, arena_left)
	elif (player_move == "scissors"):
			screen.blit(scissors.surf, arena_left)

	if (player_move == "rock" and ai_move == "scissors"):
		screen.blit(scissors.surf, arena_right)
		result = "You Win"
		#player_wins = player_wins + 1
		#player_move = ""
		#ai_move = ""
	elif (player_move == "rock" and ai_move == "paper"):
		screen.blit(paper.surf, arena_right)
		result = "You Lose"
		#ai_wins = ai_wins + 1
		#player_move = ""
		#ai_move = ""
	elif (player_move == "rock" and ai_move == "rock"):
		screen.blit(rock.surf, arena_right)
		result = "Draw"
		#player_move = ""
		#ai_move = ""

	elif (player_move == "paper" and ai_move == "scissors"):
		screen.blit(scissors.surf, arena_right)
		result = "You Lose"
		#ai_wins = ai_wins + 1
		#player_move = ""
		#ai_move = ""
	elif (player_move == "paper" and ai_move == "paper"):
		screen.blit(paper.surf, arena_right)
		result = "Draw"
		#player_move = ""
		#ai_move = ""
	elif (player_move == "paper" and ai_move == "rock"):
		screen.blit(rock.surf, arena_right)
		result = "You Win"
		#player_wins = player_wins + 1
		#player_move = ""
		#ai_move = ""

	elif (player_move == "scissors" and ai_move == "scissors"):
		screen.blit(scissors.surf, arena_right)
		result = "Draw"
		#player_move = ""
		#ai_move = ""
	elif (player_move == "scissors" and ai_move == "paper"):
		screen.blit(paper.surf, arena_right)
		result = "You Win"
		#player_wins = player_wins + 1
		#player_move = ""
		#ai_move = ""
	elif (player_move == "scissors" and ai_move == "rock"):
		screen.blit(rock.surf, arena_right)
		result = "You Lose"
		#ai_wins = ai_wins + 1
		#player_move = ""
		#ai_move = ""
	else:
		pass

	result_text = font.render(result, True, (255,255,255))
	result_text_center = ((SCREEN_WIDTH - result_text.get_width())/2, (SCREEN_HEIGHT - result_text.get_height() - 125)/2)

	#player_stats = font.render(str(player_wins), True, (255,255,255))
	#player_center = ((SCREEN_WIDTH - player_stats.get_width() - 460)/2, (SCREEN_HEIGHT - player_stats.get_height() - 125)/2)

	#ai_stats = font.render(str(ai_wins), True, (255,255,255))
	#ai_center = ((SCREEN_WIDTH - ai_stats.get_width() + 480)/2, (SCREEN_HEIGHT - ai_stats.get_height() - 125)/2)

	screen.blit(result_text, result_text_center)
	#screen.blit(player_stats, player_center)
	#screen.blit(ai_stats, ai_center)

	pygame.display.flip()
	clock.tick(30)


pygame.quit()
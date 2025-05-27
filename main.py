import pygame
from pygame import locals
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = 1

game_state = "main_menu"
game_type = 3
background = ""
titlescreen = pygame.image.load("Backgrounds/prot_titlesc2.png").convert()
start = (pygame.image.load("Backgrounds/start_0.png").convert(), pygame.image.load("Backgrounds/start_1.png").convert(), pygame.image.load("Backgrounds/start_2.png").convert(),pygame.image.load("Backgrounds/start_3.png").convert(),pygame.image.load("Backgrounds/start_4.png").convert())
options = pygame.image.load("Backgrounds/prot_opcje.png").convert()
def generate_options_rect(pos1, pos2):
    prostokat = pygame.Surface([200,100])
    rect = prostokat.get_rect()
    pygame.draw.rect(screen, "#FFFFFF", rect)
    #pygame.display.flip()
def animated_start(napis):
    for i in napis:
        screen.blit(i, (150, 350))
        pygame.display.flip()
        time.sleep(0.07)
def generate_background(bkg):
    if bkg == 3:
        screen.fill("red")
    elif bkg == 4:
        screen.fill("purple")
    elif bkg == 5:
        screen.fill("maroon")
    elif bkg == titlescreen:
        screen.blit(bkg, (0, 0))
    elif bkg == options:
        screen.blit(bkg, (0, 0))
class Player(pygame.sprite.Sprite):
   def __init__(self):
       pygame.sprite.Sprite.__init__(self)
       self.image=pygame.Surface([100,100])
       self.image.fill("#FFAF00")
       self.rect_pos=(100,0)
       self.rect=self.image.get_rect()
player: Player = Player()
obj = pygame.sprite.Group()
obj.add(player)
while running:
    if game_state == "main_menu":
        background = titlescreen
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_q:
                    running = 0
                    break
                elif event.key == pygame.K_SPACE:
                    background = game_type
                    game_state = "playing"
                    break
                elif event.key == pygame.K_o:
                    game_state = "options"
                    break
            elif event.type == pygame.QUIT:
                running=0
                break
    elif game_state == "options":
        background = options
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_q:
                    game_state = "main_menu"
                elif event.key == pygame.K_t:
                    game_type += 1
                    if game_type > 5:
                        game_type = 3
            elif event.type == pygame.QUIT:
                running=0
    elif game_state == "playing":
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = 0
                    break
            elif event.type == pygame.QUIT:
                running = 0
    #obj.draw(screen)
    generate_background(background)
    generate_options_rect(100, 100)
    pygame.display.flip()
    if game_state == "main_menu" and background == titlescreen:
        animated_start(start)

pygame.quit()
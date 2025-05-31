import pygame
from pygame import locals
import time

#inicjalizacja pygame, ekranu, czasu i warunku wyjscia z gry
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = 1

#zmienne i kolekcje dotyczace waznych elementow, potrzebne w wielu miejscach. Nazwy opisuja role
game_state = "main_menu"
opcja = ("Tryb","Board","SILVL","Timer")
numer_opcji = 0
options_attributes = {"Tryb" : [0,1,90], "Board" : [0,2,90], "SILVL" : [0,2,120], "Timer" : [0,1,90]}
options_positions = ([323,165,[90,60], 1], [323,235,[90,60], 0], [323,305,[120,60], 0], [323,375,[90,60], 0])
background = ""
#zaladowanie potrzebnych obrazow
titlescreen = pygame.image.load("Backgrounds/prot_titlesc2.png").convert()
start = (pygame.image.load("Backgrounds/start_0.png").convert(), pygame.image.load("Backgrounds/start_1.png").convert(), pygame.image.load("Backgrounds/start_2.png").convert(),pygame.image.load("Backgrounds/start_3.png").convert(),pygame.image.load("Backgrounds/start_4.png").convert())
options = pygame.image.load("Backgrounds/prot_opcje.png").convert()
credits_screen = pygame.image.load("Backgrounds/placeholder_credits.png").convert()
#funkcje
def generate_options_rect(pos1, pos2, rozmiar, active):
    prostokat = pygame.Surface(rozmiar)
    rect = prostokat.get_rect()
    rect=rect.move(pos1,pos2)
    if active:
        pygame.draw.rect(screen, "#22CD55", rect, 3)
    else:
        pygame.draw.rect(screen, "#FFFFFF", rect, 3)
    #pygame.display.flip()
def animated_start(napis):
    for i in napis:
        screen.blit(i, (150, 350))
        pygame.display.flip()
        time.sleep(0.07)
def generate_background(bkg):
    if bkg == 0:
        screen.fill("red")
    elif bkg == 1:
        screen.fill("purple")
    elif bkg == 2:
        screen.fill("maroon")
    elif bkg == credits_screen:
        screen.blit(bkg, (0, 0))
    elif bkg == titlescreen:
        screen.blit(bkg, (0, 0))
    elif bkg == options:
        screen.blit(bkg, (0, 0))
#prototyp
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
#cialo gry podzielone na sekcje
while running:
    if game_state == "main_menu":
        background = titlescreen
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_e:
                    running = 0
                    break
                elif event.key == pygame.K_SPACE:
                    background = options_attributes["Board"][0]
                    game_state = "playing"
                    break
                elif event.key == pygame.K_o:
                    game_state = "options"
                    break
                elif event.key == pygame.K_c:
                    game_state = "credits"
                    break
            elif event.type == pygame.QUIT:
                running=0
                break
    elif game_state == "playing":
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = 0
                    break
            elif event.type == pygame.QUIT:
                running = 0
    while game_state == "credits":
        background = credits_screen
        generate_background(background)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game_state = "main_menu"
            elif event.type == pygame.QUIT:
                running = 0
    while game_state == "options":
        background = options
        generate_background(background)
        for elem in options_positions:
            generate_options_rect(elem[0], elem[1], elem[2], elem[3])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if  event.key == pygame.K_q:
                    game_state = "main_menu"
                elif event.key == pygame.K_DOWN:
                    numer_opcji+=1
                    if numer_opcji > 3:
                        options_positions[numer_opcji - 1][3] = 0
                        numer_opcji = 0
                        options_positions[numer_opcji][3] = 1
                        continue
                    options_positions[numer_opcji][3] = 1
                    options_positions[numer_opcji - 1][3] = 0
                elif event.key == pygame.K_UP:
                    numer_opcji -= 1
                    if numer_opcji < 0:
                        options_positions[numer_opcji + 1][3] = 0
                        numer_opcji = 3
                        options_positions[numer_opcji][3] = 1
                        continue
                    options_positions[numer_opcji][3] = 1
                    options_positions[numer_opcji + 1][3] = 0
                elif event.key == pygame.K_SPACE:
                    options_attributes[opcja[numer_opcji]][0] += 1
                    if options_attributes[opcja[numer_opcji]][0] > options_attributes[opcja[numer_opcji]][1]:
                        options_attributes[opcja[numer_opcji]][0] = 0
                        options_positions[numer_opcji][0] = 323
                    else:
                        options_positions[numer_opcji][0] += options_attributes[opcja[numer_opcji]][2]
            elif event.type == pygame.QUIT:
                running=0
        if not running:
                break
    #obj.draw(screen)
    generate_background(background)
#Animowany napis w menu
    if game_state == "main_menu" and background == titlescreen:
        animated_start(start)
    pygame.display.flip()

pygame.quit()
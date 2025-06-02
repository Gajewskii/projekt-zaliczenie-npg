import pygame
import sys
import random

pygame.init()
# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LINE_COLOR = (10, 10, 10)
RED = (255, 0, 0)

# Rozmiary
SCREEN_SIZE = 600
MARGIN = 20

FONT = pygame.font.SysFont(None, 60)

# Funkcja uruchamiająca grę
def run_game(mode="PvP", size=3):
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("KóK\xf3łko i Krzyżyk")
    board = [[None for _ in range(size)] for _ in range(size)]
    current_player = "X"
    cell_size = SCREEN_SIZE // size
    game_over = False
    winner = None

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

    def draw_board():
        screen.fill(WHITE)
        for row in range(1, size):
            pygame.draw.line(screen, LINE_COLOR, (0, row * cell_size), (SCREEN_SIZE, row * cell_size), 3)
            pygame.draw.line(screen, LINE_COLOR, (row * cell_size, 0), (row * cell_size, SCREEN_SIZE), 3)

        for row in range(size):
            for col in range(size):
                if board[row][col]:
                    text = FONT.render(board[row][col], True, BLACK)
                    rect = text.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2))
                    screen.blit(text, rect)

        if winner:
            end_text = FONT.render(f"Wygral: {winner}", True, RED)
            screen.blit(end_text, end_text.get_rect(center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2)))

        pygame.display.flip()

   

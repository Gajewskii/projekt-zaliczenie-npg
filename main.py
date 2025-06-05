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
    pygame.display.set_caption("Kółko i Krzyżyk")
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

    def check_win():
        # Wiersze i kolumny
        for i in range(size):
             if all(board[i][j] == current_player for j in range(size)):
                return True
             if all(board[j][i] == current_player for j in range(size)):
                return True

        # Przekątne
        if all(board[i][i] == current_player for i in range(size)):
            return True
        if all(board[i][size - i - 1] == current_player for i in range(size)):
            return True

        return False

    def is_board_full():
        return all(cell for row in board for cell in row)

    def ai_move():
        # Prosty losowy ruch
        empty = [(r, c) for r in range(size) for c in range(size) if board[r][c] is None]
        if empty:
            return random.choice(empty)
        return None

    while True:
        draw_board()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                clicked_row = mouseY // cell_size
                clicked_col = mouseX // cell_size

                if board[clicked_row][clicked_col] is None:
                    if mode == "PvP" or (mode == "PvE" and current_player == "X"):
                        board[clicked_row][clicked_col] = current_player
                        if check_win():
                            game_over = True
                            winner = current_player
                        elif is_board_full():
                            game_over = True
                            winner = "Remis"
                        current_player = "O" if current_player == "X" else "X"  

        if mode == "PvE" and current_player == "O" and not game_over:
            pygame.time.wait(500)
            move = ai_move()
            if move:
                board[move[0]][move[1]] = "O"
                if check_win():
                    game_over = True
                    winner = "O"
                elif is_board_full():
                    game_over = True
                    winner = "Remis"
                current_player = "X"

        if game_over:
            draw_board()
            pygame.time.wait(3000)
    return

# Menu graficzne wyboru rozmiaru planszy i trybu gry
def main_menu():
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Menu")
    clock = pygame.time.Clock()
    running = True

    size_buttons = [
        ("3x3", 3, (200, 150)),
        ("4x4", 4, (200, 250)),
        ("5x5", 5, (200, 350)),
    ]

    mode_buttons = [
        ("PvP", (100, 450)),
        ("PvE", (300, 450)),
    ]

    selected_mode = "PvP"

    while running:
        screen.fill(WHITE)
        title = FONT.render("Wybierz rozmiar planszy", True, BLACK)
        screen.blit(title, (50, 50))

        for label, size, pos in size_buttons:
            pygame.draw.rect(screen, LINE_COLOR, (*pos, 200, 60), border_radius=10)
            text = FONT.render(label, True, WHITE)
            text_rect = text.get_rect(center=(pos[0] + 100, pos[1] + 30))
            screen.blit(text, text_rect)

        mode_title = FONT.render("Tryb gry:", True, BLACK)
        screen.blit(mode_title, (50, 400))

        for label, pos in mode_buttons:
            color = RED if selected_mode == label else LINE_COLOR
            pygame.draw.rect(screen, color, (*pos, 150, 50), border_radius=10)
            text = FONT.render(label, True, WHITE)
            text_rect = text.get_rect(center=(pos[0] + 75, pos[1] + 25))
            screen.blit(text, text_rect)

        pygame.display.flip()



            




   

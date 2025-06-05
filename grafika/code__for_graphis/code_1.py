import pygame
import sys

# Initialize
pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Tic-Tac-Toe Menu")

# Load background (your image)
bg = pygame.image.load("/home/piotr/npg_projekt/grafika/menu_glowne/opcja2.png")  # Make sure the image is in the same folder
bg = pygame.transform.scale(bg, (600, 800))

# Font
font = pygame.font.SysFont("pixel", 48)  # Adjust as needed

# Colors
WHITE = (255, 255, 255)
HOVER = (255, 0, 255)

# Button class
class Button:
    def __init__(self, text, rect):
        self.text = text
        self.rect = pygame.Rect(rect)
        self.hovered = False

    def draw(self, screen):
        color = HOVER if self.hovered else WHITE
        pygame.draw.rect(screen, (0, 0, 0), self.rect, border_radius=5)  # optional bg fill
        pygame.draw.rect(screen, color, self.rect, 3, border_radius=5)

        text_surf = font.render(self.text, True, color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_hover(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

# Button layout (positioned like on your image)
buttons = [
    Button("PLAY",    (200, 200, 200, 60)),
    Button("BOARD",   (200, 280, 200, 60)),
    Button("CREDITS", (200, 360, 200, 60)),
    Button("EXIT",    (200, 440, 200, 60)),
]

# Game loop
running = True
while running:
    screen.blit(bg, (0, 0))
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        for btn in buttons:
            if btn.is_clicked(event):
                print(f"{btn.text} clicked")

    for btn in buttons:
        btn.is_hover(mouse_pos)
        btn.draw(screen)

    pygame.display.flip()

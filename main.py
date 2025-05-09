import pygame
import sys

# Inicijalizacija
pygame.init()

# Ekran
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame - Kretanje kvadrata")

# Boje
blue = (0, 0, 128)
red = (192, 10, 0)

# Kvadrat
player_size = 50
player_x = width // 2
player_y = height // 2
player_speed = 5

# Glavna petlja
running = True
while running:
    pygame.time.delay(30)  # Uspori igru malo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tasteri
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Ograniči kretanje unutar ekrana
    player_x = max(0, min(width - player_size, player_x))
    player_y = max(0, min(height - player_size, player_y))

    # Crtanje
    screen.fill(blue)
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))
    pygame.display.flip()

pygame.quit()
sys.exit()


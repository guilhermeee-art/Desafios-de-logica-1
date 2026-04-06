import pygame
import random

# Inicializar
pygame.init()

# Tela
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Shooter")

# Cores
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLACK = (0, 0, 0)

# Player
player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT - 60
player_speed = 6

# Tiro
bullet_x = 0
bullet_y = player_y
bullet_speed = 10
bullet_active = False

# Inimigo
enemy_size = 50
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 50
enemy_speed = 4

# Pontuação
score = 0
font = pygame.font.SysFont(None, 36)

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)
    screen.fill(BLACK)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not bullet_active:
                bullet_x = player_x + player_size // 2
                bullet_y = player_y
                bullet_active = True

    # Movimento
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Movimento do tiro
    if bullet_active:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_active = False

    # Movimento do inimigo
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemy_y = 50

    # Colisão
    if (
        bullet_x > enemy_x and bullet_x < enemy_x + enemy_size and
        bullet_y > enemy_y and bullet_y < enemy_y + enemy_size
    ):
        enemy_x = random.randint(0, WIDTH - enemy_size)
        enemy_y = 50
        bullet_active = False
        score += 1

    # Desenhar player
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))

    # Desenhar inimigo
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_size, enemy_size))

    # Desenhar tiro
    if bullet_active:
        pygame.draw.rect(screen, WHITE, (bullet_x, bullet_y, 5, 10))

    # Pontuação
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
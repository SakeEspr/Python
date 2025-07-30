import pygame
import random

# Initializes Pygame
pygame.init()

# Screen setup
W = 800
H = 600
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Seizure Pong")

# Clock and Font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

# Paddle and Block
paddle = pygame.Rect(W // 2 - 60, H - 20, 60, 10)
block = pygame.Rect(random.randint(0, W - 20), 0, 20, 20)
b_dy = 2  # vertical speed
b_dx = 2  # horizontal speed

# Score
score = 0

# Game loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Paddle movement
    # Paddle movement with wrap-around
    mouse_x, _ = pygame.mouse.get_pos()
    paddle.centerx = mouse_x

    if paddle.right < 0:
        paddle.left = W
    elif paddle.left > W:
        paddle.right = 0

    # Move block
    block.x += b_dx
    block.y += b_dy

    # Bounce off walls
    if block.left <= 0 or block.right >= W:
        b_dx *= -1

    # Bounce off top
    if block.top <= 0:
        b_dy *= -1

    # Bounce off paddle
    if block.colliderect(paddle) and b_dy > 0:
        b_dy *= -1
        score += 1
        b_dy *=1.15
        

    # Game over if block hits bottom
    if block.bottom >= H:
        game_over = font.render("Game Over! Final Score: You Suck", True, (255, 0, 0))
        screen.blit(game_over, (W // 2 - 115, H // 2))
        pygame.display.flip()
        pygame.time.wait(20000)
        running = False

    # Draw everything
    pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), paddle)
    pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), block)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
import pygame
import random
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'  # Center window on screen

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
running = True
game_over = False
flash_mode = False

# Game loop
while running:
    if game_over and flash_mode:
        screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    else: screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                running = False


    # Paddle movement
    # Paddle movement with wrap-around
    mouse_x, _ = pygame.mouse.get_pos()
    paddle.centerx = mouse_x

    if paddle.right < 0:
        paddle.left = W
    elif paddle.left > W:
        paddle.right = 0

    # Gameplay logic if not game over
    if not game_over:
        block.x += b_dx
        block.y += b_dy

        # Bounce off sides
        if block.left <= 0 or block.right >= W:
             b_dx *= -1

        # Bounce off Top
        if block.top <= 0:
            b_dy *= -1

        # Bounce off Paddle
        if block.colliderect(paddle) and b_dy > 0:
            b_dy *= -1
            score += 1
            b_dy *=1.15

        if block.bottom >= H:
            game_over = True
            screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            flash_mode = True
        
    # Draw everything
    pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), paddle)
    pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), block)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    # Game over if block hits bottom




    pygame.display.flip()
    clock.tick(60)

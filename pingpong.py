import pygame
import random

# Mängu seaded
WIDTH = 640
HEIGHT = 480
FPS = 60
BACKGROUND_COLOR = (240, 240, 240)
BALL_SIZE = 20
BALL_SPEED = 5
PADDLE_WIDTH = 120
PADDLE_HEIGHT = 20
PADDLE_SPEED = 5

# Initsialiseeri Pygame'i
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pall ja alus mäng")
clock = pygame.time.Clock()

# Mängu elemendid
ball = pygame.Rect(WIDTH / 2 - BALL_SIZE / 2, HEIGHT / 2 - BALL_SIZE / 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED * random.choice((1, -1))
ball_speed_y = BALL_SPEED * random.choice((1, -1))
paddle = pygame.Rect(WIDTH / 2 - PADDLE_WIDTH / 2, HEIGHT / 1.5, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 0

# Mängu loop
running = True
score = 0
while running:
    # Sündmuste loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed = -PADDLE_SPEED
            elif event.key == pygame.K_RIGHT:
                paddle_speed = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_speed = 0

    # Liiguta palli
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Põrkumine seintega
    if ball.right >= WIDTH or ball.left <= 0:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    if ball.bottom >= HEIGHT:
        score -= 1
        ball.center = (WIDTH / 2, HEIGHT / 2)
        ball_speed_x = BALL_SPEED * random.choice((1, -1))
        ball_speed_y = BALL_SPEED * random.choice((1, -1))

    # Põrkumine alusega
    if ball.colliderect(paddle) and ball_speed_y > 0:
        score += 1
        ball_speed_y *= -1

    # Liiguta alust
    paddle.x += paddle_speed
    if paddle.left < 0:
        paddle.left = 0
    if paddle.right > WIDTH:
        paddle.right = WIDTH

    # Joonista ekraanile
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, (0, 0, 0), paddle)
    pygame.draw.ellipse(screen, (0, 0, 0), ball)
    score_text = pygame.font.SysFont(None, 24).render("Score: {}".format(score), True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

    # Piiritle FPS
    clock.tick(FPS)

# Lõpeta Pygame'i
pygame.quit()

# impordib erinevad asjad
import pygame
import time
import random
# ussi liikumiskiiurs
snake_speed = 15
# ekraani suurus
window_x = 720
window_y = 480

# defineerib värvid
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# paneb mängu tööle
pygame.init()

# apply'b ekraani suuruse ning mängu nime
pygame.display.set_caption('snakegame_otthubel')
game_window = pygame.display.set_mode((window_x, window_y))

# fps kontroller
fps = pygame.time.Clock()

# defineerib ussi alustamispunkti
snake_position = [100, 50]

# defineerib esimseed 4 ussi kehablokki
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# ussi marja asukoht
fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# seadistab ussi algse suuna paremale
direction = 'RIGHT'
change_to = direction

# alustamise skoor
score = 0


# skoori funktsioon
def show_score(choice, color, font, size):
    # loob fonti
    score_font = pygame.font.SysFont(font, size)

    # loob skoori tausta ning kirja enda
    score_surface = score_font.render('Skoor : ' + str(score), True, color)

    # loob ristküliku kujulise kujundi skoori jaoks
    score_rect = score_surface.get_rect()

    # kuvab teksti
    game_window.blit(score_surface, score_rect)


# mängus surma saamise funktsioon
def game_over():
    # loob uue fondi
    my_font = pygame.font.SysFont('times new roman', 50)

    # loob pinna kuhu tekst peale kirjutatakse
    game_over_surface = my_font.render(
        'Sinu skoor on : ' + str(score), True, red)

    # loob ristküliku kujulise objekti teksti jaoks
    game_over_rect = game_over_surface.get_rect()

    # määrab teksti positsiooni
    game_over_rect.midtop = (window_x / 2, window_y / 4)

    # tekst kuvatakse ekraanile
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # 2 sekundi möödumisel suletakse mäng
    time.sleep(2)

    # sulgeb pygame'i
    pygame.quit()

    # sulgub täielikult
    quit()


# põhifunktsioon
while True:

    # tegeleb põhifunktsioonidega mängus nagu näiteks liikumine
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # kahte nuppu korraga vajutades me ei taha et uss iseendasse läheks
    # seega me loome koodi selleks et ta kahte nuppu korraga all hoides ei liiguks

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # ussi liikumine
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # ussi keha kasvamise mehhanism
    # kui uss sööb ühe maiuse ära siis kasvab 1 bloki võrra ning lisatakse 10 punkti skoorile juurde
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))

    # mängus surmasaamise funktsioon
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    # ussi enda kehasse jooksmine
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # skoori näitamine jooksvalt
    show_score(1, white, 'times new roman', 20)

    # mängu ekraani värskendamine
    pygame.display.update()

    # ussi frames per second speed
    fps.tick(snake_speed)

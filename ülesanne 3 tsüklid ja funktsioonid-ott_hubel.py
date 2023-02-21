import pygame

# Määrab ekraani suuruse
screen_width = 640
screen_height = 480

# initsialiseerige pygame ja looge ekraan
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ülesanne 3: Tsüklid ja funktsioonid")

# Määrab värvid
GREEN = (153, 255, 153)
RED = (255, 0, 0)

def draw_squares(size, rows, cols, color):
    """
    Joonistab ruudud, et täita ekraani etteantud suuruse, ridade ja veergude arvu ning joone värviga.
    """
    screen.fill(RED)
    y = 0
    for row in range(rows):
        x = 0
        for col in range(cols):
            pygame.draw.rect(screen, color, (x, y, size, size), 1)
            x += size
        y += size

    # Uuendab ekraani
    pygame.display.flip()

# määrab funktsioonile parameetrid
square_size = 30
num_rows = screen_height // square_size
num_cols = screen_width // square_size
line_color = GREEN

# kutsub välja joonistus_ruudud
draw_squares(square_size, num_rows, num_cols, line_color)

# Paneb mängu tsüklisse ehk loopi
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

# Lahkub PyGamest
pygame.quit()
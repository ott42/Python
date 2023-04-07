import pygame # importeerime pygame

pygame.init() # initsialiseerime pygame'i

screen = pygame.display.set_mode((640, 480)) # loome akna, kus mäng hakkab jooksma
pygame.display.set_caption("Merchant Mike Oxlong") # seame akna pealkirja
screen.fill((234, 105, 241)) # täidame akna värviga

bg = pygame.image.load('img/bg_shop.jpg') # laeme taustapildi
screen.blit(bg, (0, 0)) # kuvame taustapildi

seller = pygame.image.load('img/seller.png') # laeme müüja pildi
seller = pygame.transform.scale(seller, (250, 300)) # skaalame müüja pildi sobivaks
screen.blit(seller, (60, 150)) # kuvame müüja pildi

chat_box = pygame.image.load('img/chat.png') # laeme rääkimisakna pildi
chat_box = pygame.transform.scale(chat_box, (250, 200)) # skaalame rääkimisakna sobivaks
screen.blit(chat_box, (200, 75)) # kuvame rääkimisakna

font = pygame.font.Font(pygame.font.match_font('Arial'), 25) # valime fondi ja selle suuruse
text = font.render("Hello, Im Ott", True, (255, 255, 255)) # loome teksti

text_width, text_height = text.get_size() # arvutame teksti suuruse
screen.blit(text, (225, 150)) # kuvame tekstitahvli

vykk_logo = pygame.image.load('img/VIKK logo.png') # laeme VIKK logo pildi
vykk_logo = pygame.transform.scale(vykk_logo, (300, 50)) # skaalame logo sobivaks
screen.blit(vykk_logo, (0, 0)) # kuvame logo

cake = pygame.image.load('img/cake.png') # laeme kooki pildi
cake = pygame.transform.scale(cake, (100, 100)) # skaalame kooki sobivaks
screen.blit(cake, (436, 200)) # kuvame koogi

sword = pygame.image.load('img/Mõõk.png') # laeme mõõga pildi
sword = pygame.transform.smoothscale(sword, (40, 37)) # skaalame mõõga sobivaks
screen.blit(sword, (390, 325)) # kuvame mõõga

pygame.draw.line(screen, (255, 255, 255), (2, 2), (295, 2), 1) # joonistame valge joone
pygame.draw.line(screen, (255, 255, 255), (2, 50), (295, 50), 1) # joonistame valge joone
pygame.draw.line(screen, (255, 255, 255), (2, 2), (2, 50), 1) # joonistame valge joone
pygame.draw.line(screen, (255, 255, 255), (265, 2), (265, 50), 1) # joonistame valge joone
pygame.display.flip()

# võimaldab mängu ristist kinnipanekut
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
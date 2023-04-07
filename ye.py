def is_collision(rect1, rect2):
    return rect1.colliderect(rect2)


red_car_rect = pygame.Rect(punaneposx, 310, 60, 150)
blue_car_rect1 = pygame.Rect(sinine_posx, sinine_posy, 60, 150)
blue_car_rect2 = pygame.Rect(sinine_posx2, sinine_posy2, 60, 150)


if is_collision(red_car_rect, blue_car_rect1) or is_collision(red_car_rect, blue_car_rect2):
    print("Collision detected!")


red_car_rect = pygame.Rect(punaneposx + 10, 310, 40, 130)
blue_car_rect1 = pygame.Rect(sinine_posx + 10, sinine_posy + 10, 40, 130)
blue_car_rect2 = pygame.Rect(sinine_posx2 + 10, sinine_posy2 + 10, 40, 130)
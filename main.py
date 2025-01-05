import pygame
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((400,600))
background = pygame.image.load("DodgeGame/Images/Road.png")
background = pygame.transform.scale(background,(400,600))

car = pygame.image.load("DodgeGame/Images/Car Sprite.png")
car = pygame.transform.scale(car,(125,175))
car_rect = car.get_rect()
car_rect.x = 150
car_rect.y = 350

clock = pygame.time.Clock()

while True:
    screen.blit(background,(0,0))
    screen.blit(car,car_rect)
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        car_rect.x -= 5
    elif key[pygame.K_d]:
        car_rect.x += 5

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
   
    pygame.display.flip()
    clock.tick(60)

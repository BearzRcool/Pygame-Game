import pygame
import random
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((400,600))
background = pygame.image.load("Images/Road.png")
background = pygame.transform.scale(background,(400,600))

car = pygame.image.load("Images/Car Sprite.png")
car = pygame.transform.scale(car,(60,100))
car_rect = car.get_rect()
car_rect.x = 150
car_rect.y = 350

obstacle = pygame.image.load("Images/Car Obstacle.PNG")
obstacle = pygame.transform.scale(obstacle,(60,100))
obstacle_rect = obstacle.get_rect()
obstacle_rect.x = 100
obstacle_rect.y = 200


clock = pygame.time.Clock()
def choice():
    choice = random.randint(1,4)
    if choice == 1:
        choice = 80
    elif choice == 2:
        choice = 140
    elif choice == 3:
        choice = 200
    elif choice == 4:
        choice = 260
    return choice
def update():
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        car_rect.x -= 5
    elif key[pygame.K_d]:
        car_rect.x += 5
    elif key[pygame.K_s]:
        car_rect.y += 5
    elif key[pygame.K_w]:
        car_rect.y -= 5

    if car_rect.x < 65:
        car_rect.x = 65
    elif car_rect.x > 280:
        car_rect.x = 280
    if car_rect.y < 200:
        car_rect.y = 200
    elif car_rect.y > 445:
        car_rect.y = 445

    obstacle_rect.y+=3
    
    if obstacle_rect.y >600:
        obstacle_rect.y = 10
        lane = choice()
        obstacle_rect.x = lane
while True:
    screen.blit(background,(0,0))
    screen.blit(car,car_rect)
    screen.blit(obstacle,obstacle_rect)

    

    
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    print(car_rect.x)
    update()
    pygame.display.flip()
    clock.tick(60)

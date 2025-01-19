import pygame
import random

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((400, 600))
background = pygame.image.load("Images/Road.png")
background = pygame.transform.scale(background, (400, 600))

lanes = [80, 140, 200, 260]

car = pygame.image.load("Images/Car Sprite.png")
car = pygame.transform.scale(car, (60, 100))
car_rect = car.get_rect()
car_rect.x = lanes[1]
car_rect.y = 350

clock = pygame.time.Clock()


def choice():
    choice = random.randint(1, 4)
    if choice == 1:
        choice = 80
    elif choice == 2:
        choice = 140
    elif choice == 3:
        choice = 200
    elif choice == 4:
        choice = 260
    return choice


class Car():

    def __init__(self, CarColor):
        self.speed = 3
        startY = 0
        if CarColor == 1:
            self.Car = pygame.image.load("Images/Car Obstacle.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
            startY = 0
        elif CarColor == 2:
            self.Car = pygame.image.load("Images/Car Obstacle 2.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
            startY = 30
        elif CarColor == 3:
            self.Car = pygame.image.load("Images/Car Obstacle 3.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
            startY = 50
        elif CarColor == 4:
            self.Car = pygame.image.load("Images/Car Obstacle 4.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
            startY = 15
        elif CarColor == 5:
            self.Car = pygame.image.load("Images/Car Obstacle 5.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
            startY = 60

        self.Car_rect = self.Car.get_rect()
        self.Car_rect.x = choice()
        self.Car_rect.y = startY

    def CarUpdate(self):

        screen.blit(self.Car, self.Car_rect)
        key = pygame.key.get_pressed()

        if key[pygame.K_s]:
            self.speed -= 1
        elif key[pygame.K_w]:
            self.speed += 1
        self.Car_rect.y += self.speed

        if self.Car_rect.y > 600:
            self.Car_rect.y = -50
            self.Car_rect.x = choice()


current_lane = 1


def update():
    global car_rect

    car_rect.x = lanes[current_lane]
    if car_rect.x < 65:
        car_rect.x = 65
    elif car_rect.x > 280:
        car_rect.x = 280
    if car_rect.y < 200:
        car_rect.y = 200
    elif car_rect.y > 445:
        car_rect.y = 445


OrangeCar = Car(1)
GreenCar = Car(2)

while True:
    screen.blit(background, (0, 0))
    screen.blit(car, car_rect)
    OrangeCar.CarUpdate()
    GreenCar.CarUpdate()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_a:
                current_lane -= 1
                print("test")
            elif event.type == pygame.K_d:
                current_lane += 1
                print("test")
    update()
    pygame.display.flip()
    clock.tick(60)

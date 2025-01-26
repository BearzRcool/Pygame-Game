import pygame
import random
import time

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((400, 600))
background1 = pygame.image.load("Images/road#1.PNG")
background1 = pygame.transform.scale(background1, (400, 600))
background2 = pygame.image.load("Images/road#2.PNG")
background2 = pygame.transform.scale(background2, (400,600))
background3 = pygame.image.load("Images/road#3.PNG")
background3 = pygame.transform.scale(background3, (400,600))

backgrounds = [background1,background2,background3]

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
        self.speed = 5
        startY = 0
        if CarColor == 1:
            self.Car = pygame.image.load("Images/Car Obstacle.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
            startY = 0
        elif CarColor == 2:
            self.Car = pygame.image.load("Images/Car Obstacle 2.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
            startY = -30
            self.speed = 7
        elif CarColor == 3:
            self.Car = pygame.image.load("Images/Car Obstacle 3.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
            startY = -50
            self.speed = 9
        elif CarColor == 4:
            self.Car = pygame.image.load("Images/Car Obstacle 4.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
            startY = -60
        elif CarColor == 5:
            self.Car = pygame.image.load("Images/Car Obstacle 5.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
            startY = 60
            self.speed = 2

        self.Car_rect = self.Car.get_rect()
        self.Car_rect.x = choice()
        self.Car_rect.y = startY

    def CarUpdate(self):

        screen.blit(self.Car, self.Car_rect)
        key = pygame.key.get_pressed()



        self.Car_rect.y += self.speed

        if self.Car_rect.y > 600:
            self.Car_rect.y = -50
            self.Car_rect.x = choice()


def Animations():
    for background in backgrounds:
        
    

current_lane = 1


def ExtraUpdates():
    global car_rect
    global current_lane
    if current_lane < 0:
        current_lane += 1
    elif current_lane > 3:
        current_lane -= 1

    car_rect.x = lanes[current_lane]




time1 = time.time()
GreenCar = Car(2)
TangerineCar = Car(3)
BlueCar = Car(4)

while True:
    print(current_lane)
    ExtraUpdates()
    screen.blit(background1, (0, 0))
    screen.blit(car, car_rect)
    
    GreenCar.CarUpdate()
    TangerineCar.CarUpdate()
    BlueCar.CarUpdate()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                current_lane -= 1
       
            elif event.key == pygame.K_d:
                current_lane += 1
    time2 = time.time()
    if time2 - time1 >= 3:

        Animations()
    pygame.display.flip()
    clock.tick(60)

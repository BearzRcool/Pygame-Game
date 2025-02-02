import pygame
import random
import time

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((400, 600))
background = pygame.image.load("Images/road#1.PNG")
background = pygame.transform.scale(background, (400, 600))
background1 = pygame.image.load("Images/road#1.PNG")
background1 = pygame.transform.scale(background1, (400, 600))
background2 = pygame.image.load("Images/road#2.PNG")
background2 = pygame.transform.scale(background2, (400,600))
background3 = pygame.image.load("Images/road#3.PNG")
background3 = pygame.transform.scale(background3, (400,600))
background4 = pygame.image.load("Images/road#4.PNG")
background4 = pygame.transform.scale(background4, (400,600))
background5 = pygame.image.load("Images/road#5.PNG")
background5 = pygame.transform.scale(background5, (400,600))
background6 = pygame.image.load("Images/road#6.PNG")
background6 = pygame.transform.scale(background6, (400,600))
background6 = pygame.image.load("Images/road#6.PNG")
background6 = pygame.transform.scale(background6, (400,600))
background7 = pygame.image.load("Images/road#7.PNG")
background7 = pygame.transform.scale(background7, (400,600))
background8 = pygame.image.load("Images/road#8.PNG")
background8 = pygame.transform.scale(background8, (400,600))

backgrounds = [background1,background2,background3,background4,background5,background6,background7,background8]

lanes = [44, 125, 212, 296]

car = pygame.image.load("Images/Car Sprite.png")
car = pygame.transform.scale(car, (60, 100))
car_rect = car.get_rect()
car_rect.x = lanes[1]
car_rect.y = 350

clock = pygame.time.Clock()


def choice():
    choice = random.randint(1, 4)
    if choice == 1:
        choice = 44
    elif choice == 2:
        choice = 125
    elif choice == 3:
        choice = 212
    elif choice == 4:
        choice = 296
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

    def CarUpdate(self,CarColor):


        screen.blit(self.Car, self.Car_rect)

        



        self.Car_rect.y += self.speed

        if self.Car_rect.y > 600:
            self.Car_rect.y = -50
            self.Car_rect.x = choice()
            if CarColor == 1:
                    
                self.Car = pygame.image.load("Images/Car Obstacle.PNG")
                self.Car = pygame.transform.scale(self.Car, (60, 100))

                self.speed = 5
                
            elif CarColor == 2:
                self.Car = pygame.image.load("Images/Car Obstacle 2.PNG")
                self.Car = pygame.transform.scale(self.Car, (60, 100))
            
                self.speed = 7
            elif CarColor == 3:
                self.Car = pygame.image.load("Images/Car Obstacle 3.PNG")
                self.Car = pygame.transform.scale(self.Car, (60, 100))
                
                self.speed = 9
            elif CarColor == 4:
                self.Car = pygame.image.load("Images/Car Obstacle 4.PNG")
                self.Car = pygame.transform.scale(self.Car, (60, 100))

                self.speed = 5
                
            elif CarColor == 5:
                self.Car = pygame.image.load("Images/Car Obstacle 5.PNG")
                self.Car = pygame.transform.scale(self.Car, (60, 100))
                
                self.speed = 3

i = 0
        
start_time = time.time()
def Animations():
   global start_time, i
   current_time = time.time() 
   if current_time - start_time >= 0.05:
        if i < 7:
           i += 1
        else:
           i = 0
        start_time = time.time()
    



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
Car1 = Car(2)
Car2 = Car(3)
Car3 = Car(4)

while True:
    ExtraUpdates()
    Animations()
    screen.blit(backgrounds[i], (0, 0))
    screen.blit(car, car_rect)

    Car1Type = random.randint(1,5)
    Car2Type = random.randint(1,5)
    Car3Type = random.randint(1,5)

    # if Car1Type == Car2Type or Car1Type == Car3Type:
    #     Car1.CarUpdate(Car1Type)

    
    # elif Car2Type == Car1Type or Car2Type == Car3Type:
    #     Car2Type = random.randint(1,5)
    #     Car2.CarUpdate(Car2Type)

    
    # elif Car3Type == Car1Type or Car3Type == Car2Type:
    #     Car3Type = random.randint(1,5)
   
    Car3.CarUpdate(Car3Type)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                current_lane -= 1
       
            elif event.key == pygame.K_d:
                current_lane += 1

    #hold = pygame.key.get_pressed()
    # if hold[pygame.K_a]:
    #     car_rect.x -= 3
    # elif hold[pygame.K_d]:
    #     car_rect.x += 3
    pygame.display.flip()
    clock.tick(60)

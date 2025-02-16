import pygame
import random
import time

pygame.init()
pygame.display.init()
screen = pygame.display.set_mode((400, 600))
# background images for creating moving road animation
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
# x-coordinates for all of the lanes.
lanes = [44, 125, 212, 296]



# defining the player character car
car = pygame.image.load("Images/Car Sprite.png")
car = pygame.transform.scale(car, (60, 100))
car_rect = car.get_rect()
car_rect.x = lanes[1]
car_rect.y = 350

clock = pygame.time.Clock()


# point system
end = time.time()
points = 0
start = time.time()
def PointSystem():
    global end
    global points
    global start
    
    if end - start >= 1:
        points += 1
        start = time.time()
        points += 1
    end = time.time()
# text
text = pygame.font.SysFont("Noto Sans", 30)
printer = text.render("SCORE: " + str(points), True, (0,0,0))
score = pygame.Surface((100, 100))


# randomly choosing lanes for the obstacle cars
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

# class defines Car obstacles in the game
class Car():

    def __init__(self):
        self.speed = 5

        self.CarColor = random.randint(1,5)
        if self.CarColor == 1:
            self.Car = pygame.image.load("Images/Car Obstacle.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))

        elif self.CarColor == 2:
            self.Car = pygame.image.load("Images/Car Obstacle 2.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
   
            self.speed = 7
        elif self.CarColor == 3:
            self.Car = pygame.image.load("Images/Car Obstacle 3.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
    
            self.speed = 9
        elif self.CarColor == 4:
            self.Car = pygame.image.load("Images/Car Obstacle 4.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
   
        elif self.CarColor == 5:
            self.Car = pygame.image.load("Images/Car Obstacle 5.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
 
            self.speed = 2

        self.Car_rect = self.Car.get_rect()
        self.Car_rect.x = choice()
        self.Car_rect.y = -50

    def CarUpdate(self):
        screen.blit(self.Car, self.Car_rect)
        self.Car_rect.y += self.speed

     
            
    #def SwitchColors(self):

# For animations
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
# keeps the player within each of the lanes
def ExtraUpdates():
    global car_rect
    global current_lane
    if current_lane < 0:
        current_lane += 1
    elif current_lane > 3:
        current_lane -= 1
    car_rect.x = lanes[current_lane]
   
cars = [Car(), Car(), Car()]
while True:
    ExtraUpdates()
    Animations()
    screen.blit(backgrounds[i], (0, 0))
    screen.blit(car, car_rect)
    screen.blit(score, (0,0))

    for obstacle in cars:
        obstacle.CarUpdate()
        if obstacle.Car_rect.y > 600:
            cars.remove(obstacle)
            cars.append(Car())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                current_lane -= 1
       
            elif event.key == pygame.K_d or event.key == pygame.K_:
                current_lane += 1

    PointSystem()
  
    pygame.display.flip()
    clock.tick(60)
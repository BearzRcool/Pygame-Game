import pygame
import random
import time
import os
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
lanes = [42, 120, 210, 294]
# extra
invincibility_start = False

HSCoreR = open("score.txt","r")
HighScore = HSCoreR.read()
HSCoreR.close()



# defining the player character car
car = pygame.image.load("Images/Car Sprite.png")
car = pygame.transform.scale(car, (60, 100))
car_rect = car.get_rect()
car_rect.x = lanes[1]
car_rect.y = 350

clock = pygame.time.Clock()


move_switch_right = False
move_switch_left = False

# point system
end = time.time()
points = 0
start = time.time()
def PointSystem():
    global end
    global points
    global start
    global printer
    
    if end - start >= 1:
        points += 1
        start = time.time()
        printer = text.render("SCORE: " + str(points), True, (0,0,0))
    end = time.time()
# text
text = pygame.font.SysFont("Mojangles", 30)
printer = text.render("SCORE: " + str(points), True, (0,0,0))
inv_text = text.render("INV for: " + str(invinciblity_start), True, (0,0,0))
HSText = text.render("HS: "+ str(HighScore), True, (0,0,0))





# randomly choosing lanes for the obstacle cars
def choice():
    choice = random.randint(1, 4)
    if choice == 1:
        choice = 42
    elif choice == 2:
        choice = 120
    elif choice == 3:
        choice = 210
    elif choice == 4:
        choice = 294
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
   
            self.speed = 5
        elif self.CarColor == 3:
            self.Car = pygame.image.load("Images/Car Obstacle 3.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
    
            self.speed = 7
        elif self.CarColor == 4:
            self.Car = pygame.image.load("Images/Car Obstacle 4.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
   
        elif self.CarColor == 5:
            self.Car = pygame.image.load("Images/Car Obstacle 5.PNG")
            self.Car = pygame.transform.scale(self.Car, (60, 100))
 
            self.speed = 2

        self.Car_rect = self.Car.get_rect()
        self.Car_rect.x = choice()
        # if end - start > 3:
        #     if self.Car_rect.x == 120:
        #         self.Car_rect.x = choice()
        self.Car_rect.y = -50

    def CarUpdate(self):
        screen.blit(self.Car, self.Car_rect)
        self.Car_rect.y += self.speed

     
#ability
invincible = False
invincibility_timer_start = 0
invincibility_time = 6
def Ability():
    global invincible, invinciblity_start, points, invincibility_time, invincibility_timer_start, inv_text
    if invincibility_timer_start:
        elapsed = time.time() - invincibility_timer_start
        invincible_for = max(0,invincibility_time - elapsed)

        if elapsed < invincibility_time:
            invincible = True
            invincible_for = int(invincible_for)
            inv_text = text.render("INV for: " + str(invincible_for), True, (0,0,0))
            text2 = pygame.font.SysFont("Mojangles", 100)
            inv_text2 = text2.render(str(invincible_for), True, (255,255,255))
            screen.blit(inv_text2, (180,250))

        else:
            invincible = False
            invincibility_timer_start = 0

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
    
        


# keeps the player within each of the lanes
current_lane = 1
def ExtraUpdates():
    global car_rect
    global current_lane
    global move_switch_left
    global move_switch_right
    print ("left " + str(move_switch_left))
    print ("right " + str(move_switch_right))
    
    
    if move_switch_right == True:
        if car_rect.x >= 294: 
            move_switch_right == False
        else: 
            car_rect.x += 6
    if move_switch_left == True:
        if car_rect.x <= 42:
            move_switch_left == False
        else: 
            car_rect.x -= 6
    if car_rect.x in lanes or car_rect.x >= 294 or car_rect.x <= 42:
        move_switch_right = False
        move_switch_left = False
    

cars = [Car(), Car(), Car()]

cooldown_start = time.time()
while True:
    os.system('cls')
    ExtraUpdates()
    Animations()
    screen.blit(backgrounds[i], (0, 0))
    screen.blit(car, car_rect)
    screen.blit(printer, (0,0))
    
    screen.blit(inv_text, (0,20))
    screen.blit(HSText, (0,40))
    
    if car_rect.x in lanes:
        pass
    for obstacle in cars:
        obstacle.CarUpdate()
        if obstacle.Car_rect.y > 600:
            cars.remove(obstacle)
            cars.append(Car())
            #collision check:
        if obstacle.Car_rect.colliderect(car_rect) and not invincible:

            HSCoreR = open("score.txt","r")
            if int(HSCoreR.read()) < points:
                HSCoreR.close()
                HSCoreW = open("score.txt", "w")
                HSCoreW.write(str(points))
                HSCoreW.close()

            pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        elif event.type == pygame.KEYDOWN:
            move_switch_right = False
            move_switch_left = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                move_switch_left = True
            
       
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                move_switch_right = True

            if event.key == pygame.K_SPACE:
                if not invincible:
                    invincibility_timer_start = time.time()
                 
    
    
    print("Invinsible: " + str(invincible))
    print("Start: " + str(start))
    
    Ability()
    PointSystem()
  
    pygame.display.flip()
    clock.tick(60)
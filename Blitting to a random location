#Kris Shields ETGG1801 Lab 08
##4/4: Get, adjust, and organize the assets (floor, princess, heart, font)
##3/3: Make a window and draw the background
##7/7: Draw the two hearts [2] and the partial heart [5]
##5/7: Pick and draw a random animation frame and draw centered
##Your perimeter idea is a good one. Just make sure once you’ve chosen your point that you center the sprite around it (in this case)
##5/5: Show (least some of) the stats using a font object
#import modules
import pygame
pygame.init()
import random
import time

#draw pygame window
win_x = 800
win_y = 600
win_dim = (win_x,win_y)
win = pygame.display.set_mode(win_dim)

#load assets
wood = pygame.image.load("Images\Wood.jpg")
heart = pygame.image.load("Images\Heart.png")
princess = pygame.image.load("Images\Princess.jpg")

#draw objects
win.blit(wood,(0,0))
win.blit(heart,(736,0))
win.blit(heart,(704,0))

#draw the random heart
heart_percent = random.uniform(8,32) #to prevent the edge case where none of the heart is displayed
#but in reality a very small amount of the heart was selected (cropping out transparent pixels)
win.blit(heart,(768,0),(0,0,heart_percent,32))
heart_percent100 = 100*heart_percent/32
heart_percent100_rounded = round(2+heart_percent100/100,2)

#figure out the princess things
sprite_size = 96
direction = random.randint(0,7) #needs to be 0-7 to allow it to call sprites from 1st column and row
frame = random.randint(0,7) #and prevent calling from an inaccessible 9th row and column
x = random.randint(48,752) #creating a "perimeter" where the sprite cannot be drawn to prevent overlap with hearts/text
y = random.randint(48,552) #and to prevent being partially drawn off-screen
win.blit(princess,(x,y),(direction*96,frame*96,sprite_size,sprite_size))

#font things
font_obj= pygame.font.Font("Fonts/Roboto-Thin.ttf",16)
temp_surface = font_obj.render(f"Player X: {direction*96}, Player Y: {frame*96}, Player Health: {heart_percent100_rounded}",False,((255,255,0)))
win.blit(temp_surface,(0,0))

#ending things
pygame.display.flip()
time.sleep(3)
pygame.quit()

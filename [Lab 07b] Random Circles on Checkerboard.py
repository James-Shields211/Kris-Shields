#Kris Shields ETGG1801 Lab 07B

#import necessary modules
import pygame
import random
pygame.init()

##12/12: [5] checkboard, [5] lines, [2] knuckles and line-width

#draw a window
window_width = random.randint(200,800)
window_height = random.randint(200,800)
window_dim = (window_width,window_height)
window = pygame.display.set_mode(window_dim)
thwindow_x = int(window_width / 3)
thwindow_y = int(window_height / 3)
#define colors
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
orange = (254,143,1)
yellow = (254,242,0)
green = (36,181,80)
blue = (16,96,255)
indigo = (117,66,255)
violet = (122,31,160)
magenta = (247,0,247)
#draw checkerboard pattern
pygame.draw.polygon(window,white,[(thwindow_x,0),(thwindow_x,thwindow_y),(2*thwindow_x,thwindow_y),(2*thwindow_x,0)],0)
pygame.draw.polygon(window,white,[(0,thwindow_y),(thwindow_x,thwindow_y),(thwindow_x,2*thwindow_y),(0,2*thwindow_y)],0)
pygame.draw.polygon(window,white,[(2*thwindow_x,thwindow_y),(2*thwindow_x,2*thwindow_y),(3*thwindow_x,2*thwindow_y),(3*thwindow_x,thwindow_y)],0)
pygame.draw.polygon(window,white,[(thwindow_x,2*thwindow_y),(2*thwindow_x,2*thwindow_y),(2*thwindow_x,3*thwindow_y),(thwindow_x,3*thwindow_y)],0)
#pick random point in each square
top_left = ((random.randint(0,thwindow_x),random.randint(0,thwindow_y)))
top_middle = ((random.randint(thwindow_x,2*thwindow_x),random.randint(0,thwindow_y)))
top_right = ((random.randint(2*thwindow_x,3*thwindow_x),random.randint(0,thwindow_y)))
middle_left = ((random.randint(0,thwindow_x),random.randint(thwindow_y,2*thwindow_y)))
middle_right = ((random.randint(2*thwindow_x,3*thwindow_x),random.randint(thwindow_y,2*thwindow_y)))
bottom_left = ((random.randint(0,thwindow_x),random.randint(2*thwindow_y,3*thwindow_y)))
bottom_middle = ((random.randint(thwindow_x,2*thwindow_x),random.randint(2*thwindow_y,3*thwindow_y)))
bottom_right = ((random.randint(2*thwindow_x,3*thwindow_x),random.randint(2*thwindow_y,3*thwindow_y)))
#connect the dots
pygame.draw.line(window,red,top_left,top_middle,random.randint(2,10))
pygame.draw.line(window,orange,top_middle,top_right,random.randint(2,10))
pygame.draw.line(window,yellow,top_right,middle_right,random.randint(2,10))
pygame.draw.line(window,green,middle_right,bottom_right,random.randint(2,10))
pygame.draw.line(window,blue,bottom_right,bottom_middle,random.randint(2,10))
pygame.draw.line(window,indigo,bottom_middle,bottom_left,random.randint(2,10))
pygame.draw.line(window,violet,bottom_left,middle_left,random.randint(2,10))
pygame.draw.line(window,magenta,middle_left,top_left,random.randint(2,10))
#draw the cicles
pygame.draw.circle(window,white,(top_left),random.randint(11,20))
pygame.draw.circle(window,black,(top_middle),random.randint(11,20))
pygame.draw.circle(window,white,(top_right),random.randint(11,20))
pygame.draw.circle(window,black,(middle_left),random.randint(11,20))
pygame.draw.circle(window,black,(middle_right),random.randint(11,20))
pygame.draw.circle(window,white,(bottom_left),random.randint(11,20))
pygame.draw.circle(window,black,(bottom_middle),random.randint(11,20))
pygame.draw.circle(window,white,(bottom_right),random.randint(11,20))
#ending things
pygame.display.flip()
import time
time.sleep(3)
pygame.quit()

#Kris Shields ETGG 1801 Lab 07a
#idea: Draw tricorn loosely centered, draw class sigils around it
#Warlock sigil: 1 triangle, 1 diamond, 4 rectangles (ttl6)
#Hunter sigil: 6 rectangles (ttl6)
#Titan sigil:  2 triangles, 2 diamonds (ttl 4)
#Total: 16 shapes, probably 2-4 for tricorn

##15/12: Lab07a (4 types, 30+ shapes, make something, stay open 3 seconds, +5 option)
    ##The shadows are very nice!
import pygame
pygame.init()
#Draw window
window_dim = (800,800)
window = pygame.display.set_mode(window_dim)
#colors
white = (255,255,255)
void = (158,109,188)
dvoid = (71,49,138)
arc =(155,205,238)
darc =(103,182,191)
dsolar =(239,125,53)
solar = (233,140,45)
"""
#colors test (not to be used in final)
pygame.draw.circle(window, void,(100,100),50)
pygame.draw.circle(window, dvoid,(200,200),50)
pygame.draw.circle(window, arc,(300,300),50)
pygame.draw.circle(window, darc,(400,400),50)
pygame.draw.circle(window, solar, (500,500),50)
pygame.draw.circle(window, solar, (600,600),50)
"""
#Warlock Sigil Overlay
#center lower triangle
pygame.draw.polygon(window,dvoid,[(410,110),(370,150),(450,150)],0)

#directly left of center triangle
pygame.draw.polygon(window,dvoid,[(400,100),(390,90),(335,150),(360,150)],0)

#leftmost rectangle
pygame.draw.polygon(window,dvoid,[(380,80),(370,70),(295,150),(320,150)],0)

#directly right of center triangle
pygame.draw.polygon(window,dvoid,[(420,100),(430,90),(485,150),(460,150)],0) 

#rightmost rectangle
pygame.draw.polygon(window,dvoid,[(440,80),(450,80),(525,150),(500,150)],0) 

#diamond on top
pygame.draw.polygon(window,dvoid,[(410,100),(370,60),(410,20),(450,60)],0)

#Warlock sigil (placed above) Void
#center lower triangle
pygame.draw.polygon(window,void,[(400,100),(360,140),(440,140)],0)

#directly left of center triangle
pygame.draw.polygon(window,void,[(390,90),(380,80),(325,140),(350,140)],0)

#leftmost rectangle
pygame.draw.polygon(window,void,[(370,70),(360,60),(285,140),(310,140)],0)

#directly right of center triangle
pygame.draw.polygon(window,void,[(410,90),(420,80),(475,140),(450,140)],0) 

#rightmost rectangle
pygame.draw.polygon(window,void,[(430,70),(440,60),(515,140),(490,140)],0) 

#diamond on top
pygame.draw.polygon(window,void,[(400,90),(360,50),(400,10),(440,50)],0)


#Hunter Sigil Overlay
#top left triangle
pygame.draw.polygon(window,dsolar,[(190,390),(140,390),(90,490),(140,490)],0)

#top right rectangle
pygame.draw.polygon(window,dsolar,[(190,390),(240,390),(290,490),(240,490)],0)

#middle left rectangle
pygame.draw.polygon(window,dsolar,[(190,490),(140,490),(90,590),(140,590)],0)

#middle right rectangle
pygame.draw.polygon(window,dsolar,[(190,490),(240,490),(290,590),(240,590)],0)

#bottom left rectangle
pygame.draw.polygon(window,dsolar,[(190,590),(140,590),(90,690),(140,690)],0)

#bottom right triangle
pygame.draw.polygon(window,dsolar,[(190,590),(240,590),(290,690),(240,690)],0)

#Hunter Sigil (placed lower left) solar
#top left rectangle
pygame.draw.polygon(window,solar,[(200,400),(150,400),(100,500),(150,500)],0)

#top right rectangle
pygame.draw.polygon(window,solar,[(200,400),(250,400),(300,500),(250,500)],0)

#middle left rectangle
pygame.draw.polygon(window,solar,[(200,500),(150,500),(100,600),(150,600)],0)

#middle right rectangle
pygame.draw.polygon(window,solar,[(200,500),(250,500),(300,600),(250,600)],0)

#bottom left rectangle
pygame.draw.polygon(window,solar,[(200,600),(150,600),(100,700),(150,700)],0)

#bottom right rectangle
pygame.draw.polygon(window,solar,[(200,600),(250,600),(300,700),(250,700)],0)

#Titan Sigil overlay
#top middle diamond
pygame.draw.polygon(window,darc,[(660,510),(560,460),(660,410),(760,460)],0)

#bottom middle diamond
pygame.draw.polygon(window,darc,[(660,515),(560,565),(660,615),(760,565)],0)

#left triangle
pygame.draw.polygon (window,darc,[(655,512.5),(560,462.5),(560,562.5)],0)

#right triangle
pygame.draw.polygon (window,darc,[(665,512.5),(760,562.5),(760,462.5)],0)
#Titan Sigil (placed lower right) Arc
#top middle diamond
pygame.draw.polygon(window,arc,[(650,500),(550,450),(650,400),(750,450)],0)

#bottom middle diamond
pygame.draw.polygon(window,arc,[(650,505),(550,555),(650,605),(750,555)],0)

#left triangle
pygame.draw.polygon (window,arc,[(645,502.5),(550,452.5),(550,552.5)],0)

#right triangle
pygame.draw.polygon (window,arc,[(655,502.5),(750,552.5),(750,452.5)],0)

#Traveller in center
pygame.draw.circle (window,white,(425,350),100)

#show drawing (keep this seperate)
pygame.display.flip()


#sleep the program for 3sec
import time
time.sleep(3.0)

#end the program
pygame.quit()

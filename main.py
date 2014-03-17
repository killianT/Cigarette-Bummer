import sys, os, time, pygame
from pygame.locals import *

pygame.init()

#make window
window = pygame.display.set_mode((800, 600))
background = pygame.Surface(window.get_size())
background = background.convert()
background.fill((250, 250, 250))
window.blit(background, (0,0))
pygame.display.flip()
pygame.mouse.set_visible(1)

#set path
path_main = os.path.dirname(__file__)

#load images
bum = pygame.image.load(os.path.join(path_main, "images/bum.png"))
sell = pygame.image.load(os.path.join(path_main, "images/sell.png"))
buy = pygame.image.load(os.path.join(path_main, "images/buy.png"))
sell2 = pygame.image.load(os.path.join(path_main, "images/sell2.png"))
upgrades = pygame.image.load(os.path.join(path_main, "images/upgrades.png"))
des1 = pygame.image.load(os.path.join(path_main, "images/description1.png"))
des2 = pygame.image.load(os.path.join(path_main, "images/description2.png"))

#Variables
cigarettes = 0
money = 0
upgrade1 = 0
upgrade2 = 0
lasttime = time.time() * 1000
lasttime2 = time.time() * 1000 
lastdaytime = time.time() * 1000
day = 0
rent = 800

#text render
font = pygame.font.SysFont("None", 20) #set font 


#start game
startscreen = True
while(startscreen):
    #upgrades logic
    currenttime = time.time() * 1000
    if upgrade1 > 0:
        if currenttime - lasttime >= 60000:
	    cigarettes += 5 * upgrade1 
	    lasttime += 60000
    if upgrade2 > 0:
	if currenttime - lasttime2 >= 30000 and cigarettes > 20:
	    cigarettes -= 20 * upgrade2
	    lasttime2 -= 30000
	    money += 5 * upgrade2
    #time for day and rent
    if currenttime - lastdaytime >= 60000:
	day += 1
	lastdaytime += 60000
	if day == 31: 
	    if money >= rent: 
	        money -= rent
		day -= 30
	    else: 
		print "Game Over!"
		quit()
    #input & logic 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
	    pos = pygame.mouse.get_pos()
	    if bumSurf.collidepoint(pos):
	        cigarettes += 1
            if sellSurf.collidepoint(pos):
		if cigarettes >= 20:
		    cigarettes -= 20
		    money += 5
		elif cigarettes < 20:
		    print "You do not have enough cigarettes to sell!"
            if buysurf1.collidepoint(pos):
		 if money >= 80:
                     upgrade1 += 1
                     money -= 80
		     lasttime = currenttime
            if sellsurf1.collidepoint(pos):
		 if upgrade1 > 0: 
                     upgrade1 -= 1
	    if buysurf2.collidepoint(pos):
	   	 if money >= 80:
		     upgrade2 += 1
		     money -= 80
		     lasttime2 = currenttime
	    if sellsurf2.collidepoint(pos):
		 if upgrade2 > 0: 
		     upgrade2 -= 1


    #Almost everything is rendered here unless it is rendered on a certain condition
    window.blit(background, (0,0))
    #set text
    moneytext = font.render("Money:"+str(money), 0, (0, 0, 0))
    cigarettetext = font.render("Cigarettes:"+str(cigarettes), 0, (0, 0, 0))
    daytext = font.render("Day:"+str(day), 0, (0, 0, 0,)) 
    renttext = font.render("Rent:"+str(rent), 0, (0, 0, 0,))
    #render text
    window.blit(moneytext, (30, 350))
    window.blit(cigarettetext, (30, 150))
    window.blit(daytext, ( 30, 500))
    window.blit(renttext, (30, 520)) 
    #render buy and sell surfaces 
    bumSurf = window.blit(bum, (30, 50))
    sellSurf = window.blit(sell, (30, 250))
    #render upgrade surfaces 
    window.blit(upgrades, (300, 0))
    buysurf1 = window.blit(buy, (600, 50))
    sellsurf1 = window.blit(sell2, (700, 50))
    buysurf2 = window.blit(buy, (600, 100))
    sellsurf2 = window.blit(sell2, (700, 100))
    window.blit(des1, (300, 50))
    window.blit(des2, (300, 100))
    pygame.display.flip()

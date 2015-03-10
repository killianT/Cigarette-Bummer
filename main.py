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
money = 2000
upgrade1 = 0
upgrade2 = 0
upgrade3 = 0
upgrade4 = 0
upgrade5 = 0
lasttime = time.time() * 1000
lasttime2 = time.time() * 1000
lasttime3 = time.time() * 1000
lastdaytime = time.time() * 1000
day = 0
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December", ]
month_days = [31, 28, 31, 30, 31, 30, 31, 31, 31, 30, 31, 30, 31,]
month = 0
rent = 800
location = ["Virginia", "Nebraska", "Maine", "New Jersey", "Washington", "Illinois", "New York",]
location_num = 0
price = [5, 6, 7, 8, 9, 10, 11,]

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
            lasttime2 += 30000
            money += price[location_num] * upgrade2
    if upgrade4 > 0:
        if currenttime - lasttime4 >= 30000:
            cigarettes += 10 * upgrade4
            lasttime3 += 30000

    #time for day and rent
    if currenttime - lastdaytime >= 60000:
        day += 1
        lastdaytime += 60000
        if day == month_days[month]:
            day -= month_days[month]
            month += 1
            day += 1
            if money >= rent: 
                money -= rent
            else: 
                print "Game Over!"
                quit()

    #input & logic 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            if bumSurf.collidepoint(pos):
                cigarettes += 1 + upgrade5
            if sellSurf.collidepoint(pos):
                if cigarettes >= 20:
                    cigarettes -= 20
                    money += price[location_num]
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
            if buysurf3.collidepoint(pos):
                if location_num == 0 and money >= 1000:
                    money -= 1000
                    location_num = 1
                    rent += 200
            if buysurf4.collidepoint(pos):
                if location_num == 1 and money >= 160:
                    money -= 160
                    upgrade4 += 1
            if sellsurf4.collidepoint(pos):
                if upgrade4 >0:
                    upgrade4 -= 1
            if buysurf5.collidepoint(pos):
                if money >= 300 and upgrade5 < 1:
                    upgrade5 += 1
                    money -= 300

    #If Location upgrade is bought add upgrades and change location
    if location_num == 0:
        des3 = font.render("Move to Nebraska and sell cigarettes for a", 0, (0, 0, 0,))
        des3_2 = font.render("dollar more per pack!   $1000", 0, (0, 0, 0,))
        des3_3 = font.render("Rent is increased by $200", 0, (0, 0, 0,))
        des4 = font.render("Locked", 0, (0, 0, 0,))
        des4_2 = font.render("", 0, (0, 0, 0,))
        des4_3 = font.render("", 0, (0, 0, 0,))
        des5 = font.render("Locked", 0, (0, 0, 0,))
        des5_2 = font.render("", 0, (0, 0, 0,))
        des5_3 = font.render("", 0, (0, 0, 0,))
        des5_4 = font.render("", 0, (0, 0, 0,))

    if location_num == 1:
        des3_2 = font.render("dollar more per pack!   Purchased!", 0, (0, 0, 0,))
        des4 = font.render("Buy a Cigarette roller to roll you 10", 0, (0, 0, 0,))
        des4_2 = font.render("cigarettes every 30 seconds", 0, (0, 0, 0,))
        des4_3 = font.render("cost: $160", 0, (0, 0, 0,))
        des5 = font.render("Invest in better clothing and some Cologne", 0, (0, 0, 0,))
        des5_2 = font.render("to make people trust you more", 0, (0, 0, 0,))
        if upgrade5 == 0:
            des5_3 = font.render("cost $300", 0, (0, 0, 0,))
        elif upgrade5 == 1:
            des5_3 = font.render("Purchased!", 0, (0, 0, 0,))
        des5_4 = font.render("2 Cigarettes per click", 0, (0, 0, 0,))



    
                    
    #Almost everything is rendered here unless it is rendered on a certain condition
    window.blit(background, (0,0))
    #set text
    moneytext = font.render("Money:"+str(money), 0, (0, 0, 0))
    cigarettetext = font.render("Cigarettes:"+str(cigarettes), 0, (0, 0, 0))
    monthtext = font.render("Month: "+str(months[month]), 0, (0, 0, 0))
    daytext = font.render("Day:%s / %s " % (str(day), str(month_days[month])), 0, (0, 0, 0,))
    renttext = font.render("Rent:"+str(rent), 0, (0, 0, 0,))
    locationtext = font.render("Location:"+str(location[location_num]), 0, (0, 0, 0,))
    #render info text
    window.blit(moneytext, (30, 350))
    window.blit(cigarettetext, (30, 150))
    window.blit(monthtext, (30, 480))
    window.blit(daytext, (30, 500))
    window.blit(renttext, (30, 520))
    window.blit(locationtext, (30, 540))
    #render buy and sell surfaces 
    bumSurf = window.blit(bum, (30, 50))
    sellSurf = window.blit(sell, (30, 250))
    #render upgrade surfaces 
    window.blit(upgrades, (300, 0))
    buysurf1 = window.blit(buy, (600, 50))
    sellsurf1 = window.blit(sell2, (700, 50))
    buysurf2 = window.blit(buy, (600, 100))
    sellsurf2 = window.blit(sell2, (700, 100))
    buysurf3 = window.blit(buy, (600, 150))
    sellsurf3 = window.blit(sell2, (700, 150))
    buysurf4 = window.blit(buy, (600, 200))
    sellsurf4 = window.blit(sell2, (700, 200))
    buysurf5 = window.blit(buy, (600, 250))
    sellsurf5 = window.blit(sell2, (700, 250))
    buysurf6 = window.blit(buy, (600, 300))
    sellsurf6 = window.blit(sell2, (700, 300))
    buysurf7 = window.blit(buy, (600, 350))
    sellsurf7 = window.blit(sell2, (700, 350))
    #descriptions
    window.blit(des1, (300, 50))
    window.blit(des2, (300, 100))
    window.blit(des3, (300, 150))
    window.blit(des3_2, (300, 160))
    window.blit(des3_3, (300, 170))
    window.blit(des4, (300, 200))
    window.blit(des4_2, (300, 210))
    window.blit(des4_3, (300, 220))
    window.blit(des5, (300, 250))
    window.blit(des5_2, (300, 260))
    window.blit(des5_3, (300, 270))
    window.blit(des5_4, (300, 280))
    pygame.display.flip()

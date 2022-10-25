import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((500,500))
green = (0,255,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
black = (0,0,0)
cavebob = pygame.image.load('cavebob (2).png')
pepe = pygame.image.load('pepe2.png')
shrek = pygame.image.load('shrek2.png')
trump = pygame.image.load('donald.png')
ugandanKnuckles = pygame.image.load('doukdawae.png')
screen.fill(black)
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freeans",60)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
def shop():
    global screen
    pygame.display.set_caption("S H O P")
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                x,y=event.pos
                if 5<=x<=93 and 70<=y<=170:
                    import game
                    if game.coins >= 10:
                        game.coins = game.coins - 10
                        print("You have bought: Caveman Spongebob!")
                        print("Coins:",game.coins)
                        game.plane = game.cavebob
                if 200<=x<=300 and 70<=y<170:
                    import game
                    if game.coins >= 10:
                        game.coins = game.coins - 10
                        print("You have bought: Pepe!")
                        print("Coins:",game.coins)
                        game.plane = game.pepe
                if 350<=x<=438 and 70<=y<=170:
                    import game
                    if game.coins >= 10:
                        game.coins = game.coins - 10
                        print("You have bought: Shrek!")
                        print("Coins:",game.coins)
                        game.plane = game.shrek
                if 50<=x<=138 and 220<=y<=320:
                    import game
                    if game.coins >= 50:
                        game.coins = game.coins - 50
                        print("You have bought: Donald Trump!")
                        print("Coins:",game.coins)
                        game.plane = game.trump
                if 300<=x<=388 and 220<=y<=320:
                    import game
                    if game.coins >= 50:
                        game.coins = game.coins - 50
                        print("You have bought: Ugandan Knuckles!")
                        print("Coins:",game.coins)
                        game.plane = game.ugandanKnuckles
                if 150<=x<=325 and 350<=y<=450:
                        x = 0
                        y = 0
                        screen.fill(black)
                        import gamemenu
                        gamemenu.menu()
        show_text("STORE",175,10,red)
        screen.blit(cavebob,(5,70))
        show_text("10",20,150,red)
        screen.blit(pepe,(200,70))
        show_text("10",200,180,red)
        screen.blit(shrek,(350,70))
        show_text("10",375,160,red)
        screen.blit(trump,(50,220))
        show_text("50",85,310,red)
        screen.blit(ugandanKnuckles,(300,220))
        show_text("50",315,310,red)
        pygame.draw.rect(screen,white,(150,350,175,100))
        show_text("BACK",180,380,blue)
shop()

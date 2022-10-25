import pygame
import random
import time
from pygame.locals import*
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((500,500))
green=(0,255,0)
white = (255,255,255)
red=(255,0,0)
blue=(0,0,255)
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freeans",60)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
def menu():
    global screen
    pygame.display.set_caption("M E N U")
    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                x,y=event.pos
                if 25<=x<=200 and 200<=y<=300:
                    import game
                    x = 0
                    y = 0
                    game.stuff()
                    game.x = 50
                    game.y = 50
                    game.xchange = 5
                    game.ychange = 5
                    game.xx = 0
                    game.yy = 400
                    game.points = 0
                    game.right = 0
                    game.left = 0
                    game.bullet_list = []
                    game.num = 3
                    game.start = time.time()
                    while True:
                        game.game()
                if 300<=x<=475 and 200<=y<=300:
                    exit()
                if 150<=x<=325 and 350<=y<=450:
                    x = 0
                    y = 0
                    screen.fill((0,0,0))
                    import shop
                    shop.shop()
        pygame.draw.rect(screen,green,(25,200,175,100))
        pygame.draw.rect(screen,red,(300,200,175,100))
        pygame.draw.rect(screen,white,(150,350,175,100))
        show_text("Play",73,225,blue)
        show_text("Shop",180,380,blue)
        show_text("Quit",345,225,blue)
        show_text("MONSTA OOF",100,10,blue)
        show_text("by Harini",175,100,blue)
menu()

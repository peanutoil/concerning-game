import time
import random
import pygame
pygame.init()
from pygame.locals import *
pygame.display.set_caption("G A M E")
plane=pygame.image.load("gameship.png")
cavebob = pygame.image.load('cavebob (2).png')
pepe = pygame.image.load('pepe2.png')
shrek = pygame.image.load('shrek2.png')
trump = pygame.image.load('donald.png')
ugandanKnuckles = pygame.image.load('doukdawae.png')
screen=pygame.display.set_mode((500,500))
red=((255,0,0))
black = ((0,0,0))
#pygame.mixer.music.load("roblox-death-sound-effect.mp3") 
pygame.draw.rect(screen,red,(0,0,5,10))
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freeans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
x=50
y=50
xchange=5
ychange=5
xx=0
yy=400
points=0
right=0
left=0
bullet_list = []
num=3
target=pygame.image.load("monster.png")
start=time.time()
coins = 0
def stuff():
    print("Press 'd' to move right, 'a' to move left and the space bar to fire")
    print("You get one point for each time your bullet hits the space monster")
    print("Get 50 points to win! You have 40 seconds before it is Game Over")
    timeleft = 0
def game():
    global coins
    global timeleft
    global start
    global target
    global x
    global y
    global xx
    global yy
    global points
    global right
    global left
    global bullet_list
    global num
    global xchange
    global ychange
    pygame.display.update()
    screen.fill((0,0,0))
    for event in pygame.event.get(): 
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==KEYDOWN:
            if event.key==K_d and xx<=500:
                right=1
            if event.key==K_a and xx>=0:
                left=1
            if event.key==K_SPACE or event.key==K_UP:
                bullet_list.append([xx+50, yy])
        elif event.type==KEYUP:
            if event.key==K_d:
                right=0
            if event.key==K_a:
                left=0
            if event.key==K_SPACE or event.key==K_UP:
                bullet=False
    x=x+xchange
    y=y+ychange
    screen.blit(target,(x,y))
    screen.blit(plane,(xx,yy))
    currtime=time.time()
    timeleft=currtime-start
    show_text("Time:"+str(int(timeleft)),20,40,red)
    if timeleft>=40:
        screen.fill((255,255,255))
        show_text("GAME OVER: YOU LOSE",100,200,red)
        pygame.display.update()
        time.sleep(3)
        screen.fill(black)
        import gamemenu
        gamemenu.menu()
    if x>=400:
        xchange=-1*random.randint(1,num)
    if x<=0 and xchange < 0:
        xchange=-1*xchange
    if y<=0 and ychange<0:
        ychange=-1*ychange
    if y+70>=400 and ychange>0:
        ychange=-1*random.randint(1,num)
    if right==1 and xx<=400:
        xx=xx+5
    if left==1 and xx>=0:
        xx=xx-5
    if points>=10:
        num=4
    if points>=20:
        num=5
    if points>=30:
        num=6
    if points>=40:
        num=7       
    for bullet in bullet_list:
        pygame.draw.rect(screen,red,bullet + [5,10])
        bullet[1] -= 10
        if bullet[1]==0:
            bullet_list.remove(bullet)
            #pygame.mixer.music.play(0)
        if bullet[0] in range(x,x+100) and bullet[1] in range(y,y+70):
            bullet_list.remove(bullet)
            points=points+1
    if points==50:
        #pygame.mixer.music.stop()
        screen.fill((255,255,255))
        show_text("GAME OVER: YOU WIN",125,200,red)
        if 30<timeleft<=40:
            coins = coins + 10
        if 20<timeleft<=30:
            coins = coins + 50
        if 10<timeleft<=20:
            coins = coins + 100
        if 0<timeleft<=10:
            coins = coins + 100000000
        print("Coins:",coins)
        pygame.display.update()
        time.sleep(3)
        screen.fill(black)
        import gamemenu
        gamemenu.menu()
    #keep number of coins?
    show_text("Point(s):"+str(points),10,10,red)            
    
    



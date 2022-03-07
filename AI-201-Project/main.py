import pygame
import time
import os
import random
import math
from playsound import playsound
from Player import *
from Missile import *
from explosion2 import *
from Score_Powerups import *
from Menu_page import *
import winsound

# initializing pygame
pygame.init()

# creating the window for our game
window_w=1000
window_h=580
window = pygame.display.set_mode((window_w,window_h))


# setting title and icon for our game
pygame.display.set_caption("Missile Dodger")
icon = pygame.image.load("assets/icon.png")
pygame.display.set_icon(icon)

#class to display the background
class background:
    def __init__(self):
        self.start=pygame.image.load("assets/background1.jpg")
        self.surface=pygame.image.load("assets/background1.jpg")
        self.imag=pygame.image.load("assets/Gameover3.png")
    def draw(self,window):
        window.blit(self.surface,(0,0))
    def draw_game_over(self,window):
        window.blit(self.imag,(0,0))
    def draw_menu(self, window):
        window.blit(self.start,(0,0))


gameRunning = True
FPS=60
clock=pygame.time.Clock()

#creating our player
player=plane(8,window_w,window_h)

#creating our background
Background=background()

#creating our missile
Missi=missile(4,window_w,window_h, "assets/missile.png")
Missi2=missile(5,window_w,window_h, "assets/missile2.png")
#speed_missi=1
#speed_missi2=2

# explosions
end_explos=explosion2()

#Creating Power Ups
power_life = Power_ups(2,window_w,window_h,"assets/shield4.0.png")
power_score = Power_ups(2,window_w,window_h,"assets/mult2.0.png")
life=1

score=Score()
#score_count=0.1
#score_count2=0.1
multiplyer=0
exp=0
x=0
y=0


font = pygame.font.SysFont('monospace',15) 

# Game menu loop
collision=False
start = True
menu = Menu("assets/play.png",460,260,75,75)
sound_image=Menu("assets/sound.png",950,10,55,55)
sound_cancel=Menu("assets/sound_cancel.png",950,10,55,55)
music=True
while start==True:
    clock.tick(FPS)
    for event in pygame.event.get():
        # quiting the game if user clicks quit
        if event.type == pygame.QUIT:
            gameRunning = False
            start = False
    
    pos=pygame.mouse.get_pos()
    if menu.getRect_mouse().collidepoint(pos):
        if pygame.mouse.get_pressed()[0]==1:
            start=False
    if sound_image.getRect_mouse().collidepoint(pos):
        if pygame.mouse.get_pressed()[0]==1:
            music=False
    elif sound_image.getRect_mouse().collidepoint(pos):
        if pygame.mouse.get_pressed()[0]==1:
            music=True

    Background.draw_menu(window)
    menu.draw(window)
    if music==False:
        sound_cancel.draw(window)
    elif music == True:
        sound_image.draw(window)
    pygame.display.update()
    

if music==True:
    pygame.mixer.init()
    pygame.mixer.music.load("assets/audio.mp3")
    pygame.mixer.music.play()


# main game loop
while gameRunning==True:
    clock.tick(FPS)
    ############################# User input #############################################
    for event in pygame.event.get():
        # quiting the game if user clicks quit
        if event.type == pygame.QUIT:
            gameRunning = False
    #Key Input
    key = pygame.key.get_pressed()
    if (key[pygame.K_LEFT] or key[pygame.K_a])and player.get_x()>0:
        player.move_LEFT()
    if (key[pygame.K_RIGHT] or key[pygame.K_d]) and player.get_x()<942:
        player.move_RIGHT()
    if (key[pygame.K_UP] or key[pygame.K_w]) and player.get_y()>0:
        player.moveDOWN()
    if (key[pygame.K_DOWN] or key[pygame.K_s]) and player.get_y()<530:
        player.moveUP()
    if key[pygame.K_x]and collision==True:
        life = 1
        player.reset_to_defaultPosition(window_w,window_h)
        Missi.reset_Position(window_w,window_h)
        Missi2.reset_Position(window_w,window_h)
        power_score.reset_Position_multiplyer(window_w,window_h)
        power_life.reset_Position(window_w,window_h)
        score.reset()
        collision=False
    if key[pygame.K_q]and collision==True:
        gameRunning=False

    ##############################################################################################################
    if (power_score.getRectS().colliderect(player.getRectP())):
        power_score.reset_Position_multiplyer(window_w,window_h)
        multiplyer=500
    

    if (power_life.getRectS().colliderect(player.getRectP())):
        power_life.reset_Position(window_w,window_h)
        life=life+1
        
    ############################## updating our game before displaying it on window ##############################
    if collision==False:
        player.update()
        #score_count=score.val()
       
        #score_count2=score_count2+0.02        
        #score_count2 = 100 % score_count
        #if score_count2 == 110:
        #    score_count2=0
        #    speed_missi=speed_missi+10
        #    speed_missi2=speed_missi2 + 10
        Missi.update(window_w, window_h, 4, player.get_x(), player.get_y())
        Missi2.update(window_w, window_h, 5, player.get_x(), player.get_y())
        power_life.update(window_w, window_h)
        power_score.update(window_w, window_h)
        if(multiplyer<=0):
            score.add(1)
        else:
            score.add(5)
            multiplyer-=1

    if(Missi.getRectM().colliderect(player.getRectP())):
        print(life) 
        life=life-1
        Missi.reset_Position(window_w,window_h)
        end_explos.draw(window,player.get_x(),player.get_y(),100)
        if(life<=0):
            collision=True
    if(Missi2.getRectM().colliderect(player.getRectP())):
        print(life)
        life=life-1
        Missi2.reset_Position(window_w,window_h)
        end_explos.draw(window,player.get_x(),player.get_y(),100)
        if(life<=0):
            collision=True



    if(Missi.getRectM().colliderect(Missi2.getRectM()) or Missi2.getRectM().colliderect(Missi.getRectM())):
        end_explos.draw(window,Missi.get_x(),Missi.get_y(),200)
        end_explos.draw(window,Missi2.get_x(),Missi2.get_y(),200)

        Missi.reset_Position(window_w,window_h)
        Missi2.reset_Position(window_w,window_h)
    ############################## Displaying our updated settings on window ##############################
    if (collision == True):
        Background.draw_game_over(window)
        txt = font.render('Your Score is : ' + str(math.floor(score.val())), True, (225,225,225))
        window.blit (txt, (10,10))
    else:
        Background.draw(window)
        player.draw(window)
        Missi.draw(window)
        Missi2.draw(window)
        power_life.draw(window)
        power_score.draw(window)
        score.draw(window)
        
        txt = font.render('Lifes: ' + str(life), True, (0,0,0))
        window.blit (txt, (10,30))

    ############################## Collison Detection ##############################
    pygame.display.update()
    #-------------------------------------------------------------------------------

# quiting pygame
#playsound('assets/audio.mp3')
pygame.quit()
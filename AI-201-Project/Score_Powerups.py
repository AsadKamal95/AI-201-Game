import pygame
import random
import math

class Power_ups:
    def __init__(self, speed, window_w, window_h, image):
        self.__surface=pygame.transform.scale(pygame.image.load(image),size=(20,25))
        self.__Rect=self.__surface.get_rect()
        self.__Rect.x=random.randint(0,window_w-20)
        self.__Rect.y=-20
        self.__speed=speed
    def getRectS(self):
        return self.__Rect

    def update(self,w,h):
        #i=random.randint(0,window_w)

        if self.__Rect.y>(h+random.randint(200,800)):
            self.__Rect.x=random.randint(0,w-20)
            self.__Rect.y=-20
        else:
            self.__Rect.y+=self.__speed
    def reset_Position(self,window_w,window_h):
        self.__Rect.x=random.randint(0,window_w-20)
        self.__Rect.y=-1300

    def reset_Position_multiplyer(self,window_w,window_h):
        self.__Rect.x=random.randint(0,window_w-20)
        self.__Rect.y=-2000
    


    def draw(self,Window):
        Window.blit(self.__surface,self.__Rect)


white=(0,0,0)

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont('monospace',15)
    
    def draw(self, Window):
        txt = self.font.render('SCORE: ' + str(math.floor(self.score)), True, white)
        Window.blit (txt, (10,10))
    def add(self, m):
        x=0.02*m
        self.score+=x
        math.floor(self.score)
    def val(self):
        return self.score
    def reset(self):
        self.score=0

import pygame
import random
from minmax import *


class missile:
    def __init__(self,speed,window_w,window_h,image):
        #playsound('assets/audio.mp3')
        #Creating a missile and passing it in a rectangle
        self.__surface=pygame.transform.scale(pygame.image.load(image),size=(15,40))
        self.__Rect=self.__surface.get_rect()
        self.__Rect.x=random.randint(0,window_w)
        self.__Rect.y=window_h
        self.__speed=speed
    def getRectM(self):
        return self.__Rect
    def get_x(self):
        return self.__Rect.x

    def get_y(self):
        return self.__Rect.y

    def update(self,w,h,missi_spped,p_x,p_y):
        bestposition_x=maximize_state_score(p_x)
        if p_y<self.__Rect.y:
            if bestposition_x < self.__Rect.x :
                self.__Rect.x = self.__Rect.x-missi_spped
            elif bestposition_x>self.__Rect.x:
                self.__Rect.x = self.__Rect.x+missi_spped
            else:
                pass
        if self.__Rect.y<-50:
            self.__Rect.x=random.randint(0,w)
            self.__Rect.y=h
        else:
            self.__Rect.y-=self.__speed
    def reset_Position(self,window_w,window_h):
        self.__Rect.x=random.randint(0,window_w)
        self.__Rect.y=window_h
    def draw(self,Window):
        Window.blit(self.__surface,self.__Rect)
import pygame
import random


class Menu:
    def __init__(self,image,x,y,a,b):
        self.__surface=pygame.transform.scale(pygame.image.load(image),size=(a,b))
        self.__Rect=self.__surface.get_rect()
        self.__Rect.x=x
        self.__Rect.y=y
    
    def getRect_mouse(self):
        return self.__Rect

    def draw(self,window):
        
        window.blit(self.__surface,self.__Rect)

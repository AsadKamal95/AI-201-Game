import pygame


class explosion2:
    def __init__(self):
        self.surfaces=[]
        self.surfaces.append(pygame.image.load("assets/explosion/tile000.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile001.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile002.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile003.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile004.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile005.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile006.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile007.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile008.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile009.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile010.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile011.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile012.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile013.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile014.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile015.png"))
        self.surfaces.append(pygame.image.load("assets/explosion/tile016.png"))
        self.index=0
    def update(self):
        self.index+=1
        if self.index>=len(self.surfaces):
            self.index=0
    def draw(self,window,x,y,fps):
        clk=pygame.time.Clock()
        for i in range(0,16):
            clk.tick(fps)
            temprect=self.surfaces[self.index].get_rect()
            temprect.x=x
            temprect.y=y
            window.blit(self.surfaces[self.index],temprect)
            pygame.display.update()
            self.update()
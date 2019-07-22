import pygame as pg
import board

pg.init()



class Pawn(pg.sprite.Sprite):
    def __init__(self, boss,black=False, *groups):
        self.groups = groups
        self._layer = 1
        pg.sprite.Sprite.__init__(self, self.groups)

        self.image = pg.image.load("pawns.png")
        
        if(black):
            self.image = self.image.subsurface((0, 0, 450, 580))
            self.image = pg.transform.scale(self.image, (15, 20))
            self.rect = self.image.get_rect()

        if not black:
            self.image = self.image.subsurface((450, 0, 450, 580))
            self.image = pg.transform.scale(self.image, (15, 20))
            self.rect = self.image.get_rect()

        self.rect.center = boss.rect.center

        self.clickinterval=0.05
        self.clicktime=0



    def update(self, time):
        x,y=pg.mouse.get_pos()
        button=[0]

        if self.clicktime>0:
            self.clicktime-=time
        else:
            button=pg.mouse.get_pressed()




        if Pawn.selected==self and button[0]:
            print("mete")
            
            self.rect.center=board.Board.current_cell_rect.center

            Pawn.selected=0
            self.clicktime=self.clickinterval



                    
        if self.rect.contains(pg.Rect(x,y,1,1)) and button[0]:
            Pawn.selected=self
            self.clicktime=self.clickinterval
             


Pawn.selected=0
import pygame as pg
import math


class Board(pg.sprite.Sprite):
    def __init__(self,pos,*groups):
        self._layer=2
        self.groups=groups
        pg.sprite.Sprite.__init__(self,self.groups)

        self.image=self.cell(2)
        self.imagecopy=self.image.copy()
       
        
        self.pos=pos.copy()
        self.rect=self.image.get_rect()

        self.rect.left=self.pos[0]
        self.rect.top=self.pos[1]



    def update(self, time):
        self.image=self.imagecopy.copy()
     
        mx,my=pg.mouse.get_pos()
        mouserect=pg.Rect(mx,my,1,1)


        collision=False
        if self.rect.contains(mouserect):
            if 30+self.pos[1]>my>10+self.pos[1]:
                collision=True



        if collision:
            self.image.blit(self.cell(0),(0,0))
            self.image.convert_alpha()
            Board.current_cell_rect=self.rect


    @staticmethod
    def cell(width=0):
        cell=pg.Surface((31,41),pg.SRCALPHA,32)
        pg.draw.polygon(cell,(1,1,1,120),((0,10),(0,30),(15,40),(30,30),(30,10),(15,0)),width)

        cell.set_colorkey((0,0,0))
        cell.convert()


        return cell

    @staticmethod
    def board(size,*groups):
        Board.cell_group=[]
    
        for y in range(size[1]):
            for x in range(size[0]):
                if(y%2==0):
                    cell=Board([x*30,y*30],groups)

                if(y%2==1 and x<9):
                    cell=Board([x*30+15,y*30],groups)
                
                Board.cell_group.append([cell,x*30,y*30])



Board.current_cell_rect=pg.Rect(0,0,0,0)
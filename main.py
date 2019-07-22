import pygame as pg
from board import *
from pawn import *



WIDTH, HEIGHT = 305, 315




def main():
    pg.init()

    screen = pg.display.set_mode((WIDTH, HEIGHT), 0, 32)


    allgroups = pg.sprite.LayeredUpdates()
    board_group = pg.sprite.Group()
    pawn_groups = pg.sprite.Group()


    Board.board((10,10),allgroups,board_group)

    cell_list=board_group.sprites()

    for i in range(0, 9):
         Pawn(cell_list[i],False, allgroups, pawn_groups)

    for i in range(9, 19):
         Pawn(cell_list[i],False, allgroups, pawn_groups)


    for i in range(len(cell_list)-9-1, len(cell_list)):
         Pawn(cell_list[i],True, allgroups, pawn_groups)

    for i in range(len(cell_list)-19, len(cell_list)-10):
         Pawn(cell_list[i],True , allgroups, pawn_groups)

    


    clock = pg.time.Clock()
    running = True

    while running:
        screen.fill((100, 100, 100))
        time = clock.tick()/1000.0

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        allgroups.update(time)
        allgroups.draw(screen)

        pg.display.flip()


if __name__ == "__main__":
    main()

import pygame as pg
import sys

def main():

    clock=pg.time.Clock()
    clock.tick(1)
    pg.display.set_caption("初めてのpygame")
    screen=pg.display.set_mode((800,600))

    tori_img=pg.image.load("./fig/6.png")
    tori_img=pg.transform.rotozoom(tori_img,0,2.0)
    tori_rect=tori_img.get_rect()
    tori_rect.center=900,400
    screen.blit(tori_img,tori_rect)
    pg.display.update()

    clock.tick(0.2)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

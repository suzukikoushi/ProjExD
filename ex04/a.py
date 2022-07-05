import random
from turtle import right
import pygame as pg
import sys
import tkinter as tk
import tkinter.messagebox as tkm
import datetime

def main():
    st = datetime.datetime.now()
    vx1, vy1 = 1, 1
    vx2, vy2 = -1, 1
    time = 0
    bomb_list = []
    
    pg.display.set_caption("逃げろ！！こうかとん")
    
    screen_sfc = pg.display.set_mode((1600,900))
    screen_rct = screen_sfc.get_rect()
    clock = pg.time.Clock()
    bgimg_sfc = pg.image.load("fig/pg_bg.jpg")
    bgimg_rct = bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc, bgimg_rct)

    bdimg_sfc = pg.image.load("fig/6.png")
    bdimg_sfc = pg.transform.rotozoom(bdimg_sfc, 0, 2.0)
    bdimg_rct = bdimg_sfc.get_rect()
    bdimg_rct.center = 900,400

    bmimg_sfc = pg.Surface((20, 20))
    pg.draw.circle(bmimg_sfc, (255, 0, 0), (10, 10), 10)
    bmimg_sfc.set_colorkey(0)
    bmimg_rct = bmimg_sfc.get_rect()
    bmimg_rct.centerx = random.randint(0, screen_rct.width)
    bmimg_rct.centery = 9
    bomb_list.append(bmimg_rct)
    
    bmimg2_sfc = pg.Surface((20, 20))
    pg.draw.circle(bmimg2_sfc, (255, 0, 0), (10, 10), 10)
    bmimg2_sfc.set_colorkey(0)
    bmimg2_rct = bmimg_sfc.get_rect()
    bmimg2_rct.centerx = random.randint(0, screen_rct.width)
    bmimg2_rct.centery = 9
    bomb_list.append(bmimg2_rct)

    while True:
        screen_sfc.blit(bgimg_sfc, bgimg_rct)

        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_type = pg.key.get_pressed()
        if key_type[pg.K_UP] == True:
            bdimg_rct.centery -=1
        elif key_type[pg.K_DOWN] == True:
            bdimg_rct.centery +=1
        elif key_type[pg.K_LEFT] == True:
            bdimg_rct.centerx -=1
        elif key_type[pg.K_RIGHT] == True:
            bdimg_rct.centerx +=1

        if bound(bdimg_rct, screen_rct) != (1, 1):
            if key_type[pg.K_UP] == True:
                bdimg_rct.centery +=1
            elif key_type[pg.K_DOWN] == True:
                bdimg_rct.centery -=1
            elif key_type[pg.K_LEFT] == True:
                bdimg_rct.centerx +=1
            elif key_type[pg.K_RIGHT] == True:
                bdimg_rct.centerx -=1

        screen_sfc.blit(bdimg_sfc, bdimg_rct)

        bmimg_rct.move_ip(vx1, vy1)
        bmimg2_rct.move_ip(vx2, vy2)
        screen_sfc.blit(bmimg_sfc, bmimg_rct)
        screen_sfc.blit(bmimg2_sfc, bmimg2_rct)
        yoko1, tate1 = bound(bmimg_rct, screen_rct)
        yoko2, tate2 = bound(bmimg2_rct, screen_rct)
        vx1 *= yoko1
        vy1 *= tate1
        vx2 *= yoko2
        vy2 *= tate2 

        if bdimg_rct.colliderect(bmimg_rct) :
            fi = datetime.datetime.now()
            tkm.showinfo("GameOver", f"残念また遊んでね！\n生存時間{(fi - st).seconds}秒")
            return
        if bdimg_rct.colliderect(bmimg2_rct) :
            fi = datetime.datetime.now()
            tkm.showinfo("GameOver", f"残念また遊んでね！\n生存時間{(fi - st).seconds}秒")
            return

        time += 1

        if time % 1500 == 0:
            if vx1 < 5.0:
                vx1 *= 1.2
                vy1 *= 1.2
                vx2 *= 1.2
                vy2 *= 1.2

        
        pg.display.update()
        clock.tick(1000)

def bound(rct, scr_rct):

    yoko, tate = +1, +1

    if rct.left < scr_rct.left or scr_rct.right < rct.right: yoko = -1
    if rct.top < scr_rct.top or scr_rct.bottom < rct.bottom: tate = -1
    return yoko, tate

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    pg.init()
    main()
    pg.quit()
    sys.exit()
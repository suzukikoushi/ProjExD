import pygame as pg
import sys
import random
import math
import tkinter as tk
import tkinter.messagebox as tkm

class Screen:
    def __init__(self, title, wh, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(wh) # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()              # Rect
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self, image, size, xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = xy


    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]: 
            self.rct.centery -= 1
        if key_states[pg.K_DOWN]: 
            self.rct.centery += 1
        if key_states[pg.K_LEFT]: 
            self.rct.centerx -= 1
        if key_states[pg.K_RIGHT]: 
            self.rct.centerx += 1

        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]: 
                self.rct.centery += 1
            if key_states[pg.K_DOWN] : 
                self.rct.centery -= 1
            if key_states[pg.K_LEFT] : 
                self.rct.centerx += 1
            if key_states[pg.K_RIGHT] : 
                self.rct.centerx -= 1
        self.blit(scr)


class Bomb:
    def __init__(self, color, size, vxy, scr: Screen):
        self.sfc = pg.Surface((2 * size, 2 * size)) # Surface
        self.sfc.set_colorkey((0, 0, 0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        # 練習6
        self.rct.move_ip(self.vx, self.vy)
        # 練習7
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        # 練習5
        self.blit(scr)


class Enemy:
    def __init__(self, size, vxy, scr: Screen):
        self.sfc = pg.image.load("fig/washi.png")
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(20, scr.rct.width - 20)
        self.rct.centery = random.randint(20, scr.rct.height - 20)
        self.vx, self.vy = vxy

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.vx *= yoko
        self.vy *= tate
        self.blit(scr)


class Beam:
    def __init__(self, chr: Bird):
        self.sfc = pg.image.load("fig/beam.png")    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.05)  # Surface
        self.rct = self.sfc.get_rect()          # Rect
        self.rct.center = chr.rct.center
        mx, my = pg.mouse.get_pos()
        sign = math.atan2(chr.rct.centery - my, chr.rct.centerx - mx)
        self.vx = -10 * math.cos(sign)
        self.vy = -10 * math.sin(sign)
        
    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.vx, self.vy)
        self.blit(scr)



def main():
    clock = pg.time.Clock()
    scr = Screen("逃げろこうかとん", (1600, 900), "fig/bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900,400))
    bkb = Bomb((255, 0, 0), 10, (+1, +1), scr)
    em = Enemy(0.5, (+1.7, +1.7), scr)
    bm = None

    while True:
        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            if event.type == pg.MOUSEBUTTONDOWN:
                bm  = Beam(kkt)


        kkt.update(scr)
        bkb.update(scr)
        em.update(scr)

        if bm:
            bm.update(scr)
        if kkt.rct.colliderect(bkb.rct):
            tkm.showinfo("GameOver", f"残念また遊んでね！")
            return
        if kkt.rct.colliderect(em.rct):
            tkm.showinfo("GameOver", f"残念また遊んでね！")
            return
        """if em.rct.colliderect(bm.rct):
            tkm.showinfo("GameClear", f"おめでとう！！")
            return"""

        pg.display.update()
        clock.tick(1000)


# 練習7
def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    pg.init()
    main()
    pg.quit()
    sys.exit()
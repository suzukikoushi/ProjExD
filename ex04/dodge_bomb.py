from os import kill
import pygame as pg
import sys
import random
import tkinter as tk
import tkinter.messagebox as tkm

def main():
    clock=pg.time.Clock()
    
    pg.display.set_caption("逃げろ！こうかとん")
    root = tk.Tk()
    root.withdraw()
    screen_sfc=pg.display.set_mode((1500,900))
    screen_rct=screen_sfc.get_rect()
    bgimg_sfc=pg.image.load("fig/pg_bg.jpg")
    bgimg_rct=bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)
    image=["fig/0.png","fig/1.png","fig/2.png","fig/3.png","fig/4.png","fig/5.png","fig/6.png","fig/7.png","fig/8.png","fig/9.png",]
    kkimag_sfc=pg.image.load(image[random.randint(0,9)])#ランダムでこうかとんのイラストを変更
    kkimag_sfc=pg.transform.rotozoom(kkimag_sfc,0,2.0)
    kkimag_rct = kkimag_sfc.get_rect()
    kkimag_rct.center=900,400
    screen_sfc.blit(kkimag_sfc, kkimag_rct)
    
    bmimg_sfc=pg.image.load("fig/bomb.png")#爆弾のイラストを変更
    bmimg_sfc=pg.transform.rotozoom(bmimg_sfc,0,0.09)
    bmimg_rct=bmimg_sfc.get_rect()
    bmimg_rct.centerx=random.randint(0,screen_rct.width)
    bmimg_rct.centery=random.randint(0,screen_rct.height)
    vx,vy=+1,+1

    
    

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        #練習4
        key_states=pg.key.get_pressed()
        if key_states[pg.K_UP]==True:
            kkimag_rct.centery -= 1
        if key_states[pg.K_DOWN]==True:
            kkimag_rct.centery += 1
        if key_states[pg.K_RIGHT]==True:
            kkimag_rct.centerx += 1
        if key_states[pg.K_LEFT]==True:
            kkimag_rct.centerx -= 1
        if check_bound(kkimag_rct,screen_rct)!=(1,1):
            if key_states[pg.K_UP]    == True:
                kkimag_rct.centery += 1
            if key_states[pg.K_DOWN]  == True:
                kkimag_rct.centery -= 1
            if key_states[pg.K_RIGHT] == True:
                kkimag_rct.centerx -= 1
            if key_states[pg.K_LEFT]  == True:
                kkimag_rct.centerx += 1
        screen_sfc.blit(kkimag_sfc,kkimag_rct)
        
        #練習6
        bmimg_rct.move_ip(vx,vy)
        
        #練習5
        screen_sfc.blit(bmimg_sfc,bmimg_rct)
    
        #練習7
        yoko,tate=check_bound(bmimg_rct,screen_rct)
        vx *= yoko
        vy *= tate

        if kkimag_rct.colliderect(bmimg_rct):
            tkm.showinfo("GAME OVER","おわおわりでぇす")#ゲームオーバー時にメッセージボックスの表示
            sys.exit()

        pg.display.update()
        clock.tick(1000)

def check_bound(rct,scr_rct):
    '''
    [1] rct: こうかとんと爆弾のRect
    [2]scr_rct:スクリーンのRect
    '''
    yoko,tate = +1,+1
    if rct.left<scr_rct.left or scr_rct.right < rct.right:
        yoko=-1.1#横に当たると少し加速

    if rct.top<scr_rct.top or scr_rct.bottom < rct.bottom:
        tate=-1.1#縦に当たると少し加速
    return yoko,tate

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
from ast import NodeVisitor
import pygame as pg
import random 
import sys
import tkinter.messagebox as tkm

deck=[1,2,3,4,5,6,7,8,9,10,11,12,13]*4

class Screen:
    def __init__(self, title,size, image):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode(size)     # Surface
        self.rct = self.sfc.get_rect()         # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect() # Rect
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)

class Deal:
    def deal(): #最初にカードを配る関数
        phand = []
        for i in range(2):
            random.shuffle(deck)
            card = deck.pop()
            if card == 11:
                card = "J"
            if card == 12:
                card = "Q"
            if card == 13:
                card = "K"
            if card == 1:
                card = "A"
            phand.append(card)
            return phand
def main():
    scr=Screen("BJ",(900,700),"fig/haikei.png")

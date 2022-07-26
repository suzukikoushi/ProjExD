import random
import pygame as pg
import tkinter.messagebox as tkm
import tkinter as tk
import sys


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4 #トランプの数字のリスト
#トランプのpng画像のリスト
deck_imag=[["fig/トランプ/CL/1_CL.png","fig/トランプ/CL/2_CL.png","fig/トランプ/CL/3_CL.png",
            "fig/トランプ/CL/4_CL.png","fig/トランプ/CL/5_CL.png","fig/トランプ/CL/6CL.png",
            "fig/トランプ/CL/7_CL.png","fig/トランプ/CL/8_CL.png","fig/トランプ/CL/9_CL.png",
            "fig/トランプ/CL/10_CL.png","fig/トランプ/CL/11_CL.png","fig/トランプ/CL/12_CL.png","fig/トランプ/CL/13_CL.png"],
            ["fig/トランプ/DI/1_DI.png","fig/トランプ/DI/2_DI.png","fig/トランプ/DI/3_DI.png",
            "fig/トランプ/DI/4_DI.png","fig/トランプ/DI/5_DI.png","fig/トランプ/DI/6_DI.png",
            "fig/トランプ/DI/7_DI.png","fig/トランプ/DI/8_DI.png","fig/トランプ/DI/9_DI.png",
            "fig/トランプ/DI/10_DI.png","fig/トランプ/DI/11_DI.png","fig/トランプ/DI/12_DI.png","fig/トランプ/DI/13_DI.png"],
            ["fig/トランプ/HT/1_HT.png","fig/トランプ/HT/2_HT.png","fig/トランプ/HT/3_HT.png",
            "fig/トランプ/HT/4_HT.png","fig/トランプ/HT/5_HT.png","fig/トランプ/HT/6_HT.png",
            "fig/トランプ/HT/7_HT.png","fig/トランプ/HT/8_HT.png","fig/トランプ/HT/9_HT.png",
            "fig/トランプ/HT/10_HT.png","fig/トランプ/HT/11_HT.png","fig/トランプ/SP/12_SP.png","fig/トランプ/HT/13_HT.png"],
            ["fig/トランプ/SP/1_SP.png","fig/トランプ/SP/2_SP.png","fig/トランプ/SP/3_SP.png",
            "fig/トランプ/SP/4_SP.png","fig/トランプ/SP/5_SP.png","fig/トランプ/SP/6_SP.png",
            "fig/トランプ/SP/7_SP.png","fig/トランプ/SP/8_SP.png","fig/トランプ/SP/9_SP.png",
            "fig/トランプ/SP/10_SP.png","fig/トランプ/SP/11_SP.png","fig/トランプ/SP/12_SP.png","fig/トランプ/SP/13_SP.png"]]
        

class Screen:
    def __init__(self,image):
        pg.display.set_caption("BJ")
        self.bgi_sfc=pg.image.load(image)
        self.bgi_rct=self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)




def deal(): #最初にカードを配る関数
    hand = []
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
        hand.append(card)
        return hand


def hit(hand): #ヒットする関数
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
    hand.append(card)
    return hand


def total(hand): #合計得点を返す関数
    score = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            score = score + 10
        elif card == "A":
            if score >= 11:
                score = score + 1
            else:
                score += 11
        else:
            score += card
    return score


def play_again(): #ゲームを続けるかやめるか判定する関数
    mb=tkm.askquestion("ゲーム終了","もう１度プレイしますか？ ",icon='warnimg')
    if mb == "yes" :
        # game()
        return
    else:
        tkm.showinfo("終了","お疲れさまでした!")
        


def result(dealer_hand, player_hand): #結果の関数
    if total(player_hand) > total(dealer_hand):
        print(
            f"\nディーラーの合計は {total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[32mYOU WIN!\033[0m")
    elif total(dealer_hand) > total(player_hand):
        print(
            f"\nディーラーの合計は {total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[91mYOU LOSE...\033[0m")


def game():#ゲームのルール関数
    dealer_hand = deal()
    player_hand = deal()
    print(f"ディーラーのカードは {dealer_hand[0]} です。")
    print(f"プレイヤーのカードは {player_hand} 合計が {total(player_hand)} です。")

    choice = 0

    while choice != quit:
        choice = input("ヒットしますか？ スタンドしますか？ (HIT/STAND): ").lower()
        if choice == "hit":
            hit(player_hand)
            print(
                f"\nあなたに {player_hand[-1]} が配られ、カードは {player_hand} 合計は {total(player_hand)} です。")
            if total(player_hand) > 21:
                print("あなたは 21 を超えてしまいました。\033[91mYOU LOSE...\033[0m")
                choice = quit

        elif choice == "stand":
            print(
                f"\nディーラーの２枚めのカードは {dealer_hand[1]} 合計は {total(dealer_hand)} です。")
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(
                    f"ディーラーに {dealer_hand[-1]} が配られ、カードは {dealer_hand} 合計は {total(dealer_hand)} です。")
                if total(dealer_hand) > 21:
                    print("ディーラーは 21 を超えてしまいました。\033[32mYOU WIN!\033[0m")
                    choice = quit

            if total(dealer_hand) <= 21:
                result(dealer_hand, player_hand)
                choice = quit


game()
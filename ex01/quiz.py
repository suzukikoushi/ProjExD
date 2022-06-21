import random
num=random.randint(0,2)
def main():
    seikai=shutudai(num)
    kaito(seikai)
def shutudai(num):
    q=["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    a=["マスオ","ますお"],["わかめ","ワカメ"],["甥","おい","甥っ子","おいっこ"]
    print(q[num])
    return a[num]
def kaito(seikai):

    ans=input("解答:")
    if ans in seikai:
        print("正解")
    else:
        print("不正解")


        
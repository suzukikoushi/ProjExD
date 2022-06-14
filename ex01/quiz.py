import random
num=random.randint(0,2)
def main():
    seikai=shutudai()
    kaito(seikai)
def shutudai():
    q=["サザエの旦那の名前は？","カツオの妹の名前は？","タラオはカツオから見てどんな関係？"]
    print(q[num])
    return 
def kaito(seikai):
    a={0:["マスオ","ますお"],1:["わかめ","ワカメ"],2:["甥","おい","甥っ子","おいっこ"]}
    ans=input("解答:")
    if ans in seikai:
        print("正解")
    else:
        print("不正解")


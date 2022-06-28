
import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm
import random
import sys
def key_down(event):
    global key #グローバル関数
    key=event.keysym #キーを押したとき

def key_up(event):
    global key
    key=" "#キーを押さなかった時

def main_proc():
    global cx,cy,my,mx
        #移動する処理
    if key=="Right" and maze_bg[my][mx+1]==0:
        mx+=1
    elif key=="Left" and maze_bg[my][mx-1]==0:
        mx-=1
    elif key=="Up" and maze_bg[my-1][mx]==0:
        my-=1
    elif key=="Down" and maze_bg[my+1][mx]==0:
        my+=1
    cx,cy=mx*100+50,my*100+50
    canvas.coords("tori",cx,cy)
    gall()
    root.after(100,main_proc)
def gall():
    global mx,my
    #クリア処理
    if mx==x-2 and my==y-2:
        maze_bg[my+1][mx]=1
        maze_bg[my-1][mx]=1
        maze_bg[my][mx+1]=1
        maze_bg[my][mx-1]=1
        tkm.showinfo("ゴール","ゴールしました。")
        
        sys.exit()
if __name__ =="__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん")

    canvas=tk.Canvas(root,width=1500,height=900,bg="black")#ウィンドウを作る
    canvas.pack()
    x,y=15,9    #迷路の大きさ
    maze_bg=mm.make_maze(x,y)
    mm.show_maze(canvas,maze_bg)
    #こうかとんのillustration
    illust=["fig/0.png","fig/1.png","fig/2.png",
            "fig/3.png","fig/4.png","fig/5.png",
            "fig/6.png","fig/7.png","fig/8.png","fig/9.png"]
    #ランダムでillustrationを表示
    num=random.randint(0,9)
    tori = tk.PhotoImage(file=illust[num])
    #移動する量
    mx,my=1,1
    cx,cy=mx*100,my*100
    #illustrationの表示位置
    canvas.create_image(mx,my,image=tori,tag="tori")

    key=" "
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()

    root.mainloop()

import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key=event.keysym

def key_up(event):
    global key
    key=" "

def main_proc():
    global cx,cy,my,mx
        
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
    root.after(100,main_proc)

if __name__ =="__main__":
    root=tk.Tk()
    root.title("迷えるこうかとん")

    canvas=tk.Canvas(root,width=1500,height=900,bg="black")
    canvas.pack()

    maze_bg=mm.make_maze(15,9)
    mm.show_maze(canvas,maze_bg)

    tori = tk.PhotoImage(file="fig/2.png")
    mx,my=1,1
    cx,cy=mx*100+50,my*100+50
    canvas.create_image(mx,my,image=tori,tag="tori")

    key=" "
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()

    root.mainloop()
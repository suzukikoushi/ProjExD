
import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key=event.keysym

def key_up(event):
    global key
    key=" "

def main_proc():
    global cx,cy
    if key=="Right":
        cx=cx+20
    elif key=="Left":
        cx=cx-20
    elif key=="Up":
        cy=cy-20
    elif key=="Down":
        cy=cy+20
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
    cx,cy=300,400
    canvas.create_image(cx,cy,image=tori,tag="tori")

    key=" "
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)

    main_proc()

    root.mainloop()
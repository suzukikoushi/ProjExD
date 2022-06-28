import tkinter as tk
import tkinter.messagebox as tkm

def count_up():
    global tmr,jid
    tmr = tmr+1
    label["text"]=tmr
    jid=root.after(1000,count_up)

def key_down(event):
    global jid
    if jid !=None:
        root.after_cancel(jid)
        jid = None
        return
    key=event.keysym
    tkm.showinfo("キー押下",f"{key}キーが押されました")
    jid=root.after(1000,count_up)

if __name__ =="__main__":
    root=tk.Tk()
    label = tk.Label(root,text=7,font=("Times New Roman",80))
    label.pack()
    tmr=0 #タイマーの初期値
    jid=None #ジョブ番号の初期値
    root.bind("<KeyPress>",key_down)
    root.mainloop()


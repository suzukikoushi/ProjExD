import tkinter as tk
import  tkinter.messagebox as tkm

if __name__ =="__main__":
    
    def button_click(event):
        btn=event.widget
        txt=btn["text"]
        tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

    root=tk.Tk()
    root.geometry("300x500")
    r=0
    c=0
    for i in range(9,-1,-1):
        button=tk.Button(root,
                      text=f"{i}",
                      width=4,
                      height=1,
                      font=("Times New Roman",30))
        button.bind("<1>",button_click)
        button.grid(row=r,column=c)
        c+=1
        if (i-1)%3==0:
            r+=1
            c=0
    root.mainloop()

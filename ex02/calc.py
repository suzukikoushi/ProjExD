import tkinter as tk
import  tkinter.messagebox as tkm

if __name__ =="__main__":
    
    def button_click(event):
        btn=event.widget
        num=btn["text"]

        #tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

    root=tk.Tk()
    #root.geometryがない場合ちょうどいいサイズに勝手になる
    r=1
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

    entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3)
    entry.insert(tk.END,"num")
    root.mainloop()

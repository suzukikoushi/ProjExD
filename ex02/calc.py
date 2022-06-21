import tkinter as tk
import  tkinter.messagebox as tkm

if __name__ =="__main__":
    
    def button_click(event):
        btn=event.widget
        num=btn["text"]
        if num=="=":
            eqn=entry.get()
            entry.delete(0,tk.END)
            res=eval(eqn)
            entry.insert(tk.END,res)
        elif num=="C":
            entry.delete(0,tk.END)
        elif num=="×":
            num="*"
            entry.insert(tk.END,num)
        elif num=="÷":
            num="/"
            entry.insert(tk.END,num)
        else:
            entry.insert(tk.END,num)
        #tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

    root=tk.Tk()
    #root.geometry(300,500)
    r=1

    for c,i in enumerate(["","","","C",7,8,9,"+",4,5,6,"-",1,2,3,"×",0,"","=","÷"]):
        button=tk.Button(root,
                      text=f"{i}",
                      width=3,
                      height=1,
                      font=("Times New Roman",30))
        button.bind("<1>",button_click)
        x=c%4+1
        y=c//4+1
        button.grid(row=y,column=x)

    entry=tk.Entry(root,justify="right",width=6,font=("Times New Roman",40))
    entry.grid(row=0,column=0,columnspan=3)
    root.mainloop()

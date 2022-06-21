import tkinter as tk
import  tkinter.messagebox as tkm

if __name__ =="__main__":
    
    def button_click(event):
        btn=event.widget
        num=btn["text"]
        if num=="=":#=の対応
            eqn=entry.get()
            entry.delete(0,tk.END)
            res=eval(eqn)
            entry.insert(tk.END,res)
        elif num=="C":#クリアの対応
            entry.delete(0,tk.END)
        elif num=="×":#掛け算の対応
            num="*"
            entry.insert(tk.END,num)
        elif num=="÷":#割り算の対応
            num="/"
            entry.insert(tk.END,num)
        else:#その他の計算の対応
            entry.insert(tk.END,num)
        #tkm.showinfo(txt,f"[{txt}]ボタンが押されました")

    root=tk.Tk()
    #root.geometry(300,500)
    r=1

    for c,i in enumerate(["","","税","C",7,8,9,"+",4,5,6,"-",1,2,3,"×",0,"","=","÷"]):
        #ボタンの設定
        button=tk.Button(root,
                      text=f"{i}",
                      width=3,
                      height=1,
                      font=("Times New Roman",25))
        button.bind("<1>",button_click)
        x=c%4+1
        y=c//4+1
        button.grid(row=y,column=x)
        

    entry=tk.Entry(root,justify="right",width=10,font=("Times New Roman",20))
    entry.grid(row=0,column=0,columnspan=3)
    root.mainloop()

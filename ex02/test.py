print("hello world")

import  tkinter as tk
import  tkinter.messagebox as tkm

def button_click(event):
    btn=event.widget
    txt=btn["text"]
    tkm.showinfo(txt,f"[{txt}]ボタンが押されました")
root=tk.Tk()
#root.title("おためし")#タイトルを付ける
root.geometry("500x200")#ウィンドウのサイズ(幅x高さ)

label=tk.Label(root,
                text="らべるを書いてみた件",
                font=("Ricty Diminished",20)
                )#ラベルを付ける
label.pack()#".pack"を忘れずに付ける

button=tk.Button(root,text=("押すな"),font=("Ricty Diminished",10))
button.bind("<1>",button_click)
#ボタンを付ける
button.pack()#".pack"を忘れないように付ける

entry=tk.Entry(root,width=30)#width:文字が入る大きさ
entry.insert(tk.END,"")
entry.pack()

root.mainloop()

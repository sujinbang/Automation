from tkinter import *
import tkinter

window = Tk()

window.title("AutomationTool")
window.geometry("500x100")

# 텍스트
label=tkinter.Label(window, text="파일 경로를 입력하세요")
label.pack()

# 입력창
entry = tkinter.Entry(window)
entry.pack()

btn1 = Button(window, text = "Rename", command=)
btn1.pack()

window.mainloop()


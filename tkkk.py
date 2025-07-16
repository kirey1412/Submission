from tkinter import *

window=Tk()
window.title("My First TKInter")
window.geometry("500x500")
window.config(background="pink")
Label(window, text="Nickname").place(x=100, y=90)
name=Entry(window, text="").place(x=300, y=90)
submit=Button(window, text="Submit").place(x=200, y=200)
window.mainloop()
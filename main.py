from tkinter import *
import random
from PIL import ImageTk, Image
import os
dies = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
root = Tk()
root.title("Predict your name")
root.iconbitmap("die.ico")
root.geometry("700x550")
c = Canvas(root, bg='white', height=375, width=250)
c.grid(row=0, column=0, padx=150, pady=20)
img = ImageTk.PhotoImage(Image.open("start.png"))
#c.create_text(text="Hi", font=('helvetica', 250, 'bold'))
l1 = Label(c, font=('helvetica', 100, 'bold'),
           bg="gray10", text="start", foreground='red', padx=30)
l1.pack()


def roll():
    a = random.randint(1, 6)
    l1.pack_forget()
    l1.configure(font=('helvetica', 250, 'bold'))
    l1.configure(text=dies[a-1])
    # c.create_text(text=dies[a-1])
    l1.pack()


l2 = Label(root, text="click to start rolling dies",
           font=('helvetica', 150, 'bold'))
b1 = Button(root, text="Roll", command=roll, padx=20, pady=10)
b1.grid(row=1, column=0, padx=50, pady=20)
root.mainloop()

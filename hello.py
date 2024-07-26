import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("你好", "下载并支持我们的Defender.py谢谢")
    show_message()

root = tk.Tk()
root.withdraw()  
show_message()  
root.mainloop()

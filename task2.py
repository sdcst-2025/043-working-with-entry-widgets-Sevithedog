#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk
from tkinter import *
window = tk.Tk()

def run(event):
    print(event)
    s1 = float(s1e.get())
    s2 = float(s2e.get())
    hyp = (s2**2 + s1**2)**(1/2)
    hype.delete(0,tk.END)
    hype.insert(0,hyp)

instruct= tk.Label(window,text = "Enter two short sides of a triangle to find the hypotenuse")
s1e = tk.Entry(window)
s2e = tk.Entry(window)
s1lb = tk.Label(window, text = "Side 1")
s2lb = tk.Label(window, text = "Side 2")
hypbt = tk.Button(window, text = "Hypotenuse:")
hypbt.bind("<Button>", run)
hype = tk.Entry(window)


instruct.pack()
s1lb.pack()
s1e.pack()
s2lb.pack()
s2e.pack()
hypbt.pack()
hype.pack()

window.mainloop()




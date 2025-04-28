"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk
from tkinter import*
def run(event):
    print(event)
    name = entryn.get()
    number = entrynum.get()
    grade = entrygr.get()
    infentry.delete(0,tk.END)
    infentry.insert(0,f"Name: {name}, Grade: {grade}, Id: {number}")




window = tk.Tk()
namelb = tk.Label(window, text = "Enter student name")
entryn = tk.Entry(window)
numberlb = tk.Label(window, text = "Enter student number")
entrynum = tk.Entry(window)
gradelb = tk.Label(window, text = "Enter student grade")
entrygr = tk.Entry(window)
studentlb = tk.Label(window, text = "Student information:")
infentry = tk.Entry(window)
submit = tk.Button(window, text = "Submit")
submit.bind("<Button>", run)




namelb.pack()
entryn.pack()
numberlb.pack()
entrynum.pack()
gradelb.pack()
entrygr.pack()
submit.pack()
studentlb.pack()
infentry.pack()



window.mainloop()
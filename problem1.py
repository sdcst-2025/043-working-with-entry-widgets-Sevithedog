"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

import tkinter as tk 
from tkinter import *

window = tk.Tk()

#program
#def plusminus1():

#def plusminus2():

def run(event):
    print(event)
    



#Entities
inst = tk.Label(window, text = "Enter a trinomial to be factored in the form Ax^2 + Bx + C")
Ae = tk.Entry(window)
pm1 = tk.Button(window, text ="+")
Be = tk.Entry(window)
pm2 = tk.Button(window, text = "+")
Ce = tk.Entry(window)

#position
pm1.columnconfigure(0, weight=0)
pm2.columnconfigure(0,weight = 0)
Ae.columnconfigure(0,weight = 1)
Be.columnconfigure(0,weight = 1)
inst.grid(row = 1, column = 3)
Ae.grid(row=2, column = 1)
pm1.grid(row = 2, column =2,)
Be.grid(row=2, column = 3)
pm2.grid(row =2, column =4, )
Ce.grid(row = 2, column = 5)

window.mainloop()
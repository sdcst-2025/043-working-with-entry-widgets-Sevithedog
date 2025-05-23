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
window.geometry('570x100')
#program
def plusminus1(event):
    print(event)
    print(pm1["text"])
    if pm1['text'] == "+":
        pm1.configure(text = "-")
    elif pm1['text'] == "-":
        pm1.configure(text = "+")
def plusminus2(event):
    print(event)
    print(pm2['text'])
    if pm2['text'] == "+":
        pm2.configure(text= "-")
    elif pm2['text'] == "-":
        pm2.configure(text = "+")

def run(event):
    print(event)
    p1val = pm1['text']
    p2val = pm2['text']
    ans.delete(0,END)
    b = float(Be.get())
    c = float(Ce.get())
    
    if p1val == "-":
        b = b*(-1)
    if p2val == "-":
        c = c*(-1)
    print(p1val)
    print(p2val)
    q1 =  ((b**2)-(4*c))
    q= ((b**2)-(4*c))**0.5
    print(q)
    if q1 < 0:
        ans.insert(0,"No solution")
        return
    else:
        x1 = round((-b + q)/(2),2)
        x2 = round((-b-q)/(2),2)
        if x1 > 0:
            s1 ="-"
            x1 = abs(x1)
        else:
            s1 = "+"
            x1 = abs(x1)
        if x2 > 0:
            s2 ="-"
            x2 = abs(x2)
        else: 
            s2="+"
            x2 = abs(x2)
        ans.insert(0,f"(x {s1} {x1})(x {s2} {x2})")
        return
        

    




#Entities
inst = tk.Label(window, text = "Enter a trinomial to be factored in the form Ax^2 + Bx + C")
Ae = tk.Entry(window)
Ae.insert(0,"x^2")
Ae.config(state = "readonly")
pm1 = tk.Button(window, text ="+")
pm1.bind("<Button>", plusminus1)
Be = tk.Entry(window)
pm2 = tk.Button(window, text = "+")
pm2.bind("<Button>", plusminus2)
Ce = tk.Entry(window)
ans = tk.Entry(window)
submit = tk.Button(window, text = "Factor")
submit.bind("<Button>", run)
#position
"""pm1.columnconfigure(0, weight=0)
pm2.columnconfigure(0,weight = 0)
Ae.columnconfigure(0,weight = 1)
Be.columnconfigure(0,weight = 1)
Ce.columnconfigure(0,weight =1)"""
inst.grid(row = 1, column = 2)
Ae.grid(row=2, column = 1)
pm1.place(x = 160, y=20)
Be.grid(row=2, column = 2)
pm2.place(x = 380, y=20)
Ce.grid(row = 2, column = 3)
ans.grid(row = 4, column =2)
submit.grid(row =3, column = 2)

window.mainloop()
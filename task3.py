#!python3

"""
Create the interface shown.  The program should be able to perform the math operation specified
by the buttons and display the entry in the 3rd entry widget;
"""

import tkinter as tk

w = tk.Tk()
w.attributes("-topmost",True)

def run(event):
    print(event)
    print(event.widget)
    n1 = float(e[0].get())
    n2 = float(e[1].get())
    print(n1,n2)
    if event.widget == b[0]:
        ans = n1*n2
        print(ans)
    elif event.widget == b[1]:
        ans = n1+n2
    elif event.widget == b[2]:
        ans = n1-n2
    elif event.widget == b[3]:
        ans = n1/n2
    e[2].config(state = 'normal' )
    e[2].delete(0,tk.END)
    e[2].insert(0,ans)
    e[2].config(state = 'readonly')
    



l = []
l.append( tk.Label(w,text="Number 1"))
l.append( tk.Label(w,text="Number 2"))
l.append( tk.Label(w,text="Number Calculator"))


e = []
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text=""))
e.append( tk.Entry(w,text="answer",state='readonly'))
b=[]
b.append(tk.Button(w,text="x"))
b.append(tk.Button(w,text="+"))
b.append(tk.Button(w,text="-"))
b.append(tk.Button(w,text="÷"))
b[0].bind("<Button>",run)
b[1].bind("<Button>",run)
b[2].bind("<Button>",run)
b[3].bind("<Button>",run)


l[2].grid(row=1,column=1,columnspan=4)
l[0].grid(row=2,column=1,columnspan=2)
l[1].grid(row=2,column=3,columnspan=2)
e[0].grid(row=3,column=1, columnspan=2)
e[1].grid(row=3,column=3, columnspan=2)
b[0].grid(row=4,column=1)
b[1].grid(row=4,column=2)
b[2].grid(row=4,column=3)
b[3].grid(row=4,column=4)
e[2].grid(row=5,column=1,columnspan=4)

w.mainloop()

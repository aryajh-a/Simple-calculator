import math
from tkinter import *

root=Tk()
root.title("CALCULATOR") 

e= Entry(root, width=60,bg='pink', borderwidth=5)
e.grid(row=0, column=0,columnspan=4)

# CREATING ADD FUNCTION
def add():
    fnum=e.get()
    global first
    first= int(fnum)
    global math
    math='add'
    e.delete(0, END)

# CREATING MULTIPLICATION FUNCTION 
def mul():
    fnum=e.get()
    global first
    first= int(fnum)
    global math
    math='mul'
    e.delete(0, END)

# CREATING SUBTRACTION FUNCTION
def sub():
    fnum=e.get()
    global first
    first= int(fnum)
    global math
    math='sub'
    e.delete(0, END)

# CREATING DIVISION FUNCTION
def div():
    fnum=e.get()
    global first
    first= int(fnum)
    global math
    math='div'
    e.delete(0, END)

# CREATING SQUARE ROOT FUNCTION
def sqrt():
    fnum=e.get()
    global first
    first= int(fnum)
    global math
    math='sqrt'
    e.delete(0, END)

# CREATING PERCENTAGE FUNCTION
def percentage():
    fnum=e.get()
    global first
    first= int(fnum)
    global math
    math='percentage'
    e.delete(0, END)

def click(num):
    current=e.get()
    e.delete(0, END)
    e.insert(0,str(current) + str(num))

# CREATING CLEAR FUNCTION
def clear():
    e.delete(0,END)

# CREATING EQUAL FUNCTION WHICH IS PERFORMING ALL TASKS
def equal():
    if math=='sqrt':
        e.insert(0, first **0.5)
    else:
        snum=e.get()
        e.delete(0, END)
        second= int(snum)
        if math=='add':
            e.insert(0, first + second)
        elif math== 'sub':
            e.insert(0, first - second)
        elif math== 'mul':
            e.insert(0, first * second)
        elif math== 'percentage':
            e.insert(0, (first/100) * second)
        elif math=='div':
            e.insert(0, first / second)
    

# NUMERIC BUTTONS
Button1 = Button(root, text='1',fg='black', bg='pink', padx=40, pady=15, command=lambda : click(1))  
Button2 = Button(root, text='2',fg='black', bg='pink', padx=40, pady=15, command=lambda : click(2))  
Button3 = Button(root, text='3',fg='black', bg='pink', padx=40, pady=15, command=lambda : click(3))  
Button4 = Button(root, text='4',fg='black', bg='pink', padx=40, pady=15, command=lambda : click(4))  
Button5 = Button(root, text='5',fg='black', bg='pink', padx=40, pady=15, command=lambda : click(5))  
Button6 = Button(root, text='6',fg='black', bg='pink', padx=40, pady=15, command=lambda : click(6))  
Button7 = Button(root, text='7',fg='black', bg='pink', padx=40, pady=15, command=lambda : click(7))  
Button8 = Button(root, text='8',fg='black', bg='pink', padx=40, pady=15, command=lambda : click(8))  
Button9 = Button(root, text='9',fg='black', bg='pink', padx=40, pady=15, command=lambda : click(9))  
Button0 = Button(root, text='0',fg='black', bg='pink', padx=87, pady=15, command=lambda : click(0)) 

# POSITIONING THE BUTTONS IN THEIR RIGHT PLACE
Button1.grid(row=4, column=0)
Button2.grid(row=4, column=1)
Button3.grid(row=4, column=2)
Button4.grid(row=3, column=0)
Button5.grid(row=3, column=1)
Button6.grid(row=3, column=2)
Button7.grid(row=2, column=0)
Button8.grid(row=2, column=1)
Button9.grid(row=2, column=2)
Button0.grid(row=5, column=0, columnspan=2)

# FUNCTION BUTTONS
Button_per = Button(root, text='%',     fg='white', bg='purple', padx=38,   pady=15, command=percentage) 
Button_div = Button(root, text='/',     fg='white', bg='purple', padx=40.5, pady=15, command=div) 
Button_clr = Button(root, text='clear', fg='white', bg='purple', padx=31,   pady=15, command=clear) 
Button_sqrt = Button(root, text='sqrt', fg='white', bg='purple', padx=33,   pady=15, command=sqrt) 
Button_eql = Button(root, text='=',     fg='white', bg='purple', padx=86.5, pady=15, command=equal)  
Button_mul = Button(root, text='x',     fg='white', bg='purple', padx=40,   pady=15, command=mul) 
Button_sub = Button(root, text='-',     fg='white', bg='purple', padx=40.5, pady=15, command=sub) 
Button_add = Button(root, text='+',     fg='white', bg='purple', padx=38.5, pady=15, command=add) 

# POSITIONING THE BUTTONS IN THEIR RIGHT PLACE
Button_sqrt.grid(row=1, column=3)
Button_eql.grid(row=5, column=2, columnspan=2)
Button_add.grid(row=2, column=3)
Button_sub.grid(row=3, column=3)
Button_mul.grid(row=4, column=3)
Button_clr.grid(row=1, column=0)
Button_div.grid(row=1, column=2)
Button_per.grid(row=1, column=1)

root.mainloop()

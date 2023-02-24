# Jared Park
# This macro is made just to mess around

# making a calculator with tKinter


import numpy as np
from tkinter import *

root = Tk()
root.title("calculator")

input = Entry(root, width = 30, borderwidth= 5, font = ('Calibri',13))
input.grid(row = 0, column = 0, columnspan= 3, padx = 10, pady = 10)

def press(number):
    current = input.get()
    input.delete(0, END)
    input.insert(0, str(current) + str(number))

def add():
    first_num = input.get()
    global f_num
    f_num = int(first_num)
    input.delete(0, END)

def subtract():
    first_num = input.get()
    global f_num
    f_num = -int(first_num)
    input.delete(0,END)

def equals():
    second_num = input.get()
    answer = f_num + int(second_num)
    input.delete(0, END)
    input.insert(0, str(answer))

def clear():
    input.delete(0, END)

# all buttons

butt1 = Button(root, text = "1", padx = 40, pady = 20, command =lambda: press(1))
butt2 = Button(root, text = "2", padx = 40, pady = 20, command =lambda: press(2))
butt3 = Button(root, text = "3", padx = 40, pady = 20, command =lambda: press(3))
butt4 = Button(root, text = "4", padx = 40, pady = 20, command =lambda: press(4))
butt5 = Button(root, text = "5", padx = 40, pady = 20, command =lambda: press(5))
butt6 = Button(root, text = "6", padx = 40, pady = 20, command =lambda: press(6))
butt7 = Button(root, text = "7", padx = 40, pady = 20, command =lambda: press(7))
butt8 = Button(root, text = "8", padx = 40, pady = 20, command =lambda: press(8))
butt9 = Button(root, text = "9", padx = 40, pady = 20, command =lambda: press(9))
butt0 = Button(root, text = "0", padx = 40, pady = 20, command =lambda: press(0))
buttClear = Button(root, text = "Clear", padx = 30, pady = 20, command = clear)
buttAdd = Button(root, text = "+", padx = 35, pady = 20, command = add)
buttSub = Button(root, text = "-", padx = 35, pady = 20, command = subtract)
buttEqual = Button(root, text = "=", padx = 40, pady = 20, command = equals)

butt1.grid(row = 1, column = 0)
butt2.grid(row = 1, column = 1)
butt3.grid(row = 1, column = 2)
buttAdd.grid(row = 1, column = 3)

butt4.grid(row = 2, column = 0)
butt5.grid(row = 2, column = 1)
butt6.grid(row = 2, column = 2)
buttSub.grid(row = 2, column = 3)

butt7.grid(row = 3, column = 0)
butt8.grid(row = 3, column = 1)
butt9.grid(row = 3, column = 2)

butt0.grid(row = 4, column = 0)
buttClear.grid(row = 4, column = 1)
buttEqual.grid(row = 4, column = 2)


root.mainloop()

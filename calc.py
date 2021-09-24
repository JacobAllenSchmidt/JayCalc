from tkinter import *
import math

root = Tk()
root.title("JayCalc 3.0")

plus = False
minus = False
times = False
divide = False
sqrt = False
expo = False

print("Copyright (c) 2021 Jacob Schmidt")
print("Calculation History:")

def button_click(num):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))

def button_clear():
    e.delete(0, END)

def button_plus():
    global first_num
    first_num = e.get()
    e.delete(0, END)

    global plus
    plus= True
    global minus 
    minus = False
    global times 
    times = False
    global divide 
    divide = False
    global sqrt 
    sqrt = False
    global expo
    expo = False

def button_minus():
    global first_num
    first_num = e.get()
    e.delete(0, END)
    # Set what operator will be used
    global plus
    plus= False
    global minus 
    minus = True
    global times 
    times = False
    global divide 
    divide = False
    global sqrt 
    sqrt = False
    global expo
    expo = False

def button_times():
    global first_num
    first_num = e.get()
    e.delete(0, END)
    # Set what operator will be used
    global plus
    plus= False
    global minus 
    minus = False
    global times 
    times = True
    global divide 
    divide = False
    global sqrt 
    sqrt = False
    global expo
    expo = False

def button_divide():
    global first_num
    first_num = e.get()
    e.delete(0, END)
    # Set what operator will be used
    global plus
    plus= False
    global minus 
    minus = False
    global times 
    times = False
    global divide 
    divide = True
    global sqrt 
    sqrt = False
    global expo
    expo = False

def button_sqrt():
    global first_num
    first_num = e.get()
    e.delete(0, END)
    # Set what operator will be used
    global plus
    plus= False
    global minus 
    minus = False
    global times 
    times = False
    global divide 
    divide = False
    global sqrt 
    sqrt = True
    global expo
    expo = False

def button_expo():
    global first_num
    first_num = e.get()
    e.delete(0, END)
    # Set what operator will be used
    global plus
    plus= False
    global minus 
    minus = False
    global times 
    times = False
    global divide 
    divide = False
    global sqrt 
    sqrt = False
    global expo
    expo = True

def button_equals():
    if plus == True:
        second_num = e.get()
        result = int(first_num) + int(second_num)
        e.delete(0, END)
        e.insert(0, str(result))
        print(result)
    if minus == True:
        second_num = e.get()
        result = int(first_num) - int(second_num)
        e.delete(0, END)
        e.insert(0, str(result))
        print(result)
    if times == True:
        second_num = e.get()
        result = int(first_num) * int(second_num)
        e.delete(0, END)
        e.insert(0, str(result))
        print(result)
    if divide == True:
        second_num = e.get()
        result = int(first_num) / int(second_num)
        e.delete(0, END)
        e.insert(0, str(result))
        print(result)
    if sqrt == True:
        result = math.sqrt(int(first_num))
        e.delete(0, END)
        e.insert(0, str(result))
        print(result)
    if expo == True:
        second_num = e.get()
        result = int(first_num) ** int(second_num)
        e.delete(0, END)
        e.insert(0, str(result))
        print(result)

a = Button(root, text="0", padx=40, pady=40, command=lambda: button_click(0))
b = Button(root, text="1", padx=40, pady=40, command=lambda: button_click(1))
c = Button(root, text="2", padx=40, pady=40, command=lambda: button_click(2))
d = Button(root, text="3", padx=40, pady=40, command=lambda: button_click(3))
e = Button(root, text="4", padx=40, pady=40, command=lambda: button_click(4))
f = Button(root, text="5", padx=40, pady=40, command=lambda: button_click(5))
g = Button(root, text="6", padx=40, pady=40, command=lambda: button_click(6))
h = Button(root, text="7", padx=40, pady=40, command=lambda: button_click(7))
i = Button(root, text="8", padx=40, pady=40, command=lambda: button_click(8))
j = Button(root, text="9", padx=40, pady=40, command=lambda: button_click(9))
enter_button = Button(root, text="=", padx=39, pady=40, command=button_equals)
plus_button = Button(root, text="+", padx=38, pady=40, command=button_plus)
minus_button = Button(root, text="-", padx=39, pady=40, command=button_minus)
times_button = Button(root, text="*", padx=39, pady=40, command=button_times)
divide_button = Button(root, text="/", padx=39, pady=40, command=button_divide)
clear_button = Button(root, text="CLEAR", padx=25, pady=40, command=button_clear)
sqrt_button = Button(root, text="SQRT", padx=30, pady=40, command=button_sqrt)
expo_button = Button(root, text="EXPO", padx=30, pady=40, command=button_expo)

a.grid(row=4, column=0)
b.grid(row=3, column=0)
c.grid(row=3, column=1)
d.grid(row=3, column=2)
e.grid(row=2, column=0)
f.grid(row=2, column=1)
g.grid(row=2, column=2)
h.grid(row=1, column=0)
i.grid(row=1, column=1)
j.grid(row=1, column=2)
enter_button.grid(row=4, column=2)
plus_button.grid(row=4, column=3)
minus_button.grid(row=3, column=3)
times_button.grid(row=2, column=3)
divide_button.grid(row=1, column=3)
clear_button.grid(row=4, column=1)
sqrt_button.grid(row=1, column=4)
expo_button.grid(row=2, column=4)

e = Entry(root, borderwidth=5, fg="#999999")
e.grid(row=0, column=0, columnspan=5)

root.mainloop()
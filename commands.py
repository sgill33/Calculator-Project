import tkinter as tk
from expr_eval import *

# window and frame initialization
window = tk.Tk()
frame1 = tk.Frame(master=window, relief=tk.FLAT, borderwidth=5)
frame2 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=5)
frame3 = tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)


# commands
def one():
    screen['text'] += '1'


def two():
    screen['text'] += '2'


def three():
    screen['text'] += '3'


def four():
    screen['text'] += '4'


def five():
    screen['text'] += '5'


def six():
    screen['text'] += '6'


def seven():
    screen['text'] += '7'


def eight():
    screen['text'] += '8'


def nine():
    screen['text'] += '9'


def zero():
    screen['text'] += '0'


def add():
    screen['text'] += ' + '


def subtract():
    screen['text'] += ' - '


def divide():
    screen['text'] += ' ⁒ '


def multiply():
    screen['text'] += ' x '


def decimal():
    screen['text'] += '.'


def clear():
    screen['text'] = ''

def negative():
    txt = screen['text']
    if len(txt) == 0 or txt[len(txt)-1] == ' ':
        screen['text'] += '-'
    elif txt[len(txt)-1] == '-':
        screen['text'] = txt[:len(txt)-1]

def delete():
    txt = screen['text']

    if len(txt) != 0 and txt[len(txt)-1] == ' ':
        screen['text'] = txt[:len(txt) - 3]
    elif len(txt) != 0:
        screen['text'] = txt[:len(txt)-1]


def calculate():
    eqn = screen['text']

    try:
        screen['text'] = postfix_eval(infix_to_postfix(eqn))

    except Exception:
        screen['text'] = 'ERR'




# title frame
title = tk.Label(
    master=frame1,
    text='Calculator',
    width=40)
title.pack()

# screen frame
screen = tk.Label(
    master=frame2,
    text='',
    width=30,
    height=2
)
screen.pack()

# button frame
num1 = tk.Button(
    master=frame3,
    text='1',
    width=3,
    height=2,
    command=one
)
num2 = tk.Button(
    master=frame3,
    text='2',
    width=3,
    height=2,
    command=two
)
num3 = tk.Button(
    master=frame3,
    text='3',
    width=3,
    height=2,
    command=three
)
num4 = tk.Button(
    master=frame3,
    text='4',
    width=3,
    height=2,
    command=four
)
num5 = tk.Button(
    master=frame3,
    text='5',
    width=3,
    height=2,
    command=five
)
num6 = tk.Button(
    master=frame3,
    text='6',
    width=3,
    height=2,
    command=six
)
num7 = tk.Button(
    master=frame3,
    text='7',
    width=3,
    height=2,
    command=seven
)
num8 = tk.Button(
    master=frame3,
    text='8',
    width=3,
    height=2,
    command=eight
)
num9 = tk.Button(
    master=frame3,
    text='9',
    width=3,
    height=2,
    command=nine
)
num0 = tk.Button(
    master=frame3,
    text='0',
    width=3,
    height=2,
    command=zero
)
plus = tk.Button(
    master=frame3,
    text='+',
    width=3,
    height=2,
    command=add
)
minus = tk.Button(
    master=frame3,
    text='-',
    width=3,
    height=2,
    command=subtract

)
div = tk.Button(
    master=frame3,
    text='⁒',
    width=3,
    height=2,
    command=divide
)
mult = tk.Button(
    master=frame3,
    text='x',
    width=3,
    height=2,
    command=multiply
)
dec = tk.Button(
    master=frame3,
    text='.',
    width=3,
    height=2,
    command=decimal
)
equal = tk.Button(
    master=frame3,
    text='=',
    width=3,
    height=2,
    command=calculate

)
AC = tk.Button(
    master=frame3,
    text='AC',
    width=3,
    height=2,
    fg='red',
    command=clear
)

neg = tk.Button(
    master=frame3,
    text='(+/-)',
    width=3,
    height=2,
    command= negative
)

delt = tk.Button(
    master=frame3,
    text='<-',
    width=3,
    height=2,
    command = delete
)

# button placement
num1.grid(row=0, column=0)
num2.grid(row=0, column=1)
num3.grid(row=0, column=2)
div.grid(row=0, column=3)
num4.grid(row=1, column=0)
num5.grid(row=1, column=1)
num6.grid(row=1, column=2)
mult.grid(row=1, column=3)
num7.grid(row=2, column=0)
num8.grid(row=2, column=1)
num9.grid(row=2, column=2)
minus.grid(row=2, column=3)
num0.grid(row=4, column=0)
dec.grid(row=4, column=1)
neg.grid(row=4, column=2)
plus.grid(row=4, column=3)
AC.grid(row=5, column=0)
delt.grid(row=5,column=1)
equal.grid(row=5,column=2)
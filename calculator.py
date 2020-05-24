from tkinter import *
import parser

# FUNCTION
i = 0


def get_variable(num):
    if display.get() == 'Error':
        clear_all()
    global i
    display.insert(i, num)
    i += 1


def get_operation(operator):
    if display.get() == 'Error':
        clear_all()
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length


def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception as e:
        print(e)
        clear_all()
        display.insert(0, 'Error')


def clear_all():
    display.delete(0, END)


def undo():
    if display.get() == 'Error':
        clear_all()
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)


# UI
root = Tk()
root.title('Calculator')
root.resizable(0, 0)

display = Entry(root, width='22', font=('Courier New', 25))
display.grid(row=0, column=0, columnspan=6)

Button(root, text='1', font=('Courier New', 15, 'bold'), command=lambda: get_variable(1)).grid(row=1, column=0, sticky=NSEW)
Button(root, text='2', font=('Courier New', 15, 'bold'), command=lambda: get_variable(2)).grid(row=1, column=1, sticky=NSEW)
Button(root, text='3', font=('Courier New', 15, 'bold'), command=lambda: get_variable(3)).grid(row=1, column=2, sticky=NSEW)
Button(root, text='+', font=('Courier New', 15, 'bold'), command=lambda: get_operation('+'), bg='#d4d4d2').grid(row=1, column=3, sticky=NSEW)
Button(root, text='AC', font=('Courier New', 15, 'bold'), bg='#d4d4d2', command=clear_all).grid(row=1, column=4, sticky=NSEW)
Button(root, text='\u2B05', font=('Courier New', 15, 'bold'), bg='#d4d4d2', command=undo).grid(row=1, column=5, sticky=NSEW)

Button(root, text='4', font=('Courier New', 15, 'bold'), command=lambda: get_variable(4)).grid(row=2, column=0, sticky=NSEW)
Button(root, text='5', font=('Courier New', 15, 'bold'), command=lambda: get_variable(5)).grid(row=2, column=1, sticky=NSEW)
Button(root, text='6', font=('Courier New', 15, 'bold'), command=lambda: get_variable(6)).grid(row=2, column=2, sticky=NSEW)
Button(root, text='-', font=('Courier New', 15, 'bold'), command=lambda: get_operation('-'), bg='#d4d4d2').grid(row=2, column=3, sticky=NSEW)
Button(root, text='%', font=('Courier New', 15, 'bold'), command=lambda: get_operation('%'), bg='#d4d4d2').grid(row=2, column=4, sticky=NSEW)
Button(root, text='\u03c0', font=('Courier New', 15, 'bold'), command=lambda: get_operation('3.14'), bg='#d4d4d2').grid(row=2, column=5, sticky=NSEW)

Button(root, text='7', font=('Courier New', 15, 'bold'), command=lambda: get_variable(7)).grid(row=3, column=0, sticky=NSEW)
Button(root, text='8', font=('Courier New', 15, 'bold'), command=lambda: get_variable(8)).grid(row=3, column=1, sticky=NSEW)
Button(root, text='9', font=('Courier New', 15, 'bold'), command=lambda: get_variable(9)).grid(row=3, column=2, sticky=NSEW)
Button(root, text='*', font=('Courier New', 15, 'bold'), command=lambda: get_operation('*'), bg='#d4d4d2').grid(row=3, column=3, sticky=NSEW)
Button(root, text='(', font=('Courier New', 15, 'bold'), command=lambda: get_operation('('), bg='#d4d4d2').grid(row=3, column=4, sticky=NSEW)
Button(root, text=')', font=('Courier New', 15, 'bold'), command=lambda: get_operation(')'), bg='#d4d4d2').grid(row=3, column=5, sticky=NSEW)

Button(root, text='.', font=('Courier New', 15, 'bold'), bg='#d4d4d2', command=lambda: get_operation('.')).grid(row=4, column=0, sticky=NSEW)
Button(root, text='0', font=('Courier New', 15, 'bold'), bg='#d4d4d2', command=lambda: get_variable(0)).grid(row=4, column=1, sticky=NSEW)
Button(root, text='=', font=('Courier New', 15, 'bold'), bg='#d4d4d2', command=calculate).grid(row=4, column=2, sticky=NSEW)
Button(root, text='/', font=('Courier New', 15, 'bold'), bg='#d4d4d2', command=lambda: get_operation('/')).grid(row=4, column=3, sticky=NSEW)
Button(root, text='exp', font=('Courier New', 15, 'bold'), bg='#d4d4d2', command=lambda: get_operation('**')).grid(row=4, column=4, sticky=NSEW)
Button(root, text='^2', font=('Courier New', 15, 'bold'), bg='#d4d4d2', command=lambda: get_operation('**2')).grid(row=4, column=5, sticky=NSEW)

root.mainloop()

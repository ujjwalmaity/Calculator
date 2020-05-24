from tkinter import *

root = Tk()
root.title('Calculator')
root.resizable(0, 0)

display = Entry(root, width='22', font=('Courier New', 25))
display.grid(row=0, column=0, columnspan=6)

Button(root, text='1', font=('Courier New', 15, 'bold')).grid(row=1, column=0, sticky=NSEW)
Button(root, text='2', font=('Courier New', 15, 'bold')).grid(row=1, column=1, sticky=NSEW)
Button(root, text='3', font=('Courier New', 15, 'bold')).grid(row=1, column=2, sticky=NSEW)
Button(root, text='+', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=1, column=3, sticky=NSEW)
Button(root, text='\u03c0', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=1, column=4, sticky=NSEW)
Button(root, text='\u2B05', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=1, column=5, sticky=NSEW)

Button(root, text='4', font=('Courier New', 15, 'bold')).grid(row=2, column=0, sticky=NSEW)
Button(root, text='5', font=('Courier New', 15, 'bold')).grid(row=2, column=1, sticky=NSEW)
Button(root, text='6', font=('Courier New', 15, 'bold')).grid(row=2, column=2, sticky=NSEW)
Button(root, text='-', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=2, column=3, sticky=NSEW)
Button(root, text='%', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=2, column=4, sticky=NSEW)
Button(root, text='n!', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=2, column=5, sticky=NSEW)

Button(root, text='7', font=('Courier New', 15, 'bold')).grid(row=3, column=0, sticky=NSEW)
Button(root, text='8', font=('Courier New', 15, 'bold')).grid(row=3, column=1, sticky=NSEW)
Button(root, text='9', font=('Courier New', 15, 'bold')).grid(row=3, column=2, sticky=NSEW)
Button(root, text='*', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=3, column=3, sticky=NSEW)
Button(root, text='(', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=3, column=4, sticky=NSEW)
Button(root, text=')', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=3, column=5, sticky=NSEW)

Button(root, text='AC', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=4, column=0, sticky=NSEW)
Button(root, text='0', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=4, column=1, sticky=NSEW)
Button(root, text='=', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=4, column=2, sticky=NSEW)
Button(root, text='/', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=4, column=3, sticky=NSEW)
Button(root, text='exp', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=4, column=4, sticky=NSEW)
Button(root, text='^2', font=('Courier New', 15, 'bold'), bg='#d4d4d2').grid(row=4, column=5, sticky=NSEW)

root.mainloop()

from tkinter import *

def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(num))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("Calculator")

entry = Entry(root, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('1',1,0), ('2',1,1), ('3',1,2), ('+',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('-',2,3),
    ('7',3,0), ('8',3,1), ('9',3,2), ('*',3,3),
    ('C',4,0), ('0',4,1), ('=',4,2), ('/',4,3)
]

for (text, row, col) in buttons:
    if text == "=":
        Button(root, text=text, width=5, height=2, command=calculate).grid(row=row, column=col)
    elif text == "C":
        Button(root, text=text, width=5, height=2, command=clear).grid(row=row, column=col)
    else:
        Button(root, text=text, width=5, height=2, command=lambda t=text: click(t)).grid(row=row, column=col)

root.mainloop()

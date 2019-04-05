# importing everything from the tkinter library
from tkinter import *

# init the tkinter library with var window
canvas = Tk()


# func to execute upon button press
def kmToMiles():
    t1.delete('1.0', END)  # clears the text widget from any previous calculations
    print(e1_textInput.get())   # prints to console
    if e1_textInput.get() is not "":    # if the input var is not empty, run the next block
        result = float(e1_textInput.get()) * 0.621371
        t1.insert(END, result)  # appends the result at the end


# b1 is a button, which takes the canvas to display on, text and the grids
# to bound itself to
b1 = Button(canvas, text="Button text", command=kmToMiles)  # don't pass func brakets :/
b1.grid(row=0, column=0)

e1_textInput = StringVar()  # holds value for the entry widget
e1 = Entry(canvas, textvariable=e1_textInput)
e1.grid(row=0, column=1)

t1 = Text(canvas, height=1, width=20)
t1.grid(row=0, column=2)

# mainloop prevents the window just closing instantly
canvas.mainloop()

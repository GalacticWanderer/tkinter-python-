#   importing everything from tkinter
from tkinter import *

# init Tk as var window
window = Tk()


#   func to Convert and insert the text into the text widgets
#   make sure to check if the field is empty
def kgToGPO():
    #   result holds a float value
    result = float(e1_textInput.get()) * 1000
    #   clearing the texts
    t2.delete('1.0', END)
    #   inserting the result at the end
    t2.insert(END, result)

    result = float(e1_textInput.get()) * 2.20461
    t3.delete('1.0', END)
    t3.insert(END, result)

    result = float(e1_textInput.get()) * 35.274
    t4.delete('1.0', END)
    t4.insert(END, result)


#   label widget
text = StringVar()
text.set("Simple converter")
l1 = Label(window, textvariable=text)
l1.grid(row=0, column=0)

#   entry widget
e1_textInput = StringVar()
e1 = Entry(window, textvariable=e1_textInput)
e1.grid(row=0, column=1)

#   button widget
b1 = Button(window, text="Convert", command=kgToGPO)
b1.grid(row=0, column=2)

#   an array of texts
t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=0)

t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=1)

t4 = Text(window, height=1, width=20)
t4.grid(row=1, column=2)

#   window mainloops so that it doesnt close immediately
window.mainloop()

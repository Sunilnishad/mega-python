from tkinter import *

fileStore = "t1.txt"
def showData():
    with open(fileStore,'w+') as file:
        value = text.get()
        file.write(value)

window = Tk()
window.wm_title("Testing")
window.geometry("200x100")

l1 = Label(window,text="Entry")
l1.grid(row=1,column=1)

text = StringVar()
t1 = Entry(window,textvariable=text)
t1.grid(row=2,column=1)

s1=Button(window,text="show",command=showData)
s1.grid(row=2,column=2)

b1 = Button(window,text="close",command=window.destroy)
b1.grid(row=3,column=1)

window.mainloop()
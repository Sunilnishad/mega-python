from tkinter import *

window = Tk()

def km_to_gram():
    gram = float(el_val.get())*1000
    t1.insert(END,gram)

def km_to_pound():
    pound = float(el_val.get())*2.204
    t1.insert(END,pound)

def km_to_ounce():
    ounce = float(el_val.get())*35.27
    t1.insert(END,ounce)

b1 = Button(window,text="gram",command=km_to_gram)
b1.grid(row=0,column=0)

b2 = Button(window,text="pound",command=km_to_pound)
b2.grid(row=1,column=0)

b1 = Button(window,text="ounce",command=km_to_ounce)
b1.grid(row=2,column=0)

el_val = StringVar()
e1 = Entry(window,textvariable=el_val)
e1.grid(row=0,column=1)

t1 = Text(window,height=3,width=20)
t1.grid(row=0 ,column=2)

window.mainloop()

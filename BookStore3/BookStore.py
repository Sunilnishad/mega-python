from tkinter import *
#import Bookdatabase
from Bookbackend import Database

database = Database("bookStore.db")

w = Tk()

w.wm_title("BookStore")
def get_select_row(event):
    global selected_tuple
    index =lst1.curselection()[0]
    selected_tuple=lst1.get(index)

#View Function

def view_cmd():
    lst1.delete(0,END)
    for i in database.view():
        lst1.insert(END,i)

#Search Function
def search_cmd():
    lst1.delete(0,END)
    for i in database.search(title_t.get(),year_t.get(),author_t.get(),isbn_t.get()):
        lst1.insert(END,i)

# Add Values
def add_entry():
    database.insert(title_t.get(),year_t.get(),author_t.get(),isbn_t.get())
    lst1.delete(END,0)
    lst1.insert(0,(title_t.get(),year_t.get(),author_t.get(),isbn_t.get()))

# Delete value
def delete_cmd():
    database.delete(selected_tuple[0])
# Update value
def update_cmd():
    database.update(selected_tuple[0],title_t.get(),year_t.get(),author_t.get(),isbn_t.get())

l1 = Label(w,text="Title")
l1.grid(row=0,column=0)

title_t = StringVar()
t1= Entry(w,textvariable=title_t)
t1.grid(row=0,column=1)

l2 = Label(w,text="Year")
l2.grid(row=1,column=0)

year_t = StringVar()
t2= Entry(w,textvariable=year_t)
t2.grid(row=1,column=1)

l3 = Label(w,text="Author")
l3.grid(row=0,column=2)

author_t = StringVar()
t3= Entry(w,textvariable=author_t)
t3.grid(row=0,column=3)

l4 = Label(w,text="ISBN")
l4.grid(row=1,column=2)

isbn_t = StringVar()
t4= Entry(w,textvariable=isbn_t)
t4.grid(row=1,column=3)

lst1 = Listbox(w,height=6,width=30)
lst1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1 = Scrollbar(w)
sb1.grid(row=2,column=2,rowspan=6)

lst1.configure(yscrollcommand = sb1.set)
sb1.configure(command = lst1.yview)

lst1.bind('<<ListboxSelect>>',get_select_row)

b1 = Button(w,text="View all",width=12,command=view_cmd)
b1.grid(row=2,column=3)

b2 = Button(w,text="Search Entry",width=12,command=search_cmd)
b2.grid(row=3,column=3)

b3 = Button(w,text="Add",width=12,command=add_entry)
b3.grid(row=4,column=3)

b4 = Button(w,text="Update selected",width=12,command=update_cmd)
b4.grid(row=5,column=3)

b5 = Button(w,text="Delete selected",width=12,command=delete_cmd)
b5.grid(row=6,column=3)

b6 = Button(w,text="Close",width=12,command=w.destroy)
b6.grid(row=7,column=3)
# w.geometry("440x220")
w.mainloop()
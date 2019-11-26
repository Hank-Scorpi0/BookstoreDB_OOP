from tkinter import *
from Backend import Database

database = Database()

def get_selected_row(event):
    try:
        global selectedtuple
        index=list1.curselection()[0]
        selectedtuple=list1.get(index)
        title_e.delete(0,END)
        title_e.insert(END,selectedtuple[1])
        year_e.delete(0,END)
        year_e.insert(END,selectedtuple[2])
        author_e.delete(0,END)
        author_e.insert(END,selectedtuple[3])
        isbn_e.delete(0,END)
        isbn_e.insert(END,selectedtuple[4])
    except IndexError:
        pass

def delete_cmd():
    database.delete(selectedtuple[0])
    view_command()

def update_cmd():
    database.update(selectedtuple[0],title_txt.get(), author_txt.get(), year_txt.get(), isbn_txt.get())
    view_command()

def view_command():
    list1.delete(0,END)
    for row in database.view():
        list1.insert(END,row)

def search_cmd():
    list1.delete(0,END)
    for row in database.search(title_txt.get(), author_txt.get(), year_txt.get(), isbn_txt.get()):
        list1.insert(END, row)

def add_cmd():
    database.insert(title_txt.get(), author_txt.get(), year_txt.get(), isbn_txt.get())
    list1.delete(0,END)
    list1.insert(END,(title_txt.get(), author_txt.get(), year_txt.get(), isbn_txt.get()))

window = Tk()

window.wm_title("Bookstore Database")

title_t = Label(window,text = "Title").grid(row=1,column=0, pady = 10, padx = 10)
title_txt = StringVar()
title_e = Entry(window, textvariable=title_txt, width = 30)
title_e.grid(row=1, column=1, pady = 10)

year_t = Label(window,text = "Year").grid(row=3,column=0, pady = 10)
year_txt = StringVar()
year_e = Entry(window, textvariable=year_txt, width = 30)
year_e.grid(row=3, column=1, pady = 10)

author_t = Label(window,text = "Author").grid(row=1,column=2, pady = 10)
author_txt = StringVar()
author_e = Entry(window, textvariable = author_txt, width = 30)
author_e.grid(row=1, column=3, pady = 10)

isbn_t = Label(window,text = "ISBN").grid(row=3,column=2, pady = 10)
isbn_txt = StringVar()
isbn_e = Entry(window, textvariable = isbn_txt, width = 30)
isbn_e.grid(row=3, column=3, pady = 10)

view_b = Button(window, text = "View All", width=15, command=view_command)
view_b.grid(row=5, column=1, padx = 5, pady = 10)

search_b = Button(window, text = "Search", width=15, command=search_cmd)
search_b.grid(row=5, column=2, padx = 5, pady = 10)

add_b = Button(window, text = "Add Entry", width=15, command=add_cmd)
add_b.grid(row=5, column=3, padx = 5, pady = 10)

update_b = Button(window, text = "Update Selected", width=15, command=update_cmd)
update_b.grid(row=5, column=4, padx = 5, pady = 10)

delete_b = Button(window, text = "Delete Selected", width=15, command=delete_cmd)
delete_b.grid(row=7, column=2, padx = 5, pady = 10)

close_b = Button(window, text = "Close", width=15, command=window.destroy)
close_b.grid(row=7, column=3, padx = 5, pady = 10)

list1 = Listbox(window, height=10, width=60)
list1.grid(row=8, column=1, columnspan = 4)

sb1 = Scrollbar(window)
sb1.grid(row=8, column=4, sticky=W)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_selected_row)

window.mainloop()
from tkinter import *
from back_end import Database

database = Database()

def get_selected_row(event):
    global selected_row
    index =list_box.curselection()[0]
    selected_row = list_box.get(index)
    title_entry.delete(0,END)
    title_entry.insert(END,selected_row[1])
    author_entry.delete(0,END)
    author_entry.insert(END,selected_row[2])
    year_entry.delete(0,END)
    year_entry.insert(END,selected_row[3])
    isbn_entry.delete(0,END)
    isbn_entry.insert(END,selected_row[4])
     
def view_data():
    list_box.delete(0,END)
    for row in database.view():
        list_box.insert(END, row)

def search_entry():
    list_box.delete(0,END)
    for row in database.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list_box.insert(END, row)

def insert_data():
    list_box.delete(0,END)
    database.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_data()

def delete_data():
    database.delete(selected_row[0])
    view_data()

def update_data():
    database.update(selected_row[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_data()

def close_program():
    database.close()
    root.destroy()

root = Tk()
root.title('My books')
root.iconbitmap('book.ico')
root.resizable(0,0)

title_lbl = Label(root, text="Title")
title_lbl.grid(row=0, column=0, padx=10, pady=10)

author_lbl = Label(root, text="Author")
author_lbl.grid(row=0, column=2, padx=10, pady=10)

year_lbl = Label(root, text="Year")
year_lbl.grid(row=1, column=0, padx=10, pady=10)

isbn_lbl = Label(root, text="Isbn")
isbn_lbl.grid(row=1, column=2, padx=10, pady=10)

title_text = StringVar()
title_entry = Entry(root, textvariable=title_text)
title_entry.grid(row=0, column=1, padx=(0,10), pady=10)

author_text = StringVar()
author_entry = Entry(root, textvariable=author_text)
author_entry.grid(row=0, column=3, padx=(0,10), pady=10)

year_text = StringVar()
year_entry = Entry(root,textvariable=year_text)
year_entry.grid(row=1, column=1, padx=(0,10), pady=10)

isbn_text = StringVar()
isbn_entry = Entry(root, textvariable=isbn_text)
isbn_entry.grid(row=1, column=3, padx=(0,10),pady=10)

list_box = Listbox(root, height=6, width=35)
scroll_bar = Scrollbar(root)

list_box.bind('<<ListboxSelect>>', get_selected_row)

list_box.configure(yscrollcommand=scroll_bar.set)
list_box.grid(row=2, column=0, padx=(20,10), pady=10, rowspan=6, columnspan=2)

scroll_bar.configure(command=list_box.yview)
scroll_bar.grid(row=2, column=2, rowspan=6)

view_all_btn = Button(root, text="View all", width= 12, command=view_data)
view_all_btn.grid(row=2, column=3, padx=10, pady=(0,10))

search_entry_btn = Button(root, text="Search entry", width= 12, command=search_entry)
search_entry_btn.grid(row=3, column=3, padx=10, pady=(0,10))

add_entry_btn = Button(root, text="Add entry", width= 12, command=insert_data)
add_entry_btn.grid(row=4, column=3, padx=10, pady=(0,10))

update_btn = Button(root, text="Update", width= 12, command=update_data)
update_btn.grid(row=5, column=3, padx=10, pady=(0,10))

delete_btn = Button(root, text="Delete selected", width= 12, command=delete_data)
delete_btn.grid(row=6, column=3, padx=10, pady=(0,10))
close_btn = Button(root, text="Close", width= 12, command= close_program)
close_btn.grid(row=7, column=3, padx=10, pady=(0,10))

root.mainloop()
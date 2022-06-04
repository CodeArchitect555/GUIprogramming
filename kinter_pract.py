import sqlite3
from tkinter import *

root = Tk()
root.title('db stuff')
root.geometry("415x500")

#databases
#create a database or connect to one
conn = sqlite3.connect('address_book.db')
#hello
# create a cursor
c = conn.cursor()
'''
#create a table
c.execute("""CREATE TABLE addresses (
        first_name text,
        last_name text,
        city text,
        address text,
        state text,
        zipcode integer)
""")


'''
#create submit function for database
def submit():
    # create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #create cursor
    c = conn.cursor()
    # insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                {
                    'f_name':f_name.get(),
                    'l_name': l_name.get(),
                    'address': address.get(),
                    'city': city.get(),
                    'state': state.get(),
                    'zipcode': zipcode.get()
                  })
    #commit changes            
    conn.commit()
    #close connection
    conn.close()
    
    #clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

#create query function
def query():
    #create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #create cursor
    c = conn.cursor()
    # insert into table
    c.execute("SELECT *, oid FROM addresses")  
    records = c.fetchall() 

    #loop through results
    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + "     " + str(record[6]) + "\n"  

    query_label = Label(root, text=print_records)
    query_label.grid(row=14,column=0,columnspan=2)

def edit():
    editor = Tk()
    editor.title('update a record')
    editor.geometry("400x500")
    #create text boxes
    f_name = Entry(editor, width=30)
    f_name.grid(row=0,column=1,padx=20,pady=(10,0))
    l_name = Entry(editor, width=30)
    l_name.grid(row=1,column=1)
    address = Entry(editor, width=30)
    address.grid(row=2,column=1)
    city = Entry(editor, width=30)
    city.grid(row=3,column=1)
    state = Entry(editor, width=30)
    state.grid(row=4,column=1)
    zipcode = Entry(editor, width=30)
    zipcode.grid(row=5,column=1)
    delete_box = Entry(editor, width=30)
    delete_box.grid(row=10,column=1)


    #create text box labels for editor
    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10,0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="Zipcode")
    zipcode_label.grid(row=5, column=0)
    delete_box_label = Label(editor,text="ID Number")
    delete_box_label.grid(row=10,column=0)

def delete():
    #create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #create cursor
    c = conn.cursor()
    # insert into table
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())  
    
    #commit changes
    conn.commit()

    #close connection
    conn.close()

#create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1,column=1)
address = Entry(root, width=30)
address.grid(row=2,column=1)
city = Entry(root, width=30)
city.grid(row=3,column=1)
state = Entry(root, width=30)
state.grid(row=4,column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5,column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=10,column=1)


#create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10,0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root,text="ID Number")
delete_box_label.grid(row=10,column=0)



#create submit button
submit_btn = Button(root, text="Add Record to database", command=submit)
submit_btn.grid(row=6,column=0, columnspan=2,pady=10,padx=10,ipadx=100)
#create a query button
query_btn = Button(root, text="show records", command=query)
query_btn.grid(row=7,column=0, columnspan=2, pady=10, padx=10, ipadx=130)
#create a delete button
delete_btn = Button(root, text="delete records", command=delete)
delete_btn.grid(row=11,column=0, columnspan=2, pady=10, padx=10, ipadx=130)
#edit button
edit_btn = Button(root, text="edit records", command=edit)
edit_btn.grid(row=13,column=0, columnspan=2, pady=10, padx=10, ipadx=130)


#commit changes
conn.commit()

#close connection
conn.close()


root.mainloop()

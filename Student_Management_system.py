import datetime
from tkinter import *         
import tkinter.messagebox as mb
from tkinter import ttk
from tkcalendar import DateEntry 
import sqlite3


# Creating the universal font variables
head_label_font = ("Book Antiqua", 18, 'bold')
label_font = ('Times New Roman', 14)
entry_font = ('Times New Roman', 15)


# Connecting to the Database where all information will be stored
connector = sqlite3.connect('SchoolManagement.db')
cursor = connector.cursor()
connector.execute(
"CREATE TABLE IF NOT EXISTS SCHOOL_MANAGEMENT (STUDENT_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Name TEXT, EMAIL TEXT, PHONE_NO TEXT, Gender TEXT, DOB TEXT, STREAM TEXT)"
)


# Creating the functions by using def-function
def reset_fields():
   global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, Class_strvar
   L = ['name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar', 'Class_strvar']
   for i in L:
       exec(f"{i}.set('')")
   dob.set_date(datetime.datetime.now().date())
def reset_form():
   global tree
   tree.delete(*tree.get_children())
   reset_fields()
def display_records():
   tree.delete(*tree.get_children())
   curr = connector.execute('SELECT * FROM SCHOOL_MANAGEMENT')
   data = curr.fetchall()
   for records in data:
       tree.insert('', END, values=records)
def add_record():
   global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, Class_strvar
   name = name_strvar.get()
   email = email_strvar.get()
   contact = contact_strvar.get()
   gender = gender_strvar.get()
   DOB = dob.get_date()
   stream = Class_strvar.get()
   if not name or not email or not contact or not gender or not DOB or not stream:
       mb.showerror('Error!', "Please fill all the missing fields!!")
   else:
       try:
           connector.execute(
           'INSERT INTO SCHOOL_MANAGEMENT (Name, EMAIL, PHONE_NO, Gender, DOB, STREAM) VALUES (?,?,?,?,?,?)', (name, email, contact, gender, DOB, stream)
           )
           connector.commit()
           mb.showinfo('Record added', f"Record of {name} was successfully added")
           reset_fields()
           display_records()
       except:
           mb.showerror('Wrong type', 'The type of the values entered is not accurate. Pls note that the contact field can only contain numbers')
def remove_record():
   if not tree.selection():
       mb.showerror('Error!', 'Please select an item from the database')
   else:
       current_item = tree.focus()
       values = tree.item(current_item)
       selection = values["values"]
       tree.delete(current_item)
       connector.execute('DELETE FROM SCHOOL_MANAGEMENT WHERE STUDENT_ID=%d' % selection[0])
       connector.commit()
       mb.showinfo('Done', 'The record you want to delete was successfully deleted.')
       display_records()
def view_record():
   global name_strvar, email_strvar, contact_strvar, gender_strvar, dob, Class_strvar
   if not tree.selection():
       mb.showerror('Error!', 'Please select a record to view')
   else:
        current_item = tree.focus()
        values = tree.item(current_item)
        selection = values["values"]

        name_strvar.set(selection[1]); email_strvar.set(selection[2])
        contact_strvar.set(selection[3]); gender_strvar.set(selection[4])
        date = datetime.date(int(selection[5][:4]), int(selection[5][5:7]), int(selection[5][8:]))
        dob.set_date(date);Class_strvar.set(selection[6])


# Initializing the GUI window by using all import functions
main = Tk()
main.title('School Management System Python Program')
main.geometry('1300x650')



# Creating the background and foreground color variables
Left_Frame_bg = 'MediumSpringGreen' # bg color for the left_frame
Center_Frame_bg = 'PaleGreen' # bg color for the center_frame


# Creating the StringVar or IntVar variables
name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
Class_strvar = StringVar()



# Placing the components in the main window
Label(main, text="SCHOOL MANAGEMENT SYSTEM", font=head_label_font, bg='Violet').pack(side=TOP, fill=X)
left_frame = Frame(main, bg=Left_Frame_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.2)
center_frame = Frame(main, bg=Center_Frame_bg)
center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
right_frame = Frame(main, bg="Gray35")
right_frame.place(relx=0.4, y=30, relheight=1, relwidth=0.6)



# Placing components in the left frame
Label(left_frame, text="Name", font=label_font, bg=Left_Frame_bg).place(relx=0.375, rely=0.05)
Label(left_frame, text="Contact Number", font=label_font, bg=Left_Frame_bg).place(relx=0.175, rely=0.18)
Label(left_frame, text="Email-Address", font=label_font, bg=Left_Frame_bg).place(relx=0.2, rely=0.31)
Label(left_frame, text="Gender", font=label_font, bg=Left_Frame_bg).place(relx=0.3, rely=0.44)
Label(left_frame, text="Date of Birth (DOB)", font=label_font, bg=Left_Frame_bg).place(relx=0.1, rely=0.57)
Label(left_frame, text="Class", font=label_font, bg=Left_Frame_bg).place(relx=0.3, rely=0.7)
Entry(left_frame, width=19, textvariable=name_strvar, font=entry_font).place(x=20, rely=0.1)
Entry(left_frame, width=19, textvariable=contact_strvar, font=entry_font).place(x=20, rely=0.23)
Entry(left_frame, width=19, textvariable=email_strvar, font=entry_font).place(x=20, rely=0.36)
Entry(left_frame, width=19, textvariable=Class_strvar, font=entry_font).place(x=20, rely=0.75)
OptionMenu(left_frame, gender_strvar, 'Male', "Female", "Other").place(x=45, rely=0.49, relwidth=0.5)
dob = DateEntry(left_frame, font=("Arial", 12), width=15)
dob.place(x=20, rely=0.62)
Button(left_frame, text='Submit and Add Record', font=label_font, command=add_record, width=18).place(relx=0.025, rely=0.85)



# Placing components in the center frame
Button(center_frame, text='Delete Record', font=label_font, command=remove_record, width=15).place(relx=0.1, rely=0.25)
Button(center_frame, text='View Record', font=label_font, command=view_record, width=15).place(relx=0.1, rely=0.35)
Button(center_frame, text='Reset Fields', font=label_font, command=reset_fields, width=15).place(relx=0.1, rely=0.45)
Button(center_frame, text='Delete database', font=label_font, command=reset_form, width=15).place(relx=0.1, rely=0.55)



# Placing components in the right side of frame
Label(right_frame, text='Students Records', font=head_label_font, bg='Black', fg='Orange').pack(side=TOP, fill=X)
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                   columns=('Student ID', "Name", "Email-Address", "Contact Number", "Gender", "Date of Birth", "Class"))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.heading('Student ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email-Address', text='Email ID', anchor=CENTER)
tree.heading('Contact Number', text='Phone No', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('Class', text='Class', anchor=CENTER)
tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=140, stretch=NO)
tree.column('#3', width=200, stretch=NO)
tree.column('#4', width=80, stretch=NO)
tree.column('#5', width=80, stretch=NO)
tree.column('#6', width=80, stretch=NO)
tree.column('#7', width=150, stretch=NO)
tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_records()


# Finalizing the GUI window
main.update()
main.mainloop()
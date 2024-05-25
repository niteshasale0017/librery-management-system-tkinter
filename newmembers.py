from tkinter import *
from tkinter.ttk import Combobox
import tkinter.font as font
from tkinter import messagebox
import mysql.connector as mysql

con = mysql.connect(host="localhost",user="root",password="",database="library")
cursor = con.cursor()


class Storemember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("Add New Memeber...!")
        self.geometry("800x800")
        self.myFont = font.Font(family='Verdana',size=12,weight="bold",slant="italic")
        self.bg_image = PhotoImage(file='images/4.png')
        self.bg = Label(self,image=self.bg_image)
        self.bg.pack(side=TOP,fill=BOTH,expand=1)

        self.title_label = Label(self.bg,text="Add New Member...1",bg="white",fg="orange",font=('Verdana',22,'bold'),)
        self.title_label.pack(side=TOP)


        self.m_name_label = Label(self.bg,text="Member Name :-",font=self.myFont,bg="white")
        self.m_name_label.place(x=100,y=100)
        
        self.m_name_var = StringVar()
        self.m_name_entry = Entry(self.bg,width="20",font=self.myFont,bd=5,textvariable=self.m_name_var)
        self.m_name_entry.place(x=350,y=105)
        
        self.m_type_label = Label(self.bg,text="Member Type :-",font=self.myFont,bg="white")
        self.m_type_label.place(x=100,y=150)
        self.m_type_var = StringVar()
        self.m_type_entry = Combobox(self.bg,textvariable=self.m_type_var,width="19",state='readonly',font=self.myFont)
        self.m_type_entry['value']=('Student','Lecturer')
        self.m_type_entry.set('Select')
        self.m_type_entry.place(x=350,y=155)

        self.m_add_label = Label(self.bg,text="Address :-",font=self.myFont,bg="white")
        self.m_add_label.place(x=100,y=200)

        self.m_add_var = StringVar()
        self.m_add_entry = Entry(self.bg,width="20",font=self.myFont,bd=5,textvariable=self.m_add_var)
        self.m_add_entry.place(x=350,y=205)

        self.m_email_label = Label(self.bg,text="Email :-",font=self.myFont,bg="white")
        self.m_email_label.place(x=100,y=250)

        self.m_email_var = StringVar()
        self.m_email_entry = Entry(self.bg,width="20",font=self.myFont,bd=5,textvariable=self.m_email_var)
        self.m_email_entry.place(x=350,y=255)

        self.m_phone_label = Label(self.bg,text="Phone :-",font=self.myFont,bg="white")
        self.m_phone_label.place(x=100,y=300)

        self.m_phone_var = StringVar()
        self.m_phone_entry = Entry(self.bg,width="20",font=self.myFont,bd=5,textvariable=self.m_phone_var)
        self.m_phone_entry.place(x=350,y=305)

        self.m_gender_label = Label(self.bg,text="Gender :-",font=self.myFont,bg="white")
        self.m_gender_label.place(x=100,y=350)
        self.m_gender_var = StringVar()
        self.m_gender_entry = Combobox(self.bg,textvariable=self.m_gender_var,width="19",state='readonly',font=self.myFont)
        self.m_gender_entry['value']=('Male','Female')
        self.m_gender_entry.set('Select')
        self.m_gender_entry.place(x=350,y=355)

        self.btn = Button(self.bg,text="Save",font=self.myFont,width="10",border=None,bg="lightgreen",fg="white",command=self.save_member)
        self.btn.place(x=250,y=450)
    
    def save_member(self):
        name = self.m_name_entry.get()
        m_type = self.m_type_entry.get()
        add = self.m_add_entry.get()
        email = self.m_email_entry.get()
        phone = self.m_phone_entry.get()
        gender = self.m_gender_entry.get()

        query = "insert into member(name,type,address,email,phone,gender) values(%s,%s,%s,%s,%s,%s)" 
        val = (name,m_type,add,email,phone,gender)
        cursor.execute(query,val)
        con.commit()
        print('insert')
        self.m_name_var.set(value="")
        self.m_type_var.set("select")
        self.m_add_var.set(value="")
        self.m_email_var.set(value="")
        self.m_phone_var.set(value="")
        self.m_gender_var.set("select") 


from tkinter import *
from tkinter.ttk import Combobox
import tkinter.font as font
from tkinter import messagebox
import mysql.connector as mysql

con = mysql.connect(host="localhost",user="root",password="",database="library")
cursor = con.cursor()


class Storebook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("Add Books Details...!")
        self.geometry("800x800")
        self.myFont = font.Font(family='Verdana',size=12,weight="bold",slant="italic")
        self.bg_image = PhotoImage(file='images/4.png')
        self.bg = Label(self,image=self.bg_image)
        self.bg.pack(side=TOP,fill=BOTH,expand=1)

        self.title_label = Label(self.bg,text="Add New Member...1",bg="white",fg="orange",font=('Verdana',22,'bold'),)
        self.title_label.pack(side=TOP)


        self.title_label = Label(self.bg,text="Book Title :-",font=self.myFont,bg="white")
        self.title_label.place(x=100,y=100)
        
        self.title_var = StringVar()
        self.title_entry = Entry(self.bg,width="20",font=self.myFont,bd=5,textvariable=self.title_var)
        self.title_entry.place(x=350,y=105)

        self.author_label = Label(self.bg,text="Author Name :-",font=self.myFont,bg="white")
        self.author_label.place(x=100,y=150)
        
        self.author_var = StringVar()
        self.author_entry = Entry(self.bg,width="20",font=self.myFont,bd=5,textvariable=self.author_var)
        self.author_entry.place(x=350,y=155)

        self.pages_label = Label(self.bg,text="Book Pages :-",font=self.myFont,bg="white")
        self.pages_label.place(x=100,y=200)
        
        self.pages_var = StringVar()
        self.pages_entry = Entry(self.bg,width="20",font=self.myFont,bd=5,textvariable=self.pages_var)
        self.pages_entry.place(x=350,y=205)

        self.price_label = Label(self.bg,text="Price :-",font=self.myFont,bg="white")
        self.price_label.place(x=100,y=250)
        
        self.price_var = StringVar()
        self.price_entry = Entry(self.bg,width="20",font=self.myFont,bd=5,textvariable=self.price_var)
        self.price_entry.place(x=350,y=255)

        self.publisher_label = Label(self.bg,text="Publisher :-",font=self.myFont,bg="white")
        self.publisher_label.place(x=100,y=300)
        
        self.publisher_var = StringVar()
        self.publisher_entry = Entry(self.bg,width="20",font=self.myFont,bd=5,textvariable=self.publisher_var)
        self.publisher_entry.place(x=350,y=305)

        self.book_type_label = Label(self.bg,text="Categories :-",font=self.myFont,bg="white")
        self.book_type_label.place(x=100,y=350)
        self.book_type_var = StringVar()
        self.book_type_entry = Combobox(self.bg,textvariable=self.book_type_var,width="19",state='readonly',font=self.myFont)
        self.book_type_entry['value']=('Action and adventure',
        'Textbook',
        'Reference',
        'Art/architecture',
        'Alternate history',
        'Autobiography',
        'Biography',
        'Business/economics',
        'Crafts/hobbies',
        'Cookbook',
        'Comic book',
        'Encyclopedia',
        'Drama',
        'Health/fitness',
        'Graphic novel',
        'Historical fiction',
        'Mystery',
        'Philosophy',
        'Science fiction'
        )
        
        self.book_type_entry.set('Select')
        self.book_type_entry.place(x=350,y=355)

        
        self.btn = Button(self.bg,text="Save",font=self.myFont,width="10",border=None,bg="lightgreen",fg="white",command=self.save_book)
        self.btn.place(x=250,y=450)

    def save_book(self):
        title =  self.title_entry.get()
        author = self.author_entry.get()
        pages = self.pages_entry.get()
        price = self.price_entry.get()
        publisher = self.publisher_entry.get()
        book_type = self.book_type_entry.get()

        query = "insert into book(title,author,pages,price,publisher,book_type) values(%s,%s,%s,%s,%s,%s)"
        val = (title,author,pages,price,publisher,book_type)
        cursor.execute(query,val)
        con.commit()
        print('insert')

        self.title_var.set(value="")
        self.author_var.set(value="")
        self.pages_var.set(value="")
        self.price_var.set(value="")
        self.publisher_var.set(value="")
        self.book_type_var.set('select')

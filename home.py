from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from tkinter.ttk import Combobox,Notebook
import importlib
import mysql.connector as mysql
newmemberwindow = importlib.import_module('newmembers')
newbookwindow = importlib.import_module('newbooks')
bookissuewindow = importlib.import_module('book_issue')
bookreturnwindow = importlib.import_module('book_return')


con = mysql.connect(host="localhost",user="root",password="",database="library")
cursor = con.cursor()

win = Tk()
win.title("Librery Management System")
class home:
    def __init__(self,win):
        def management_list(self):
            query = "select * from book order by book_id"
            cursor.execute(query)
            result = cursor.fetchall()
            count = 0
            for i in result:
                self.list1.insert(count,str(i[0])+'-'+str(i[1]))
                count +=1
            self.list1.configure(fg="blue")    

            def info_list(event=None):
                res = str(self.list1.get(self.list1.curselection()))
                value = res.split('-')[0]
                query1 = "select * from book where book_id=%s"
                val1 = (value,)
                cursor.execute(query1,val1)
                result1 = cursor.fetchall()
                
                self.list2.delete(0,END)# delete previews data
                
                for i in result1:
                    
                    self.list2.insert(0,"Title :-"+str(i[1]))
                    self.list2.insert(1,"Author :-"+str(i[2]))
                    self.list2.insert(2,"Pages :-"+str(i[3]))
                    self.list2.insert(3,"Price :-"+str(i[4]))
                    self.list2.insert(4,"Publisher :-"+str(i[5]))
                    self.list2.insert(5,"Categories :-"+str(i[6]))
                    self.list2.insert(6,"Status :-"+str(i[7]))
                    if i[7]==0:
                        self.list2.configure(fg="green")
                    else:
                        self.list2.configure(fg="red")    
                    
            self.list1.bind('<<ListboxSelect>>',info_list)   



        self.myFont = font.Font(family='Verdana',size=8,weight="bold")
        self.win = win
        self.win.geometry("1400x800")
        self.topframe = Frame(self.win,height=70,width=1400,relief=SUNKEN,border=2)
        self.topframe.pack(fill=X,side=TOP)
        #creating the button add member, books,issed,resturned
        add_member = Button(self.topframe,text="Add Memeber",width=10,font=self.myFont,command=self.new_member)
        add_member.grid(row=0,column=0)

        add_books = Button(self.topframe,text="Add Books",width=10,font=self.myFont,command=self.new_book)
        add_books.grid(row=0,column=1)

        book_issue = Button(self.topframe,text="Book Issued",width=10,font=self.myFont,command=self.bookissue)
        book_issue.grid(row=0,column=2)

        book_return = Button(self.topframe,text="Book Return",width=10,font=self.myFont,command=self.bookreturn)
        book_return.grid(row=0,column=3)

                  

        
        #left side
        self.leftframe = Frame(self.win,height=730,width=800,relief=SUNKEN,border=1)
        self.leftframe.pack(side=LEFT)
        #notebook create
        self.notebook = Notebook(self.leftframe,width=800,height=730)
        self.management_tab = Frame(self.notebook)
        self.summary_tab = Frame(self.notebook)
        self.notebook.add(self.management_tab,text="Management")
        self.notebook.add(self.summary_tab,text="Summary")
        self.notebook.pack(fill=BOTH,expand=True)

        #management tab create
        self.list1 = Listbox(self.management_tab,width=40,height=40)
        self.sc = Scrollbar(self.management_tab)
        self.list1.grid(row=0,column=0,padx=(10,0),pady=10,sticky=N)
        self.sc.configure(command=self.list1.yview)
        self.list1.configure(yscrollcommand=self.sc.set,font=self.myFont)
        self.sc.grid(row=0,column=0,sticky=N+S+E)

        

        self.list2 = Listbox(self.management_tab,width=65,height=40,font=self.myFont)
        self.list2.grid(row=0,column=1,padx=(10,0),pady=10,sticky=N)

        
        #right side
        self.rightframe =Frame(self.win,height=730,width=500,border=2,relief=SUNKEN) 
        self.rightframe.pack()


        #search frame ************************************
        self.serach_frame = LabelFrame(self.rightframe,text="search",width=500,height=100)
        self.serach_frame.pack(fill=BOTH)

        self.search_label = Label(self.serach_frame,text="Search",fg="blue",font=self.myFont)
        self.search_label.place(x=10,y=15)
        
        self.search_val = StringVar()
        self.search_entry = Entry(self.serach_frame,textvariable=self.search_val,width=50,bd=10)
        self.search_entry.place(x=80,y=15)
        self.search_entry.bind('<KeyRelease>',self.search_fun)
        

        #sorting frame***************************************
        self.sort_frame = LabelFrame(self.rightframe,text="Books List...!",width=500,height=120)
        self.sort_frame.pack(fill=BOTH)

        sort_label = Label(self.sort_frame,text="Sort By...!",fg="blue",font=self.myFont)
        sort_label.place(x=10,y=20)    
        self.sort_val = IntVar()

        all_books = Radiobutton(self.sort_frame,text="ALL Books",variable=self.sort_val,value=0,font=self.myFont)
        all_books.place(x=10,y=50)

        in_stock = Radiobutton(self.sort_frame,text="In stock",variable=self.sort_val,value=1,font=self.myFont)
        in_stock.place(x=120,y=50)

        issue_books = Radiobutton(self.sort_frame,text="Issue Books",variable=self.sort_val,value=2,font=self.myFont)
        issue_books.place(x=220,y=50)

        sort_btn = Button(self.sort_frame,text="Sort",fg="white",bg="gray",font=self.myFont,width=10,command=self.radio_sort_fun)
        sort_btn.place(x=380,y=50)


        #categories Sort

        self.cate_sort = LabelFrame(self.rightframe,text="Categories Books List...!",width=500,height=120)
        self.cate_sort.pack(fill=BOTH)
        self.categories_var = StringVar()
        self.categories_box = Combobox(self.cate_sort,textvariable=self.categories_var,width="30",state='readonly',font=self.myFont)
        self.categories_box['value']=('Action and adventure',
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
        self.categories_box.set('select')
        self.categories_box.place(x=40,y=40)

        categories_btn = Button(self.cate_sort,text="Sort",fg="white",bg="gray",font=self.myFont,width=10,command=self.cate_sort_func)
        categories_btn.place(x=380,y=40)


        # image frame *******************************************************
        self.img = PhotoImage(file='images/3.png')
        self.img_frame = Frame(self.rightframe,width=500,height=300)
        self.img_frame.pack(fill=BOTH)
        img_label = Label(self.img_frame,image=self.img)
        img_label.pack()
        management_list(self)
        

    
    def cate_sort_func(self):
        cate = self.categories_box.get()
        query = "select * from book where book_type=%s"
        val = (cate,)
        cursor.execute(query,val)
        result = cursor.fetchall()
        self.list1.delete(0,END)
        for i in result:
            count = 0
            self.list1.insert(count,str(i[0])+"-"+str(i[1]))
            count +=1

    def radio_sort_fun(self):
        val = self.sort_val.get()
        if val == 0:
            query = "select * from book order by book_id"
            cursor.execute(query)
            result = cursor.fetchall()
            count = 0
            for i in result:
                self.list1.insert(count,str(i[0])+'-'+str(i[1]))
                count +=1
        elif val == 1:
            query = "select * from book where book_status=%s"
            val = (0,)
            cursor.execute(query,val)
            result = cursor.fetchall()
            self.list1.delete(0,END) # remove preview data
            for i in result:
                count = 0
                self.list1.insert(count,str(i[0])+"-"+str(i[1]))
                count +=1
        else:
            query = "select * from book where book_status=%s"
            val = (1,)
            cursor.execute(query,val)
            result = cursor.fetchall()
            self.list1.delete(0,END) # remove preview data
            for i in result:
                count = 0
                self.list1.insert(count,str(i[0])+"-"+str(i[1]))
                count +=1
    
    def search_fun(self,event=None):
        self.list1.delete(0,END)
        res = self.search_entry.get()
        query = "select * from book where title like %s"
        val = ('%'+res+'%',)
        cursor.execute(query,val)
        result = cursor.fetchall()
        for i in result:
            count = 0
            self.list1.insert(count,str(i[0])+"-"+str(i[1]))
            count +=1


    def new_book(self):
        add = newbookwindow.Storebook() #add is a object || newbookwindow is a varialbe declare || storebook is a class

    def new_member(self):
        add = newmemberwindow.Storemember()
    
    def bookissue(self):
        add = bookissuewindow.Bookissue()
    
    def bookreturn(self):
        add = bookreturnwindow.Bookreturn()        




obj = home(win)
win.mainloop()


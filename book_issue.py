from tkinter import *
import tkinter.font as font
from tkinter.ttk import Combobox
from tkinter import messagebox
import mysql.connector as mysql

con = mysql.connect(host="localhost",user="root",password="",database="library")
cursor = con.cursor()

class Bookissue(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("Books Issue Details...!")
        self.geometry("800x800")
        self.myFont = font.Font(family='Verdana',size=10,weight="bold",slant="italic")

        def m_list_fun(self): # auto load member list code
            query = "select m_id,name from member where status=%s" 
            v = (0,)
            cursor.execute(query,v)
            res = cursor.fetchall()
            for i in res:
                count = 0
                self.m_list.insert(count,str(i[0])+"-"+str(i[1]))
                count +=1

            def m_select_fun(event=None):
                self.res = str(self.m_list.get(self.m_list.curselection()))
                value = self.res.split("-")[0]
                query = "select * from member where m_id=%s"
                val = (value,)
                cursor.execute(query,val)
                result = cursor.fetchall() 

                self.choose_list.delete(0,END)
                for i in result:
                    self.choose_list.insert(0,"ID :-"+str(i[0]))
                    self.choose_list.insert(1,"Name :-"+str(i[1]))
                    self.choose_list.insert(2,"Type :-"+str(i[2]))
                    self.choose_list.insert(3,"Address :-"+str(i[3]))
                    self.choose_list.insert(4,"Email :-"+str(i[4]))
                    self.choose_list.insert(5,"Phone :-"+str(i[5]))
                    self.choose_list.insert(6,"Gender :-"+str(i[6]))
            
            self.m_list.bind('<<ListboxSelect>>',m_select_fun)        

        
        def b_list_fun(self): # auto oad book list code
            query1 = "select book_id,title from book where book_status=%s"
            v = (0,) 
            cursor.execute(query1,v)
            res1 = cursor.fetchall()
            for i in res1:
                count1 = 0
                self.b_list.insert(count1,str(i[0])+"-"+str(i[1]))
                count1 +=1

            def b_select_fun(event=None):
                self.res1 = str(self.b_list.get(self.b_list.curselection()))
                value = self.res1.split("-")[0]
                query = "select * from book where book_id=%s"
                val = (value,)
                cursor.execute(query,val)
                result = cursor.fetchall() 

                self.choose_list1.delete(0,END)
                for i in result:
                    self.choose_list1.insert(0,"Title :-"+str(i[1]))
                    self.choose_list1.insert(1,"Author :-"+str(i[2]))
                    self.choose_list1.insert(2,"Pages :-"+str(i[3]))
                    self.choose_list1.insert(3,"Price :-"+str(i[4]))
                    self.choose_list1.insert(4,"Publisher :-"+str(i[5]))
                    self.choose_list1.insert(5,"Categories :-"+str(i[6]))
                   
            self.b_list.bind('<<ListboxSelect>>',b_select_fun)    



        self.l_frame = LabelFrame(self,width=400,text="selection",relief=SUNKEN)
        self.l_frame.pack(fill=Y,side=LEFT)
        
        select_label = Label(self.l_frame,text="Select Member",fg="blue",font=self.myFont)
        select_label.grid(row=0,column=0)
        
        self.m_search_entry = Entry(self.l_frame,bd=5,width=40,font=self.myFont)
        self.m_search_entry.grid(row=1,column=0)
        self.m_search_entry.bind('<KeyRelease>',self.m_search_fun)

        self.m_list = Listbox(self.l_frame,width=30,height=5,font=self.myFont)
        self.sc = Scrollbar(self.l_frame)
        self.m_list.grid(row=2,column=0,padx=(10,0),pady=10,sticky=N)
        self.sc.configure(command=self.m_list.yview)
        self.m_list.configure(yscrollcommand=self.sc.set,font=self.myFont)
        self.sc.grid(row=2,column=0,sticky=N+S+E)


        select_label1 = Label(self.l_frame,text="Select Book",fg="blue",font=self.myFont)
        select_label1.grid(row=5,column=0)

        self.b_search_entry = Entry(self.l_frame,bd=5,width=40,font=self.myFont)
        self.b_search_entry.grid(row=6,column=0)
        self.b_search_entry.bind('<KeyRelease>',self.b_search_fun)
        
        self.b_list = Listbox(self.l_frame,width=30,height=5,font=self.myFont)
        self.sc1 = Scrollbar(self.l_frame)
        self.b_list.grid(row=7,column=0,padx=(10,0),pady=10,sticky=N)
        self.sc1.configure(command=self.b_list.yview)
        self.b_list.configure(yscrollcommand=self.sc1.set,font=self.myFont)
        self.sc1.grid(row=7,column=0,sticky=N+S+E)


        self.r_frame = LabelFrame(self,width=400,text="Display",relief=SUNKEN)
        self.r_frame.pack(fill=Y,side=TOP)


        self.choose_list = Listbox(self.r_frame,width=400,height=9,font=self.myFont)
        self.choose_list.grid(row=0,column=0)

        self.choose_list1 = Listbox(self.r_frame,width=400,height=9,font=self.myFont)
        self.choose_list1.grid(row=1,column=0)
        
        

        self.btn = Button(self,text="Issue",width=10,fg="green",font=self.myFont,command=self.btn_fun)
        self.btn.pack()
        
        m_list_fun(self)
        b_list_fun(self)

    def m_search_fun(self,event=None):
        self.m_list.delete(0,END)
        res = self.m_search_entry.get()
        query = "select m_id,name from member where name like %s"
        val = ('%'+res+'%',)
        cursor.execute(query,val)
        result = cursor.fetchall()
        for i in result:
            count = 0
            self.m_list.insert(count,str(i[0])+"-"+str(i[1]))
            count +=1
            
    def b_search_fun(self,event=None):
        self.b_list.delete(0,END)
        res = self.b_search_entry.get()
        query = "select book_id,title from book where title like %s"
        val = ('%'+res+'%',)
        cursor.execute(query,val)
        result = cursor.fetchall()
        for i in result:
            count = 0
            self.b_list.insert(count,str(i[0])+"-"+str(i[1]))
            count +=1        

    def btn_fun(self):
        
        m_id = self.res.split('-')[0]
        book_id = self.res1.split('-')[0]

        query = "update member set status=1 where m_id=%s"
        val = (m_id,)
        cursor.execute(query,val)
        con.commit()

        query1 = "update book set book_status=1 where book_id=%s"
        val1 = (book_id,)
        cursor.execute(query1,val1)
        con.commit()

        query2 = "insert into issue(book_id,m_id) value(%s,%s)"
        val2 = (book_id,m_id,)
        cursor.execute(query2,val2)
        con.commit()

        self.choose_list.delete(0,END)
        self.choose_list1.delete(0,END)
        self.destroy()
        


   


    


    
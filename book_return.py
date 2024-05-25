from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import mysql.connector as mysql


con = mysql.connect(host="localhost",user="root",password="",database="library")
cursor = con.cursor()

class Bookreturn(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.title("Books Issue Details...!")
        self.geometry("800x800")
        self.myFont = font.Font(family='Verdana',size=10,weight="bold",slant="italic")

        def m_list_fun(self): # auto load member list code
            query = "select m_id,name from member where status=%s"
            v = (1,)
            cursor.execute(query,v)
            res = cursor.fetchall()
            for i in res:
                count = 0
                self.m_list.insert(count,str(i[0])+"-"+str(i[1]))
                count +=1

            def m_select_fun(event=None):
                self.res = str(self.m_list.get(self.m_list.curselection()))
                value = self.res.split("-")[0]
                self.m_id=value
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
                
                query1 = "select book_id from issue where m_id=%s"
                val1 = (value,)
                
                cursor.execute(query1,val1)
                result1 = cursor.fetchall()
                self.book_id = result1[0][0]
                
                query2 = "select * from book where book_id=%s"
                val2 = (result1[0][0],)
                cursor.execute(query2,val2)
                result2 = cursor.fetchall()
                for j in result2:
                    self.choose_list.insert(0,"Title :-"+str(j[1]))
                    self.choose_list.insert(1,"Author :-"+str(j[2]))
                    self.choose_list.insert(2,"Pages :-"+str(j[3]))
                    self.choose_list.insert(3,"Price :-"+str(j[4]))
                    self.choose_list.insert(4,"Publisher :-"+str(j[5]))
                    self.choose_list.insert(5,"Categories :-"+str(j[6]))

            self.m_list.bind('<<ListboxSelect>>',m_select_fun)        

        
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


        

        self.r_frame = LabelFrame(self,width=400,text="Display",height=10,relief=SUNKEN)
        self.r_frame.pack(fill=Y,side=TOP)


        self.choose_list = Listbox(self.r_frame,width=400,height=15,font=self.myFont)
        self.choose_list.grid(row=0,column=0)
        

        
        
        

        self.btn = Button(self,text="Return",width=10,fg="green",font=self.myFont,command=self.btn_fun)
        self.btn.pack()
        
        m_list_fun(self)
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
    def btn_fun(self):
        self.m_id
        self.book_id

        query = "update member set status=0 where m_id=%s"
        val = (self.m_id,)
        cursor.execute(query,val)
        con.commit()

        query1 = "update book set book_status=0 where book_id=%s"
        val1 = (self.book_id,)
        cursor.execute(query1,val1)
        con.commit()

        query2 = "delete from issue where book_id=%s and m_id=%s"
        val2 = (self.book_id,self.m_id,)
        cursor.execute(query2,val2)
        con.commit()

        self.destroy()



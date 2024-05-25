from tkinter import*
from PIL import ImageTk
import time
root = Tk()
root.title("I am Neha")
root.geometry("1350x700+0+0")
class Slider:
    def __init__(self,root):
        self.root = root
        self.image1 = ImageTk.PhotoImage(file='images/26.JPG')
        self.image2 = ImageTk.PhotoImage(file='images/27.JPG')
        self.image3 = ImageTk.PhotoImage(file='images/28.JPG')
        self.image4 = ImageTk.PhotoImage(file='images/29.JPG')

        Frame_slider = Frame(self.root)
        Frame_slider.place(x=10,y=50,width=1200,height=500)
        self.lbl1 = Label(Frame_slider,image=self.image1,bd=0)
        self.lbl1.place(x=0,y=0)

        self.lbl2 = Label(Frame_slider,image=self.image2,bd=0)
        self.lbl2.place(x=1200,y=0)        
        self.x=1200
        self.count = 0
        self.slider_func()

    def slider_func(self):
        self.x-=1
    
        if self.x==0:

            self.x=1200 
            time.sleep(1)
            # ****************multiple image slide show code ********************************
            images = [self.image2,self.image3,self.image4,self.image1]
            length = len(images)
            
            self.lbl1.config(image=images[self.count])
            self.count= self.count + 1
            self.lbl2.config(image=images[self.count])
            if self.count == length-1:
                self.lbl1.config(image=images[self.count])
                self.count = 0
                self.lbl2.config(image=images[self.count])
            
            # ****************************only two image slide show code *************************
            # self.new = self.image1
            # self.image1 = self.image2
            # self.image2 = self.new
            # self.lbl1.config(image=self.image1)
            # self.lbl2.config(image=self.image2)   
        self.lbl2.place(x=self.x,y=0)
        self.lbl2.after(1,self.slider_func)









obj = Slider(root)
root.mainloop()

#### Image Processing GUI Start Page ####
from tkinter import *
from login import *
start = Tk()
start.title("Welcome")
start.config(background="black")
start.geometry("500x300")
Label(start,text="WELCOME",font=("courier",24),background="white").grid(row=1,column=1,padx=80,pady=40,ipadx=100,ipady=10)
Button(start,text="Proceed",command=lambda:log(start)).grid(row=2,column=1,ipadx=40,ipady=10,padx=100,pady=40)
mainloop()

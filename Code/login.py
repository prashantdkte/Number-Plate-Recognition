#### Image Processing GUI Login Page ####
from tkinter import *
import mysql.connector 
from tkinter import messagebox
import mysql.connector
import route
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="",
	database="vehicle")
mycursor = mydb.cursor()
mycursor.execute("create table if not exists login(username varchar(255),password varchar(255))")

def login(text2,text3,r):
	username = text2.get()
	password = text3.get()
	if(username=="" or password==""):
		print("Empty Input")
		messagebox.showinfo("Empty Input","Please fill all details")
	else:
		mycursor.execute("Select * from login")
		myresult=mycursor.fetchall()
		x=(username,password)
		if x in myresult:
			print("Login Successful Welcome ",x[0])
			messagebox.showinfo("Login Successfull","Welcome To GUI Python")
			route.run(r)
		else:
			print("Invalid Credentials")
			messagebox.showinfo("Login Failed","Enter Correct Credentials")
def register():
	r1 = Tk()
	r1.config(background="light blue")
	r1.title("Register")
	Label(r1, text="Registration Form",bg="light blue").grid(row=0,column=0,padx=20,pady=20,columnspan=2)
	Label(r1, text="Enter Name",bg="light blue").grid(row=1,column=0,padx=20,pady=20)
	Label(r1, text="Enter Username",bg="light blue").grid(row=2,column=0,padx=20,pady=20)
	Label(r1, text="Enter Address",bg="light blue").grid(row=3,column=0,padx=20,pady=20)
	Label(r1, text="Enter contact no.",bg="light blue").grid(row=4,column=0,padx=20,pady=20)
	Label(r1, text="Enter city",bg="light blue").grid(row=5,column=0,padx=20,pady=20)
	Label(r1, text="Enter password",bg="light blue").grid(row=6,column=0,padx=20,pady=20)
	e1=Entry(r1)
	e2=Entry(r1)
	Entry(r1).grid(row=1,column=1,padx=20,pady=20,ipadx=30)
	e1.grid(row=2,column=1,padx=20,pady=20,ipadx=30)
	Entry(r1).grid(row=3,column=1,padx=20,pady=20,ipadx=30)
	Entry(r1).grid(row=4,column=1,padx=20,pady=20,ipadx=30)
	Entry(r1).grid(row=5,column=1,padx=20,pady=20,ipadx=30)
	e2.grid(row=6,column=1,padx=20,pady=20,ipadx=30)
	Button(r1, text="Register",command=lambda:reg(e1,e2,r1)).grid(row=7,column=0,columnspan=2,padx=20,pady=20)

	
def reg(un,pw,r1):
	username = un.get()
	password = pw.get()
	if(username=="" or password==""):
		print("Empty Input")
		messagebox.showinfo("Empty Input","Please fill all details")
	else:
		mycursor.execute("insert into login values(%s,%s)",(username,password))
		messagebox.showinfo("Success","User Successfully Registered")
		mydb.commit()
		r1.destroy()
	
def log(start):
	start.destroy()
	r = Tk()
	r.config(background="light blue")
	r.geometry("550x300")
	r.title("Login")
	title = Label(r, text="Login Form",bg="light blue")
	title.config(font=("Algerian",20))
	text = Label(r, text="Enter Username",bg="light blue")
	text1 = Label(r, text="Enter Password",bg="light blue")
	text2= Entry(r)
	text3 = Entry(r)
	b1 = Button(r,text="Login",command=lambda:login(text2,text3,r))
	b2 = Button(r,text="Register",command=register)
	b3 = Button(r,text="Quit",command=r.destroy)	
	title.grid(row="0",column="0",columnspan=2,padx=50,pady=15)
	text.grid(row="1",column="0",padx=20,pady=20)
	text1.grid(row=2,column=0,padx=20,pady=20)
	text2.grid(row=1,column=1,ipadx=50,padx=30,pady=20)
	text3.grid(row=2,column=1,ipadx=50,padx=30,pady=20)
	b1.grid(row=3,column=0,ipadx=60,padx=50,pady=5)	
	b2.grid(row=3,column=1,ipadx=60,pady=5)
	b3.grid(row=4,column=0,columnspan=2,ipadx=60,padx=50,pady=15)
	mainloop()
	
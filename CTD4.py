from tkinter import *
import hashlib
import re

root = Tk()
root.geometry("700x400")
root.config(bg="light grey")
root.title("                                                                              Login")

password = "SuperHardPassword99"
hashpass = hashlib.new("md5",password.encode("utf-8")).hexdigest()

def click():
  user = userInput.get()
  pas = passInput.get()
  hpass = hashlib.md5(pas.encode("utf-8")).hexdigest()
  
  regex = "[@_!#$%^&*()<>?/\|}{~:]"
  special = re.compile(regex)
  
  if  user == "guest" and hpass == hashpass:
    Label(root, text="Thats right! Login is sucsseful!", fg="green", font="bold").place(x= 160, y=300)
  elif user == "" or pas == "":
    Label(root, text="Enter tht username or the password!", fg="red", font="bold").place(x= 160, y=300)
  elif special.search(user) != None or special.search(pas):
    Label (root, text="There is speacial charcther in the Username!", fg="red", font="bold").place(x= 160, y=300)
  else:
    Label (root, text="Wrong Username or password", fg="red", font="bold").place(x= 160, y=300)

userInput = Entry(root, font="sans",width=20, fg="blue")
passInput = Entry(root, font="sans",width=20, fg="blue")
userInput.place(x=260,y=35)
passInput.place(x=260, y=105)
passInput.config(show="•")

username = Label (root, text= "Username: ",font="bold",bg ="light grey").grid(row=0,column=  0, pady=30, padx=150)
password = Label (root, text= "Password: ",font="bold",bg ="light grey").grid(row=1,column=  0, pady=10, padx= 150)
button = Button (root, text="Login" ,  padx= 30, pady=10, fg="black",border=1,bg="light grey", command=click).place(x=240,y= 180)

root.mainloop()
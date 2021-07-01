from tkinter import *

def button():
    user = username.get()
    pasword = password.get()
    Label(Window, text=f" Mr. {user} you have submited successfully Thank you",fg="green", font= "Arial 10 bold").grid(row=4, column=2)
Window=  Tk()
Label(Window,text="Login Form",font = "Arial 30 bold ").grid(row=0,column=2)

Label(Window, text="UserName: - ", font = "Arial 15",fg="blue",padx=20).grid(row=1,column=1)
Label(Window,text="Password: - ", font = "Arial 15", fg="blue",padx=20).grid(row=2, column=1)

username = StringVar()
password = StringVar()

Entry(Window,textvariable=username).grid(row=1, column=2)
Entry(Window, textvariable = password).grid(row=2, column=2)

Submit_button = Button(Window, text="Submit it", bg="blue", fg="white", padx=10,pady=5,command=button).grid(row=3, column=2)
Window.minsize(height=250, width=550)
Window.maxsize(height=250, width=800)
Window.resizable(None)
Window.geometry("500x500")

Window.mainloop()


# Importing tkinter
import tkinter
from tkinter import font
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter.filedialog import askopenfile,asksaveasfile
from tkinter.filedialog import *
import tkinter.messagebox as tmsg
import os 
import PIL.Image
import PIL.ImageTk
from tkinter import *



# Functions area
def NewFile():
    global file
    Window.title("Untitle-Notepade File")
    file = None
    text.delete(1.0,END)

def OpenFile():
    global file
    file = askopenfilename(defaultextension = "txt",filetypes = [("All Files","*.*"),("Text Document","*.txt")])
    if(file == ""):
        file = None
    else:
        Window.title(os.path.basename(file) + "- Notepad")
        text.delete(1.0,END)
        f = open(file,"r")
        text.insert(1.0,f.read())
        f.close()

def SaveFile():
        global file
        if(file == None):
            file = asksaveasfilename(initialfile = "Untitle.txt",defaultextension = "txt",
        filetypes = [("All Files","*.*"),("Text Document","*.txt")])
            if(file == ""):
                file = None
            else:
                f = open(file,"w")
                f.write(text.get(1.0,END))
                f.close()

                Window.title(os.path.basename((file) + "- Notepad"))
        else:
            f = open(file,"w")
            f.write(text.get(1.0,END))
            f.close()



def SaveAsFile():
   pass

def Exit():
     Window.destroy()

# Edit Menu functions
def Cut():
    text.event_generate(("<<Cut>>"))

def Copy():
    text.event_generate(("<<Copy>>"))

def Paste():
    text.event_generate(("<<Paste>>"))

def Undo():
    print("Undo file")

def Redo():
    print("Redo File")

def Find():
    print("Find")

def Replace():
    print("Reaplce")

# View Menu functions
def ZoomIn():
    pass

def ZoomOut():
    pass

#Help Menu functions

def About():
    showinfo("Notepad","Created by Nikhil Gupta")

def Help():
    showinfo("Note Pade Help portel","We will contact for help \n Thank You!")


  
#Creating a window with tkinter
Window = Tk()


# Adding title of window
Window.title('My Notepade')

# Adding Frames widget in tkinter background
    #background =  this provide bg color in frame
    # borderwidth = This is provide borderwidth around the frame
    # relif =SUNKEN: -  Adding inside border in frame

#frame = Frame(Window, background="gray", borderwidth=6,relief=SUNKEN)

# frame_1 = Frame(Window,bg="gray", relief=SUNKEN, borderwidth=8)

# Adding Image in texteditor type png only 
# photo = PhotoImage(file="1.png")

# For adding photo in jpg
# Adding Image in texteditor type jpg

#image = PIL.Image.open("1.png")

# Reszie the image using resize() method

#resize_image = image.resize((100, 100))

# Loading image in window

# photo= PIL.ImageTk.PhotoImage(resize_image)
# label = Label(frame,image = photo)
# label.pack()


# Adding Icon
Window.wm_iconbitmap("1.ico")

# Adding Scrol bar
scrolbar = Scrollbar(Window)
# packing scrol bar
scrolbar.pack(side=RIGHT, fill=Y)

# Adding Text area
    # yscrolcommand is adding scrol bar in text area
text = Text(Window,yscrollcommand=scrolbar.set)
file = None
# Configration of scrol bar
scrolbar.config(command=text.yview)
# text.pack is always come after the configrtion of scrol bar
text.pack(fill=BOTH,expand=True)

#Adding Status bar in note pade
    # First we create string input variable
stringvar = StringVar()
    # second we create a label
sbar  = Label(Window,textvariable=stringvar,relief=SUNKEN,anchor="w")
    # Third we set the string variable
stringvar.set("Ready")
    # We pack the label
sbar.pack(fill=X,side=BOTTOM)


#Adding menu bar in our notepad
    # Adding menu by menu function
mainmenu = Menu(Window)
    # Adding drop down menu in file menu with tearoff 
    # Tearoff means that we can't pick dropdown out side the file menu
file_menu = Menu(mainmenu,tearoff=0)

# Adding Drop down fieatuers in file menu
file_menu.add_command(label="New File",command = NewFile)
file_menu.add_command(label="Open", command=OpenFile)
file_menu.add_command(label="Save",command=SaveFile)
file_menu.add_command(label="Save As",command=SaveAsFile)
# Adding saperator in dropdown in file menu
file_menu.add_separator()
file_menu.add_command(label="Exit",command=Exit)

# Adding cascade in file menu
mainmenu.add_cascade(label="File", menu=file_menu)
# Configer the file menu in tkinter
Window.config(menu=mainmenu)




# Adding edit menu
    # Adding drop down menu in file menu with tearoff 
    # Tearoff means that we can't pick dropdown out side the file menu
edit_menu = Menu(mainmenu,tearoff=0)

# Adding Drop down fieatuers in file menu
edit_menu.add_command(label="Cut",command=Cut)
edit_menu.add_command(label="Copy", command=Copy)
edit_menu.add_command(label="paste",command=Paste)
edit_menu.add_separator()
edit_menu.add_command(label = "Undo",command=Undo)
edit_menu.add_command(label = "Redo",command=Redo)
# Adding saperator in dropdown in edit menu
edit_menu.add_separator()
edit_menu.add_command(label = "Find",command=Find)
edit_menu.add_command(label = "Replace",command=Replace)


# Adding cascade in edit menu
mainmenu.add_cascade(label="Edit", menu=edit_menu)
# Configer the eidt menu in tkinter
Window.config(menu=mainmenu)



# Adding view menu
    # Adding drop down menu in view menu with tearoff 
    # Tearoff means that we can't pick dropdown out side the file menu
view_menu = Menu(mainmenu,tearoff=0)

# Adding Drop down fieatuers in view menu
view_menu.add_command(label="Zoom in",command=ZoomIn)
view_menu.add_command(label="Zoom out", command=ZoomOut)

# Adding cascade in view menu
mainmenu.add_cascade(label="View", menu=view_menu)
# Configer the view menu in tkinter
Window.config(menu=mainmenu)


# Help Menu
help_menu = Menu(mainmenu,tearoff=0)

# Adding Drop down fieatuers in view menu
help_menu.add_command(label="Help",command=Help)
help_menu.add_command(label="About",command=About)

# Adding cascade in view menu
mainmenu.add_cascade(label="Help", menu=help_menu)
# Configer the view menu in tkinter
Window.config(menu=mainmenu)





# # Adding Labels
# label_top = Label(frame_1,text="This is Nikhil Gupta",font = "Arial 19")
# label_top.pack()

# Adding Buttons in Left_Frame
    # New button: - 
        #fg = four ground color
        # bg  = background color
        # text = Save, print etc
        # pdx = padding in x direction
# button_left_New = Button(frame,fg="white",bg="blue",text="New",padx=50)
# button_left_New.pack()

    # open button: - 
            #fg = four ground color
            # bg  = background color
            # text = Save, print etc
#             # pdx = padding in x direction
# button_left_open = Button(frame,fg="white",bg="blue",text="Opena",padx=50)
# button_left_open.pack()




# Gemotry organization
    # side = side is taking it to left ,right,top ,botton
    # fill = fill make it's  resizeable in x, ydirection
    # padx, pady = padx giving padding to x and y

#frame.pack(side=LEFT,fill=Y,padx=0)
# frame_1.pack(side=TOP, fill=X,padx=0)

# Setting the gemotry of Note pade
Window.geometry('1000x500')
# Minsize function maitain the minimum size of our gui
Window.minsize(50,50)
# Starting main loop
Window.mainloop()




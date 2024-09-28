from tkinter import *
from tkinter.ttk import *

# creating the main tkinter window
root = Tk()
root.title('Menu Demonstration')

# Creating menubar

menubar = Menu(root)

# Adding the file meny

# tearoff = cannot be torn off into a spereate window
file = Menu(menubar, tearoff = 1)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label="New File", command = None)
file.add_command(label="Save", command = None)
file.add_command(label="Edit", command = None)
file.add_separator()
file.add_command(label="Exit", command = root.destroy)




e = Entry(root,width = 100,background= 'white',foreground= 'black')
e.pack()
# e.insert(0, "Enter your name")
def myClick():
    hello = "Hello "+ e.get()
    myLabel = Label(root,text=hello)
    myLabel.pack() 
    

def fade(event):
    if e.get == "Enter your name":
        e.delete(0,"end")
        e.config(foreground= 'black')

e.bind("<FocusIn>",fade)
# Dislay the menu
root.config(menu = menubar)



root.mainloop()
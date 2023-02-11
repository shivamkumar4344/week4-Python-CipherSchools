import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Menubar")

def ntf():
    print("New text file")
    
def reset():
    print("This is a function resets all..")
    
def nf():
    print("New file created.")
    
def nw():
    print("New window created.")

def save():
    print("This is a function save the file")
    
def save_as():
    print("This is save as")
    
def save_all():
    print("This is a function save all..")
    
def undo():
    print("undo the things")

def redo():
    print("redo the things")
    
def cut():
    print("This command cut the text,images,etc.")
    
def paste():
    print("This command paste the text,images,etc.")
    
def copy():
    print("This command copy the text,images,etc.")
    
def paletee():
    print("This command paletee things.")

def ov():
    print("This command helps us to open view")
    
def ww():
    print("This command helps in word wrap.")

def ss():
    print("This command helps in sticky scrolls.")
    
def sd():
    print("this is for the start of debugging")

def rwd():
    print("this is for run without debugging")
    
def add_two():
    print("Cofigurartion added")


def lis():
    print("https://code.visualstudio.com/license?lang=en")
    
def about():
    print("about visual code studio.")




#SIMPLE MENUBAR
# menubar = tk.Menu(win)

# menubar.add_command(label= "Save",command = ntf)
# menubar.add_command(label= "Save As",command = save_as)
# menubar.add_command(label= "Reset",command = reset)

# win.config(menu=menubar)

#DROP_DOWN MENUBAR

main_menu = tk.Menu(win)

#File Menu
file_menu = tk.Menu(main_menu,tearoff=0)
file_menu.add_command(label="New Text File",command=ntf)
file_menu.add_command(label="New File",command=nf)
file_menu.add_command(label="New Window",command=nw)
file_menu.add_separator()
file_menu.add_command(label="Save",command=save)
file_menu.add_command(label="Save As",command=save_as)
file_menu.add_command(label="Save All",command=save_all)

#Edit Menu
edit_menu = tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label = "Undo",command = undo)
edit_menu.add_command(label = "Redo",command = redo)
edit_menu.add_separator()
edit_menu.add_command(label = "Cut",command = cut)
edit_menu.add_command(label = "Paste",command = paste)
edit_menu.add_command(label = "Copy",command = copy)

#View Menu
view_menu = tk.Menu(main_menu,tearoff=0)
view_menu.add_command(label="Command Paletee..",command=paletee)
view_menu.add_command(label="Open View...",command=ov)
view_menu.add_separator()
view_menu.add_command(label="Word Wrap",command=ww)
view_menu.add_command(label="Sticky Scroll",command=ss)

#Run menu
run = tk.Menu(main_menu,tearoff=0)
run.add_command(label="Start Debugging",command=sd)
run.add_command(label="Run without Debugging",command=rwd)
run.add_separator()
run.add_checkbutton(label="Add Congiguration",command=add_two)

#Help Menu
help_menu = tk.Menu(main_menu,tearoff=0)
help_menu.add_command(label="Welcome")
help_menu.add_command(label="Show all commands")
help_menu.add_separator()
help_menu.add_command(label="View License",command=lis)
help_menu.add_command(label="Privacy Statement")
help_menu.add_separator()
help_menu.add_command(label="About",command=about)


# cascading the menu items means arranging it in menu bar.
main_menu.add_cascade(label="File",menu=file_menu)
main_menu.add_cascade(label="Edit",menu=edit_menu)
main_menu.add_cascade(label="View",menu=view_menu)
main_menu.add_cascade(label="Run",menu=run)
main_menu.add_cascade(label="Help",menu=help_menu)

win.config(menu=main_menu)

win.mainloop()

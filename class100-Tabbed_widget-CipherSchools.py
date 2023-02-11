import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("TAB WIDGET")
nb = ttk.Notebook(win)
page1 = ttk.Frame(nb)
page2 = ttk.Frame(nb)
nb.add(page1,text="ONE")
nb.add(page2,text="TWO")
nb.pack(expand=True, fill='both')
#making label for page 1
label1 = ttk.Label(page1, text='This is label:')
label1.grid(row=0,column=0)
#making label for page 2
label2 = ttk.Label(page2, text="This is a label:")
label2.grid(row=0,column=0)
#entry for page 1
entry1 = ttk.Entry(page1 ,width=25)
entry1.grid(row=0,column=1)

win.mainloop()

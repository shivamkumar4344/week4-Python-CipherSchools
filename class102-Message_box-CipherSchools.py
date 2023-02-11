import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as m_box
win = tk.Tk()
win.title("MESSAGES")

#label frame
label_frame = ttk.LabelFrame(win,text="Contact Details")
label_frame.grid(row =0,column=0,padx=40,pady=10)

#labels
name_label = ttk.Label(label_frame,text="Enter your name:-",font=("helvetica",14))
age_label = ttk.Label(label_frame,text="Enter your age:-",font=("helvetica",14))

#entry_box varibles

name_var = tk.StringVar()
age_var = tk.StringVar()

#entry boxes

name_entry = ttk.Entry(label_frame,width=36,textvariable=name_var)
age_entry = ttk.Entry(label_frame,width=36,textvariable=age_var)

#grid
name_label.grid(row=0,column = 0,padx=5,pady=5,sticky=tk.W)
age_label.grid(row=0,column=1,padx=5 , pady=5,sticky=tk.W)
name_entry.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)
age_entry.grid(row=1,column=1,padx=5,pady=5,sticky=tk.W)

def submit():
    name = name_var.get()
    age = age_var.get()
    if name == '' or age == '':
        m_box.showerror('Error','Please input age as well as name')
    else:
        try:
            age = int(age)
        except ValueError():
            m_box.showerror('ERROR','Please input numbers as age')
        else:
            if age<18:
                m_box.showwarning('Warning','You are under 18 ,you have to open the site at your own risk.')
            print(f"Your name is :{name} and Your age is: {age}")

#button
submit_btn = ttk.Button(win,text="Submit",command=submit)
submit_btn.grid(row=1,columnspan=2,padx=40)

win.mainloop()
import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("INFO")
labels = ["What is your name: ","What is your age: ","Gender: ","State: ","City: ","Pin_code: "]

for i in range(len(labels)):
    curr_label = "labels" + str(i)   #  label1 label2 label3
    curr_label = ttk.Label(win, text=labels[i])
    curr_label.grid(row=i, column=0 ,sticky=tk.W)

#entry box

user_info = {
    'name' : tk.StringVar(),
    'age' : tk.StringVar(),
    'gender' : tk.StringVar(),
    'state' : tk.StringVar(),
    'city' : tk.StringVar(), 
    'pin_code' : tk.StringVar()
}
conter = 0
for i in user_info:
    curr_entrybox = 'entry' + i
    curr_entrybox = ttk.Entry(win,width=20,textvariable=user_info[i])
    curr_entrybox.grid(row=conter,column=1)
    conter+=1
    
#submit

def submit():
    print(user_info["name"].get())
    print(user_info["age"].get())
    print(user_info["gender"].get())
    print(user_info["state"].get())
    print(user_info["city"].get())
    print(user_info["pin_code"].get())
    
submit_btn = ttk.Button(win, text="Submit Now", command=submit)
submit_btn.grid(row=7,columnspan=2)




win.mainloop()


import tkinter as tk
from tkinter import messagebox
root=tk.Tk()
root.title("Student Registration Form")
root.geometry("300x200")
root.configure(bg="light gray")

def submit():
    name=name_textbox.get()
    email=email_textbox.get()
    phone=phone_textbox.get()
    if name and email and phone:
        str="""Name = """+name+"""
        Email ="""+email+"""
        phone ="""+phone
        messagebox.showinfo("Captured Entry",str)
    else:
        messagebox.showwarning("Warnning","please fill all feilds")


name_label=tk.Label(root,text="Enter Your Name")
name_label.pack(anchor=tk.W,padx=10)
name_textbox=tk.Entry(root)
name_textbox.pack(anchor=tk.W,padx=10)

email_label=tk.Label(root,text="Enter Your email")
email_label.pack(anchor=tk.W,padx=10,pady=10)
email_textbox=tk.Entry(root)
email_textbox.pack(anchor=tk.W,padx=10)

phone_label=tk.Label(root,text="Enter Your phone")
phone_label.pack(anchor=tk.W,padx=10,pady=10)
phone_textbox=tk.Entry(root)
phone_textbox.pack(anchor=tk.W,padx=10)

submit_btn=tk.Button(root,text="Submit",command=submit)
submit_btn.pack(anchor=tk.W,padx=10,pady=10)

root.mainloop()
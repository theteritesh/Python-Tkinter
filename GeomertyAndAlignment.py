import tkinter as tk
root=tk.Tk()
root.title("Student Registration Form")
root.geometry("300x200")
root.configure(bg="light gray")

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

submit_btn=tk.Button(root,text="Submit")
submit_btn.pack(anchor=tk.W,padx=10,pady=10)

root.mainloop()
import tkinter as tk
root=tk.Tk()
root.title("Student Registration Form")

name_label=tk.Label(root,text="Enter Your Name")
name_label.pack()
name_textbox=tk.Entry(root)
name_textbox.pack()

email_label=tk.Label(root,text="Enter Your email")
email_label.pack()
email_textbox=tk.Entry(root)
email_textbox.pack()

phone_label=tk.Label(root,text="Enter Your phone")
phone_label.pack()
phone_textbox=tk.Entry(root)
phone_textbox.pack()

submit_btn=tk.Button(root,text="Submit")
submit_btn.pack()

root.mainloop()
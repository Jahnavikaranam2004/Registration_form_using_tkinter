import tkinter as tk
from tkinter import messagebox

def form_submission():
    name = entry_name.get()
    rollno = entry_rollno.get()
    email = entry_email.get()
    age = entry_age.get()
    CollegeName= entry_clgname.get()
    Address = entry_address.get()
 
    if name == '' or rollno =='' or email == '' or age == '' or CollegeName == '' or Address == '' :
        messagebox.showwarning("Incomplete Form", "Please fill all fields")
    else:
        messagebox.showinfo("Submitted", f"Name: {name} \nRollno: {rollno}\nEmail: {email}\nAge: {age}\nCollegeName: {CollegeName}\nAddress: {Address}")
root = tk.Tk()
root.title("Registration Form")

# Create labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_rollno = tk.Label(root, text="RollNo:")
label_rollno.grid(row=1, column=0, padx = 10, pady =5)
entry_rollno= tk.Entry(root)
entry_rollno.grid(row=1, column=1, padx=10, pady = 5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_age = tk.Label(root, text="Age:")
label_age.grid(row=3, column=0, padx=10, pady=5)
entry_age = tk.Entry(root)
entry_age.grid(row=3, column=1, padx=10, pady=5)

label_CollegeName = tk.Label(root, text="ClgName:")
label_CollegeName.grid(row=4,column=0, padx=10, pady=5)
entry_clgname = tk.Entry(root)
entry_clgname.grid(row=4, column=1, padx=10, pady=5)

label_Address = tk.Label(root, text="Address:")
label_Address.grid(row=5,column=0, padx=10, pady=5)
entry_address = tk.Entry(root)
entry_address.grid(row=5, column=1, padx=10, pady=5)


submit_button = tk.Button(root, text="Submit", command=form_submission)
submit_button.grid(row=6, column=0, columnspan=2, pady=10)


root.mainloop()

 Documentation for Registration form

This Python script utilizes Tkinter to create a registration form GUI with entry fields for name, roll number, email, age, college name, and address.
It includes validation to ensure all fields are filled before form submission. if anyone of the field is not filled then form is not submitted and it shows an message that incomplete form, please fill all the fields.
after clicking the "Submit" button, appropriate messages are displayed using Tkinter's messagebox module based on the validity of the form data.

Modules used:
	
 	tkinter: it is Python's standard GUI (Graphical User Interface) toolkit.
	
 	messagebox: it is a submodule of Tkinter used to display various types of message boxes, such as warnings or information messages etc.


Main Window (root):
	
 	tk.Tk(): Creates the main window of the registration form.
	
 	title("Registration Form"): Sets the title of the window to "Registration Form".


Labels and Entry Fields:

	
 Labels (tk.Label):
	
 	
  	1)Created for each filed to display information about that field.
	
 	2)Positioned using the grid method with specific row and column indices (row, column). at which row and which column the filed should display.
	
 	3)for spacing purpose i used padx (x- axis padding) and pady(y-axis padding)and added spacing around the labels for better view.


Entry Fields (tk.Entry):
	
 	1)To take input from user i used tk.Entry.
		
  	2)By using grid method we positioned each column and row indices.
	
 	3)Each Entry field (entry_name, entry_rollno,entry_email, entry_age, entry_clgname and entry_address) allows users to enter data.


form_submission Function:
		
  	1)Retrieves the user entered data from each Entry field (entry_name.get(), entry_rollno.get(),entry_email.get(), entry_age.get(), entry_clgname.get() and 
   		entry_address.get()).
	
 	2)Next it Checks if any of the fields are empty (name == '', rollno == '', or email == '', age == '' or CollegeName == '' or Address == '').
	
 	3)If any field is empty, displays a warning message using messagebox.showwarning.
	
 	4)If all fields are filled, displays an information message using messagebox.showinfo showing the entered data concatenated into a formatted string.


Button (tk.Button):
	
 	1)this function Creates a button labeled "Submit".
	
 	2)it Binds the form_submission function to the button's command parameter, so form_submission is called when the button is clicked.
	
 	3)Positioned using grid with row=6 (row index 6), column=0 (column index 0), columnspan=2 (spans across 2 columns), and pady=10 (y-axis padding).


root.mainloop():
	
 	1)Starts the Tkinter event loop, which listens for events (such as button clicks) and updates the GUI accordingly.
	
 	2)The program remains in this loop until the window is closed by the user.



Run the Python script.

	The GUI window titled "Registration Form" will appear.

	Enter information into each field (Name, RollNo, Email, Age, ClgName, Address).

	Click the "Submit" button to either see a confirmation message with the entered data or a warning if any field is empty.

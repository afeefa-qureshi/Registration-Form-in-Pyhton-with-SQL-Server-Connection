import pyodbc as odbc
import pyodbc
import tkinter as tk
from tkinter import messagebox


DRIVER_NAME = 'SQL Server'
SERVER_NAME ='XACADEMY\SQLEXPRESS'
DATABASE_NAME ='Registration_Form'

connection_string = f'DRIVER={{{DRIVER_NAME}}};SERVER={{{SERVER_NAME}}};DATABASE={{{DATABASE_NAME}}}'

try:
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    print("Connected to SQL Server")
    
    cursor.execute("SELECT * FROM Register_details")  
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()

import pyodbc
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import ast 
 

# Create a tkinter window
window = tk.Tk()
window.title("Registration Form")
window.configure(bg='#151547')
window.geometry("1300x700+300+200")  # Set window dimensions
window.resizable(False,False)

# Create a column configuration to center the heading
window.columnconfigure(0, weight=1)
# Add a heading
heading_label = tk.Label(window, text="Registration Form", font=("Arial", 30, "bold"), bg='#151547',fg="white")
heading_label.grid(row=0, column=0, columnspan=2, pady=(40, 50), sticky='n')  
# Create a frame for the left side (image)
left_frame = tk.Frame(window)
left_frame.grid(row=1, column=0, padx=5, pady=5)

image_path = 'A4.png'
bg_image = tk.PhotoImage(file=image_path)

# Calculate the new dimensions to fit within left_frame
max_width = 900
max_height = 300

# Get the original image dimensions
original_width = bg_image.width()
original_height = bg_image.height()

# Calculate the scaling factor for width and height
width_scale = max_width / original_width
height_scale = max_height / original_height

# Choose the smaller scale to ensure the image fits within the frame
scale = min(width_scale, height_scale)

# Resize the PhotoImage using subsample
bg_image = bg_image.subsample(int(1/scale), int(1/scale))

# Create a label with the resized image
image_label = tk.Label(left_frame, image=bg_image, bg="#151547")
image_label.grid(row=0, column=0)


# Create a frame for the right side (registration form)
right_frame = tk.Frame(window, bg='#151547')
right_frame.grid(row=1, column=1, padx=(0), pady=(20,0))


def submit_registration():
    # Get the values from entry fields
    firstname = entry_fname.get()
    lastname = entry_lname.get()
    cnic = entry_cnic.get()
    pnum = entry_pnum.get()
    gender = entry_gender.get()
    email = entry_email.get()
    password = entry_password.get()

    if not firstname or not lastname or not cnic or not pnum or not gender or not email or not password:
        messagebox.showerror("Error", "Please Enter all Details Correctly.")
    else:
        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Registration ([First Name], [Last Name], CNIC, [Phone Number], Gender, Email, Password) VALUES (?, ?, ?, ?, ?, ?, ?)", (firstname, lastname, cnic, pnum, gender, email, password))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registration successful!")
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {e}")
            
# Labels with Custom Styling
label_firstname = tk.Label(right_frame, text="First Name:", font=("Arial", 16,"bold"),bg='#151547',fg="white")
label_lastname = tk.Label(right_frame, text="Last Name:", font=("Arial", 16,"bold"),bg='#151547',fg="white")
label_cnic = tk.Label(right_frame, text="CNIC:", font=("Arial", 16,"bold"),bg='#151547',fg="white")
label_phonenumber = tk.Label(right_frame, text="Phone Number:", font=("Arial", 16,"bold"),bg='#151547',fg="white")
label_gender = tk.Label(right_frame, text="Gender:", font=("Arial", 16,"bold"),bg='#151547',fg="white")
label_email = tk.Label(right_frame, text="Email:", font=("Arial", 16,"bold"),bg='#151547',fg="white")
label_password = tk.Label(right_frame, text="Password:", font=("Arial", 16,"bold"),bg='#151547',fg="white")

# Entry Fields

entry_fname = tk.Entry(right_frame,font=("Arial", 12))
entry_lname = tk.Entry(right_frame, font=("Arial", 12))
entry_cnic = tk.Entry(right_frame, font=("Arial", 12))
entry_pnum = tk.Entry(right_frame, font=("Arial", 12))
entry_gender = tk.Entry(right_frame, font=("Arial", 12))
entry_email = tk.Entry(right_frame, font=("Arial", 12))
entry_password = tk.Entry(right_frame, show="*", font=("Arial", 12))  # Hide the password with '*'



# Submit Button
submit_button = tk.Button(right_frame,width=16,height=1,borderwidth=0,bg="#5f73f1", relief='flat', text="Submit", font=("Arial", 16,"bold"),fg="white", command=submit_registration)
# Place widgets in the window
label_firstname.grid(row=1, column=0,padx=(120, 30),pady=(40,10))
entry_fname.grid(row=1, column=1,pady=(40,10),padx=(20,160))
label_lastname.grid(row=2, column=0,padx=(120, 30))
entry_lname.grid(row=2, column=1, pady=10,padx=(20,160))
label_cnic.grid(row=3, column=0,padx=(120, 30))
entry_cnic.grid(row=3, column=1, pady=10,padx=(20,160))
label_phonenumber.grid(row=4, column=0,padx=(120, 30))
entry_pnum.grid(row=4, column=1, pady=10,padx=(20,160))
label_gender.grid(row=5, column=0,padx=(120, 30))
entry_gender.grid(row=5, column=1, pady=10,padx=(20,160))
label_email.grid(row=6, column=0,padx=(120, 30))
entry_email.grid(row=6, column=1, pady=10,padx=(20,160))
label_password.grid(row=7, column=0,padx=(120, 30))
entry_password.grid(row=7, column=1, pady=10,padx=(20,160))

submit_button.grid(row=8, column=1, pady=(30,10),padx=(10,160))

# Run the tkinter main loop
window.mainloop()

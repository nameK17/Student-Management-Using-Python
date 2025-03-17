
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # blank password
    database="student_db"
)
cursor = conn.cursor()

def add_student():
    if name_var.get() == "" or roll_var.get() == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        cursor.execute("INSERT INTO students (name, roll_no, gender, contact, dob, address) VALUES (%s, %s, %s, %s, %s, %s)",
            (name_var.get(), roll_var.get(), gender_var.get(), contact_var.get(), dob_var.get(), txt_address.get('1.0', tk.END)))
        conn.commit()
        fetch_data()
        clear_fields()

def fetch_data():
    student_table.delete(*student_table.get_children())
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        student_table.insert('', 'end', values=row)

def clear_fields():
    name_var.set("")
    roll_var.set("")
    gender_var.set("")
    contact_var.set("")
    dob_var.set("")
    txt_address.delete("1.0", tk.END)

# Main Window
root = tk.Tk()
root.title("Student Management System")
root.geometry("900x500")

# Variables
name_var = tk.StringVar()
roll_var = tk.StringVar()
gender_var = tk.StringVar()
contact_var = tk.StringVar()
dob_var = tk.StringVar()

# Entry Frame
entry_frame = tk.LabelFrame(root, text="Student Info", font=("Arial", 12, "bold"))
entry_frame.place(x=10, y=10, width=400, height=480)

tk.Label(entry_frame, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="w")
tk.Entry(entry_frame, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(entry_frame, text="Roll No").grid(row=1, column=0, padx=10, pady=5, sticky="w")
tk.Entry(entry_frame, textvariable=roll_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(entry_frame, text="Gender").grid(row=2, column=0, padx=10, pady=5, sticky="w")
ttk.Combobox(entry_frame, textvariable=gender_var, values=["Male", "Female"], state="readonly").grid(row=2, column=1, padx=10, pady=5)

tk.Label(entry_frame, text="Contact").grid(row=3, column=0, padx=10, pady=5, sticky="w")
tk.Entry(entry_frame, textvariable=contact_var).grid(row=3, column=1, padx=10, pady=5)

tk.Label(entry_frame, text="D.O.B").grid(row=4, column=0, padx=10, pady=5, sticky="w")
tk.Entry(entry_frame, textvariable=dob_var).grid(row=4, column=1, padx=10, pady=5)

tk.Label(entry_frame, text="Address").grid(row=5, column=0, padx=10, pady=5, sticky="w")
txt_address = tk.Text(entry_frame, width=30, height=3)
txt_address.grid(row=5, column=1, padx=10, pady=5)

tk.Button(entry_frame, text="Add", command=add_student).grid(row=6, column=0, columnspan=2, pady=10)

# Table Frame
table_frame = tk.Frame(root)
table_frame.place(x=420, y=10, width=460, height=480)

scroll_x = tk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
scroll_y = tk.Scrollbar(table_frame, orient=tk.VERTICAL)
student_table = ttk.Treeview(table_frame, columns=("id", "name", "roll", "gender", "contact", "dob", "address"),
                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
scroll_x.config(command=student_table.xview)
scroll_y.config(command=student_table.yview)

student_table.heading("id", text="ID")
student_table.heading("name", text="Name")
student_table.heading("roll", text="Roll No")
student_table.heading("gender", text="Gender")
student_table.heading("contact", text="Contact")
student_table.heading("dob", text="DOB")
student_table.heading("address", text="Address")
student_table['show'] = 'headings'

student_table.pack(fill=tk.BOTH, expand=1)
fetch_data()

root.mainloop()

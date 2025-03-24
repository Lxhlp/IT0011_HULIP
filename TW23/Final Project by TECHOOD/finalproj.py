import os
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# File to store records
DATA_FILE = "TW23\\Final Project by TECHOOD\\records.txt"

# Function to load records from file
def load_records():
    records = []
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                for line in file:
                    record = line.strip().split(",")
                    records.append(record)
        return records
    except Exception as e:
        messagebox.showerror("Error", f"Error loading records: {e}")
        return []

# Function to save records to file
def save_records(records):
    try:
        with open(DATA_FILE, "w") as file:
            for record in records:
                file.write(",".join(record) + "\n")
    except Exception as e:
        messagebox.showerror("Error", f"Error saving records: {e}")

# Function to format birthday date
def format_birthday(date_str):
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%B %d, %Y")
    except ValueError:
        return date_str

# Function to display the main menu
def show_menu():
    clear_window()
    tk.Label(root, text="Main Menu", font=("Arial", 14, "bold"), bg="#f4f4f4").pack(pady=10)
    
    tk.Button(root, text="Sign Up", command=sign_up_screen, width=20, height=2, bg="#4CAF50", fg="white").pack(pady=5)
    tk.Button(root, text="View All Records", command=view_all_records, width=20, height=2, bg="#2196F3", fg="white").pack(pady=5)
    tk.Button(root, text="Search a Record", command=search_record_screen, width=20, height=2, bg="#FFC107", fg="black").pack(pady=5)
    tk.Button(root, text="Exit", command=exit_program, width=20, height=2, bg="#f44336", fg="white").pack(pady=5)

# Function to clear the window before displaying a new screen
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

# Function to display the sign-up screen
def sign_up_screen():
    clear_window()
    tk.Label(root, text="Sign Up", font=("Arial", 14, "bold"), bg="#f4f4f4").pack(pady=10)
    
    frame = tk.Frame(root, bg="#f4f4f4")
    frame.pack(pady=10)
    
    # Entry fields for user details
    tk.Label(frame, text="First Name:", bg="#f4f4f4").grid(row=0, column=0, sticky="w")
    entry_first_name = tk.Entry(frame)
    entry_first_name.grid(row=0, column=1)
    
    tk.Label(frame, text="Middle Name:", bg="#f4f4f4").grid(row=1, column=0, sticky="w")
    entry_middle_name = tk.Entry(frame)
    entry_middle_name.grid(row=1, column=1)
    
    tk.Label(frame, text="Last Name:", bg="#f4f4f4").grid(row=2, column=0, sticky="w")
    entry_last_name = tk.Entry(frame)
    entry_last_name.grid(row=2, column=1)
    
    tk.Label(frame, text="Birthday (YYYY-MM-DD):", bg="#f4f4f4").grid(row=3, column=0, sticky="w")
    entry_birthday = tk.Entry(frame)
    entry_birthday.grid(row=3, column=1)
    
    tk.Label(frame, text="Gender:", bg="#f4f4f4").grid(row=4, column=0, sticky="w")
    gender_var = tk.StringVar()
    tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="#f4f4f4").grid(row=4, column=1, sticky="w")
    tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="#f4f4f4").grid(row=4, column=2, sticky="w")
    
    # Function to handle form submission
    def submit():
        first_name = entry_first_name.get().strip()
        middle_name = entry_middle_name.get().strip()
        last_name = entry_last_name.get().strip()
        birthday = entry_birthday.get().strip()
        gender = gender_var.get()
        
        if not first_name or not last_name or not birthday or not gender:
            messagebox.showerror("Error", "All fields except Middle Name are required!")
            return
        
        try:
            datetime.strptime(birthday, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format! Use YYYY-MM-DD.")
            return
        
        record = [first_name, middle_name, last_name, birthday, gender]
        records = load_records()
        records.append(record)
        save_records(records)
        messagebox.showinfo("Success", "Record added successfully!")
        show_menu()
    
    tk.Button(root, text="Submit", command=submit, bg="#4CAF50", fg="white").pack(pady=5)
    tk.Button(root, text="Back", command=show_menu, bg="#9E9E9E", fg="white").pack(pady=5)

# Function to search for a record
def search_record_screen():
    clear_window()
    tk.Label(root, text="Search a Record", font=("Arial", 14, "bold"), bg="#f4f4f4").pack(pady=10)
    
    tk.Label(root, text="Enter First or Last Name:", bg="#f4f4f4").pack()
    entry_search = tk.Entry(root)
    entry_search.pack()
    
    # Function to perform search
    def search():
        query = entry_search.get().strip().lower()
        if not query:
            messagebox.showerror("Error", "Please enter a name to search.")
            return
        
        records = load_records()
        matches = [record for record in records if query in record[0].lower() or query in record[2].lower()]
        
        if matches:
            result = "\n\n".join([
                f"Name: {match[2]}, {match[0]} {match[1]}\n"
                f"Birthday: {format_birthday(match[3])}\n"
                f"Gender: {match[4]}"
                for match in matches
            ])
            messagebox.showinfo("Search Results", result)
        else:
            messagebox.showinfo("Search Results", "No matching records found.")
    
    tk.Button(root, text="Search", command=search, bg="#FFC107", fg="black").pack(pady=5)
    tk.Button(root, text="Back", command=show_menu, bg="#9E9E9E", fg="white").pack(pady=5)

# Function to view all records
def view_all_records():
    records = load_records()
    if records:
        result = "\n\n".join([
            f"Name: {record[2]}, {record[0]} {record[1]}\n"
            f"Birthday: {format_birthday(record[3])}\n"
            f"Gender: {record[4]}\n"
            f"{'-'*30}"
            for record in records
        ])
        messagebox.showinfo("All Records", result)
    else:
        messagebox.showinfo("All Records", "No records found.")

# Function to exit the program
def exit_program():
    root.destroy()

# Initialize main window
root = tk.Tk()
root.title("Record Management System")
root.geometry("400x400")
root.configure(bg="#f4f4f4")

show_menu()
root.mainloop()

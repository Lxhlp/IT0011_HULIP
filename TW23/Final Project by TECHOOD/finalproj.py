import os
from datetime import datetime

DATA_FILE = "TW23\\Final Project\\records.txt"

# Load records from the file
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
        print(f"Error loading records: {e}")
        return []

# Save records to the file
def save_records(records):
    try:
        with open(DATA_FILE, "w") as file:
            for record in records:
                file.write(",".join(record) + "\n")
    except Exception as e:
        print(f"Error saving records: {e}")

# Collect user input for sign-up
def collect_user_input():
    print("\n--- Sign-Up Form ---")
    first_name = input("First Name: ").strip()
    middle_name = input("Middle Name: ").strip()
    last_name = input("Last Name: ").strip()
    birthday = input("Birthday (YYYY-MM-DD): ").strip()
    gender = input("Gender (Male/Female): ").strip().capitalize()
    return [first_name, middle_name, last_name, birthday, gender]

# Validate user input
def validate_input(record):
    first_name, middle_name, last_name, birthday, gender = record

    # Check for empty fields
    if not first_name or not last_name or not birthday or not gender:
        print("Error: All fields except Middle Name are required!")
        return False

    # Validate date format
    try:
        datetime.strptime(birthday, "%Y-%m-%d")
    except ValueError:
        print("Error: Invalid date format! Please use YYYY-MM-DD.")
        return False

    # Validate gender
    if gender not in ["Male", "Female"]:
        print("Error: Gender must be 'Male' or 'Female'.")
        return False

    return True

# Append a new record to the file
def sign_up():
    record = collect_user_input()
    if not validate_input(record):
        return

    records = load_records()
    records.append(record)
    save_records(records)
    print("Record added successfully!")

# View all records
def view_all_records():
    records = load_records()
    if not records:
        print("No records found.")
        return

    print("\n--- All Records ---")
    for i, record in enumerate(records, 1):
        print(f"First Name: {record[0]}")
        print(f"Middle Name: {record[1]}")
        print(f"Last Name: {record[2]}")
        print(f"Birthday: {record[3]}")
        print(f"Gender: {record[4]}")
        print("--------------------")

# Main function
def main():
    print("Welcome to the Record Management System")
    while True:
        print("\n--- Menu ---")
        print("[1] Sign-Up")
        print("[2] View all records")
        print("[3] Search a record")
        print("[4] Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            sign_up()
        elif choice == "2":
            view_all_records()
        elif choice == "3":
            print("Search functionality not implemented yet.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
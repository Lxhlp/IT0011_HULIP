# Sample student records (list of tuples)
student_records = [
    (123456, ("Alice", "Smith"), 85, 90),
    (654321, ("Bob", "Johnson"), 78, 82),
    (112233, ("Charlie", "Brown"), 92, 95),
    (445566, ("David", "Williams"), 75, 88),
    (778899, ("Eve", "Davis"), 88, 79),
]

while True:
    print("=====================================")
    print("Student Record Management System")
    print("=====================================")
    print("[1] Open File")
    print("[2] Save File")
    print("[3] Save As File")
    print("[4] Show All Students Record")
    print("[5] Show Student Record")
    print("[6] Add Record")
    print("[7] Edit Record")
    print("[8] Delete Record")
    print("[9] Exit")
    print("-------------------------------------")
    choice = input("Enter your choice: ")

    if choice == "4":  # Show All Students Record
        while True:
            print("=====================================")
            print("Show All Students Record Options:")
            print("=====================================")
            print("[1] Order by Last Name")
            print("[2] Order by Grade (60% Class Standing, 40% Major Exam)")
            print("[3] Back to Main Menu")
            print("-------------------------------------")

            order_choice = input("Enter your order choice: ")

            if order_choice == "1":  # Order by last name
                sorted_records = []
                for record in student_records:
                    sorted_records.append(record)
                
                n = len(sorted_records)
                for i in range(n):
                    for j in range(0, n-i-1):
                        if sorted_records[j][1][1] > sorted_records[j+1][1][1]:
                            sorted_records[j], sorted_records[j+1] = sorted_records[j+1], sorted_records[j]
                
                for record in sorted_records:
                    print(f"ID: {record[0]} \nName: {record[1][0]} {record[1][1]} \nClass Standing: {record[2]} \nMajor Exam: {record[3]}\n")

            elif order_choice == "2":  # Order by grade
                graded_records = []
                for record in student_records:
                    final_grade = (record[2] * 0.6) + (record[3] * 0.4)
                    graded_records.append((final_grade, record))

                n = len(graded_records)
                for i in range(n):
                    for j in range(0, n-i-1):
                        if graded_records[j][0] < graded_records[j+1][0]:
                            graded_records[j], graded_records[j+1] = graded_records[j+1], graded_records[j]

                for grade, record in graded_records:
                    print(f"ID: {record[1][0]} \nName: {record[1][1][0]} {record[1][1][1]} \nGrade: {grade:.2f}\n")
            
            elif order_choice == "3":
                break # Return to main menu.
            
            else:
                print("=====================================")
                print("Invalid order choice.")

    elif choice == "5":  # Show Student Record
        student_id = int(input("Enter Student ID: "))
        found = False
        for record in student_records:
            if record[0] == student_id:
                print(f"ID: {record[0]}, \nName: {record[1][0]} {record[1][1]}, \nClass Standing: {record[2]}, \nMajor Exam: {record[3]}")
                found = True
                break
        if not found:
            print("=====================================")
            print("Student not found.")

    elif choice == "6":  # Add Record
        student_id = int(input("Enter Student ID: "))
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = int(input("Enter Class Standing: "))
        major_exam = int(input("Enter Major Exam Grade: "))
        student_records.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("=====================================")
        print("Record added.")
        
    elif choice == "7":  # Edit Record
        student_id = int(input("Enter Student ID to edit: "))
        found = False
        for i in range(len(student_records)):
            if student_records[i][0] == student_id:
                first_name = input("Enter new First Name: ")
                last_name = input("Enter new Last Name: ")
                class_standing = int(input("Enter new Class Standing: "))
                major_exam = int(input("Enter new Major Exam Grade: "))
                student_records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
                print("=====================================")
                print("Record updated.")
                found = True
                break
        if not found:
            print("=====================================")
            print("Student not found.")

    elif choice == "8":  # Delete Record
        student_id = int(input("Enter Student ID to delete: "))
        found = False
        for i in range(len(student_records)):
            if student_records[i][0] == student_id:
                del student_records[i]
                print("=====================================")
                print("Record deleted.")
                found = True
                break
        if not found:
            print("=====================================")
            print("Student not found.")

    elif choice == "9":  # Exit
        print("=====================================")
        print("Exiting...")
        break

    elif choice == "1" or choice == "2" or choice == "3":
        print("=====================================")
        print("Functionality not yet implemented")

    else:
        print("=====================================")
        print("Invalid choice.")
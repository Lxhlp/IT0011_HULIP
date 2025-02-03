
fname = input("Enter last name: ")
lname = input("Enter first name: ")
age = input("Enter age: ")
contactNum = input("Enter contact number: ")
course = input("Enter course: ")

information = ["**************************************\n", 
               "Reading Student Information\n", 
               "**************************************\n",
               "Last Name: " + lname + "\n", "First Name: " + fname + "\n",
               "Age: " + age + "\n",
               "Contact Number: " + contactNum + "\n", "Course: " + course + "\n"]
fileObj = open("students.txt", "a")
fileObj.writelines(information)
fileObj.close()

print("Student information has been saved to 'students.txt'.")
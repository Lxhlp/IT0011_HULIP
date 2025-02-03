fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
fullName = fname + " " + lname
nameSize = len(fullName)

print("Full Name: " + fullName)
print("Full Name (Upper Case): " + fullName.upper())
print("Full Name (Lower Case): " + fullName.lower())
print("Length of Full Name: " + str(nameSize))

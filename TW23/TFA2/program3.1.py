fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

fullName = fname + " " + lname
sliceName = fullName

print()
print("Full Name: " + fullName)
shortName = fullName[0:3]
print("Sliced Name: " + shortName)
print("Greeting Message: Hello, " + shortName + "! Welcome. You are " + age + " years old.")
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")

fullName = fname + " " + lname
sliceName = fullName
greetings = "Greeting Message: Hello, {}! Welcome. You are {} years old."

print()
print("Full Name: " + fullName)
shortName = fullName[0:3]
print("Sliced Name: " + shortName)
print(greetings.format(shortName, age))
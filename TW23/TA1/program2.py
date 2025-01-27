string_input = input("Enter a string with numbers: ")

#Initialize a variable to store the sum of digits
total = 0

#Iterate through each character in the string
for char in string_input:
    if char.isdigit():  #Check if the character is a digit
        total += int(char)  #Add the digit to the total

print(f"Sum of digits: {total}")
string_input = input("Enter a string: ")

vowels = 0
consonants = 0
spaces = 0
others = 0

#Convert the string to lowercase to handle both uppercase and lowercase letters
string_input = string_input.lower()

#Iterate through each character in the string
for char in string_input:
    if char in 'aeiou':
        vowels += 1
    elif char in 'bcdfghjklmnpqrstvwxyz':
        consonants += 1
    elif char == ' ':
        spaces += 1
    else:
        others += 1
        
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Spaces: {spaces}")
print(f"Other characters: {others}")
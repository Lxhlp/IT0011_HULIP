def divide(a, b):
    if b == 0:
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return None
    return a % b

def summation(a, b):
    if b <= a:
        return None
    return sum(range(int(a), int(b) + 1))

def display_menu():
    print("==========================")
    print("MATHEMATICAL OPERATIONS")
    print("==========================")
    print("[D] - Divide")
    print("[E] - Exponentiation")
    print("[R] - Remainder")
    print("[F] - Summation")
    print("[Q] - Quit")

def get_input(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        return None

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip().upper()

        if choice == 'Q':
            print("===============================")
            print("Exiting the program. Goodbye!")
            print("===============================")
            break

        if choice not in ['D', 'E', 'R', 'F']:
            print("*****Invalid choice. Please try again.*****")
            continue

        num1 = get_input("Enter the first number: ")
        num2 = get_input("Enter the second number: ")

        if num1 is None or num2 is None:
            print("*****Invalid input. Please enter numeric values.*****")
            continue

        if choice == 'D':
            result = divide(num1, num2)
            if result is None:
                print("=======================================")
                print("Error: Division by zero is not allowed.")
                print("=======================================")
            else:
                print(f"The result of division is: {result}")

        elif choice == 'E':
            result = exponentiation(num1, num2)
            print(f"The result of exponentiation is: {result}")

        elif choice == 'R':
            result = remainder(num1, num2)
            if result is None:
                print("=======================================")
                print("Error: Division by zero is not allowed.")
                print("=======================================")
            else:
                print(f"The remainder is: {result}")

        elif choice == 'F':
            result = summation(num1, num2)
            if result is None:
                print("===============================================================")
                print("Error: The second number must be greater than the first number.")
                print("===============================================================")
            else:
                print(f"The summation is: {result}")
                
main()
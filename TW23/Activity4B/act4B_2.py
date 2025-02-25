currency_file_path = 'C:\\Users\\Alessandra Lei\\OneDrive - feutech.edu.ph\\Documents\\GitHub\\IT0011_HULIP\\TW23\\Activity4B\\currency.csv'
currency_dict = {}

#Popuplate the dictionary with the currency code and exchange rate
with open(currency_file_path, 'r', encoding='ISO-8859-1') as file:
    next(file)  
    for line in file:
        columns = line.strip().split(',')
        currency_code = columns[0].strip()
        exchange_rate = float(columns[2].strip())
        currency_dict[currency_code] = exchange_rate

while True:
    print("------------------------------------------------------------")
    dollar_amount = float(input("How much dollar do you have?: "))
    currency_to_convert = input("What currency do you want to have?: ").upper()

    #Check if currency code exists in the dictionary
    if currency_to_convert in currency_dict:
        exchange_rate = currency_dict[currency_to_convert]
        converted_amount = dollar_amount * exchange_rate
        print("------------------------------------------------------------")
        print(f"Dollar: {dollar_amount} USD")
        print(f"{currency_to_convert}: {converted_amount:.2f}")
        print("------------------------------------------------------------")
    else:
        print("------------------------------------------------------------")
        print(f"Sorry, the currency {currency_to_convert} is not available.")
        print("------------------------------------------------------------")

    again = input("Do you want to convert again? (yes/no): ").strip().lower()
    if again != 'yes':
        print("------------------------------------------------------------")
        print("Thank you for using the currency converter!")
        print("------------------------------------------------------------")
        break

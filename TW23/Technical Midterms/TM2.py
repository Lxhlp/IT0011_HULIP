months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

date_input = input("Enter the date (mm/dd/yyyy): ")
month_str, day_str, year_str = date_input.split('/')

month = int(month_str)
day = int(day_str)
year = int(year_str)

month_name = months[month - 1] 
day_formatted = str(day).lstrip('0') 

formatted_date = f"{month_name} {day_formatted}, {year}"
print(f"Date Output: {formatted_date}")

import os
class Item:
    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        print("================================================")
        return f"ID: {self.id} \nName: {self.name} \nDescription: {self.description} \nPrice: {self.price} \n"

FILE_NAME = "TW23\\Activity 6\\items.txt"

# Save items to file
def save_items(items):
    with open(FILE_NAME, "w") as file:
        for item in items:
            file.write(f"{item.id},{item.name},{item.description},{item.price}\n")

# Load items from file
def load_items():
    items = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                id, name, description, price = line.strip().split(",")
                items.append(Item(int(id), name, description, float(price)))
    return items

# Menu 
def display_menu():
    print("================================================")
    print("\t   Item Management Application")
    print("================================================")
    print("[1] Create Item")
    print("[2] Show All Items")
    print("[3] Show Item by ID")
    print("[4] Update Item")
    print("[5] Delete Item")
    print("[6] Exit")

# Create a new item
def create_item(items):
    try:
        id = int(input("Enter ID: "))
        # Check if ID already exists
        if any(item.id == id for item in items):
            print("================================================")
            print("Error: ID already exists.")
            return
        name = input("Enter Name: ")
        description = input("Enter Description: ")
        price = float(input("Enter Price: "))
        items.append(Item(id, name, description, price))
        save_items(items)
        print("================================================")
        print("Item created successfully.")
    except ValueError:
        print("================================================")
        print("Error: Invalid input. Please enter valid data.")

# Show all items
def show_all_items(items):
    if not items:
        print("================================================")
        print("No items found.")
    else:
        print("================================================")
        print("\t\t   All Items")
        for item in items:
            print(item)

# Show item by ID
def show_item_by_id(items):
    try:
        id = int(input("Enter ID of the item to show: "))
        item = next((item for item in items if item.id == id), None)
        if item:
            print("================================================")
            print("\t\t  Item Details")
            print(item)
        else:
            print("================================================")
            print("Error: Item not found.")
    except ValueError:
        print("================================================")
        print("Error: Invalid input. Please enter a valid ID.")

# Update an item
def update_item(items):
    try:
        id = int(input("Enter ID of the item to update: "))
        item = next((item for item in items if item.id == id), None)
        if item:
            print("================================================")
            print("\t   Leave blank to keep current")
            print("================================================")
            name = input("Enter new Name: ")
            description = input("Enter new Description: ")
            price = input("Enter new Price: ")
            if name:
                item.name = name
            if description:
                item.description = description
            if price:
                item.price = float(price)
            save_items(items)
            print("================================================")
            print("Item updated successfully.")
        else:
            print("================================================")
            print("Error: Item not found.")
    except ValueError:
        print("================================================")
        print("Error: Invalid input. Please enter valid data.")

# Delete an item
def delete_item(items):
    try:
        id = int(input("Enter ID of the item to delete: "))
        item = next((item for item in items if item.id == id), None)
        if item:
            items.remove(item)
            save_items(items)
            print("================================================")
            print("Item deleted successfully.")
        else:
            print("================================================")
            print("Error: Item not found.")
    except ValueError:
        print("================================================")
        print("Error: Invalid input. Please enter valid data.")

# Main function
def main():
    items = load_items()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            create_item(items)
        elif choice == "2":
            show_all_items(items)
        elif choice == "3":
            show_item_by_id(items)
        elif choice == "4":
            update_item(items)
        elif choice == "5":
            delete_item(items)
        elif choice == "6":
            print("================================================")
            print("\tExiting the application. Goodbye!")
            print("================================================")
            break
        else:
            print("================================================")
            print("Invalid choice. Please try again.")

# Run program
if __name__ == "__main__":
    main()
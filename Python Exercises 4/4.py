myset = set()

def display_items():
    print("Items in the set:", myset)

def clear():
    myset.clear()
    print("Set cleared.")

def add_item():
    item = input("Enter an item to add: ")
    myset.add(item)
    print(f"{item} added to the set.")

def remove_item():
    item = input("Enter an item to remove: ")
    if item in myset:
        myset.remove(item)
        print(f"{item} removed from the set.")
    else:
        print(f"{item} is not in the set.")

def pop_item():
    if myset:
        item = myset.pop()
        print(f"Popped item: {item}")
    else:
        print("Set is empty, nothing to pop.")

def check_item_exists():
    item = input("Enter an item to check: ")
    if item in myset:
        print(f"{item} exists in the set.")
    else:
        print(f"{item} does not exist in the set.")

def add_fruits():
    fruits = {"apple", "banana", "cherry", "lemon"}
    myset.update(fruits)
    print("Fruits added to the set.")

def subtract_big_techs():
    big_techs = {"google", "amazon", "apple", "microsoft"}
    myset.difference_update(big_techs)
    print("Big tech companies subtracted from the set.")

def display_items_in_caps():
    items_in_caps = {item.upper() for item in myset}
    print("Items in capital letters:", items_in_caps)

while True:
    print("\nMenu:")
    print("1. Display all items")
    print("2. Clear")
    print("3. Add an item")
    print("4. Remove an item")
    print("5. Pop an item")
    print("6. Check if an item exists")
    print("7. Add some fruits")
    print("8. Subtract some big-techs")
    print("9. Display all items in capital letters")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")
    
    if choice == '1':
        display_items()
    elif choice == '2':
        clear()
    elif choice == '3':
        add_item()
    elif choice == '4':
        remove_item()
    elif choice == '5':
        pop_item()
    elif choice == '6':
        check_item_exists()
    elif choice == '7':
        add_fruits()
    elif choice == '8':
        subtract_big_techs()
    elif choice == '9':
        display_items_in_caps()
    elif choice == '10':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")

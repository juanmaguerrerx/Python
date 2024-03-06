mydic = {}

def display_dictionary():
    print("Dictionary contents:")
    for key, value in mydic.items():
        print(f"{key}: {value}")

def add_key_value_pair():
    key = input("Enter a key: ")
    value = input("Enter a value: ")
    mydic[key] = value
    print(f"Key-Value pair added: {key}: {value}")

def remove_key():
    key = input("Enter a key to remove: ")
    if key in mydic:
        del mydic[key]
        print(f"Key {key} removed from the dictionary.")
    else:
        print(f"Key {key} does not exist in the dictionary.")

def lookup_value():
    key = input("Enter a key to lookup: ")
    if key in mydic:
        print(f"Value for key {key}: {mydic[key]}")
    else:
        print(f"Key {key} does not exist in the dictionary.")

def modify_value():
    key = input("Enter a key to modify its value: ")
    if key in mydic:
        new_value = input("Enter the new value: ")
        mydic[key] = new_value
        print(f"Value for key {key} updated to {new_value}.")
    else:
        print(f"Key {key} does not exist in the dictionary.")

def clear_dictionary():
    mydic.clear()
    print("Dictionary cleared.")

while True:
    print("\nMenu:")
    print("1. Display Dictionary")
    print("2. Add Key-Value Pair")
    print("3. Remove Key")
    print("4. Lookup Value")
    print("5. Modify Value")
    print("6. Clear Dictionary")
    print("7. ...")
    print("8. ...")
    print("9. ...")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")

    if choice == '1':
        display_dictionary()
    elif choice == '2':
        add_key_value_pair()
    elif choice == '3':
        remove_key()
    elif choice == '4':
        lookup_value()
    elif choice == '5':
        modify_value()
    elif choice == '6':
        clear_dictionary()
    elif choice == '10':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter Item to add to the shopping list: ").strip().title()
            shopping_list.append(item)
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter Item to remove from the shopping list: ").strip().title()
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print(f"{item} is not in your shopping list")
            pass
        elif choice == '3':
            # Display the shopping list
            for item in shopping_list:
                print(item)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
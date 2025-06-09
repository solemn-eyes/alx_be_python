def display_menu():
    print("Shopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"✅ '{item}' has been added to the shopping list.")
        elif choice == '2':
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"❌ '{item}' has been removed from the shopping list.")
            else:
                print(f"⚠️ '{item}' is not in the shopping list.")
        elif choice == '3':
            if shopping_list:
                print("\n🛒 Your Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == '4':
            print("👋 Exiting. Happy shopping!")
            break
        else:
            print("❗ Invalid choice. Please enter a number between 1 and 4.")
if __name__ == "__main__":
    main()
# This code implements a simple shopping list manager that allows users to add, remove, and view items in their shopping list.

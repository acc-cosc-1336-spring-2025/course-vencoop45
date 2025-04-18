import dictionary

def main():
    inventory_dictionary = {}

    while True:
        print("\nInventory Menu")
        print("1 - Add or Update Item")
        print("2 - Delete Item")
        print("3 - Exit")

        choice = input("Please Enter Selection:")

        if choice == '1':
            while True:
                widget_name = input("Please Enter Widget Name:")
                quantity = int(input("Please Enter Quantity:"))
                dictionary.add_inventory(widgets, widget_name, quantity)
                print(f"Updated Inventory: {inventory_dictionary}")

        elif choice == '2':
            while True:
                widget_name = input("Please Enter Name of Widget to Delete:")
                result = dictionary.remove_inventory_widget(widgets, widget_name)
                print(result)
        
        elif choice == '3':
            print("Program Closing")
            break

        else:
            print("Invalid Selection. Choose a Number 1-3.")

if __name__ == "__main__":
    main()
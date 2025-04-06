import lists
from lists import get_lowest_list_value, get_highest_list_value

def main():
    while True:
        print("\nMenu:")
        print("1 - Show the list's low and high values")
        print("2 - Exit")

        choice = input("Enter your choice:")

        if choice == '1':
            numbers = []
            while True:
                try:
                    num = int(input("Enter a list value:"))
                    numbers.append(num)

                    if len(numbers) >= 3:
                        add = input("Would you like to enter another value? (Yes/No):")
                        if add.lower() != "Yes":
                            break
                
                except ValueError:
                    print("Please enter a valid number")

            if numbers:
                lowest = lists.get_lowest_list_value(numbers)
                highest = lists.get_highest_list_value(numbers)
                print(f"The lowest value in the list is: {lowest}")
                print(f"The highest value in the list is: {highest}")
        
        elif choice == '2':
            print("Exiting the program")
            break
        
        else:
            print("Please make a valid choice")

if __name__ == "__main__":
    main()            
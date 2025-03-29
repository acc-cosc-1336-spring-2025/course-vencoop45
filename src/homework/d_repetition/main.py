import repetition

def main():
    while True:
        print("\nHomework 3 Menu:")
        print("1 - Calculate Factorial")
        print("2 - Sum Odd Numbers")
        print("3 - Exit")

        choice = input("Please enter choice (1-3):")

        if choice == '1':
            while True:
                try:
                    num_str = input("Please enter a number greater than 0 and less than 10:")
                    num = int(num_str)
                    if 0 < num < 10:
                        factorial_result = repetition.get_factorial(num)
                        print(f"The factorial of {num} is: {factorial_result}")
                        break
                    print("Invalid input. Please try again.")

        elif choice == '2':
            while True:
                try:
                    num_str = input("Please enter a number greater than 0 and less than 100:")
                    num = int(num_str)
                    if 0 < num < 100:
                        sum_odd = repetition.sum_odd_numbers(num)
                        print(f"The sum of odd numbers up to {num} is: {sum_odd}")
                        break
                    print("Invalid input. Please try again.")
        
        elif choice == '3':
            verify = input("Please verify you would like to exit. (yes/no):").lower()
            if verify == 'yes':
                break

if __name__ == "__main__":
    main()
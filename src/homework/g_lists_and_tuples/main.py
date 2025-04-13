import lists
from lists import get_lowest_list_value, get_highest_list_value
from tuples import get_p_distance, get_p_distance_matrix

def main():
    while True:
        print("\nMenu:")
        print("1 - Get p distance matrix")
        print("2 - Exit")

        choice = input("Enter your choice:")

        if choice == '1':
            dna_strings_raw = input("Enter a list of lists (e.g., [['T','T','A'], ['G','C','A']]):")
            try:
                dna_lists = eval(dna_strings_raw)
                if dna_lists:
                    first_length = len(dna_lists) if dna_lists else 0
                    for dna_list in dna_lists:
                        if len(dna_list) != first_length:
                            print("Error: all inner lists must have equal length")
                            break
                    else:
                        print("\nP-distance Matrix:")
                        matrix = get_p_distance_matrix(dna_lists)
                        for row in matrix:
                            print(*(f'{val:.5f}' for val in row))
                else:
                    print("No list entered.")
            except Exception as e:
                print(f"Error processing input: {e}")
        
        elif choice == '2':
            print("Exiting the program")
            break

        else: 
            print("Please make a valid choice")

if __name__ == "__main__":
    main()            
from strings import get_hamming_distance, get_dna_complement

def main():
    while True:
        print("\n**DNA String Operations Menu**")
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - Exit")

        choice = input("Please enter your selection:")

        if choice == '1':
            dna1 = input("Please enter the first DNA string:")
            dna2 = input("Please enter the second DNA string:")
            if len(dna1) == len(dna2):
                distance = get_hamming_distance(dna1,dna2)
                print(f"The Hamming distance between '{dna1}' and '{dna2}' is: {distance}")
            else:
                print("Error: Input strings must have equal length to calculate Hamming distance.")
        elif choice == '2':
            dna = input("Enter a DNA string:")
            complement = get_dna_complement(dna)
            print(f"The DNA complement of '{dna}' is: {complement}")
        elif choice == '3':
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
    if __name__ == "__main__":
        main()
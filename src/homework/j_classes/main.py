from class_a import Die

def main():
    keep_rolling = 'y'

    while keep_rolling.lower() == 'y':
        my_die = Die()
        my_die.roll()
        print(my_die)

        keep_rolling = input('Do you want to roll again? y/n:')
    print('Exiting the die rolling program.')

if __name__ == '__main__':
    main()
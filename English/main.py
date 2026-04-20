import os
import sys
from time import sleep
# Import the programs
import Guess_the_number
import Hangman
import Random_Password
import Rock_Paper_Scissors
import To_Do_List
import Encoder_Decoder
from To_Do_List import ExitToMainException



# Clear the console screen
def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


def main():

    clear()
    sleep(1)
    while True:
        clear()
        sleep(1)
        # List all the programs
        print("1. Guess The Number")
        print("2. Hangman Game")
        print("3. Random Password")
        print("4. Rock Paper Scissors")
        print("5. To-Do List")
        print("6. Encoder / Decoder")
        print("0. Exit")

        try:
            # The user chooses which program to run
            choice = int(input("\nEnter your choice : "))
            if choice == 1:
                Guess_the_number.run_program1()
            elif choice == 2:
                Hangman.run_program2()
            elif choice == 3:
                Random_Password.run_program3()
            elif choice == 4:
                Rock_Paper_Scissors.run_program4()
            elif choice == 5:
                try:
                    To_Do_List.run_program5()
                except ExitToMainException:
                    continue
            elif choice == 6:
                Encoder_Decoder.run_program6()
            elif choice == 0:
                print("\nExiting...")
                sleep(2)
                sys.exit()

            else:
                print("Please choose an existing program.")
                sleep(2)
                clear()
        # Handle value error
        except ValueError:
            print("Please use an integer.")
            sleep(2)
            clear()


# Run the program
if __name__ == '__main__':
    clear()
    main()

import os
import sys
from time import sleep
# Import the programs
import Guess_the_number
import Hangman_Game
import random_password
import rock_paper_scissors
import To_Do_List
import encoder_decoder
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
                Hangman_Game.run_program2()
            elif choice == 3:
                random_password.run_program3()
            elif choice == 4:
                rock_paper_scissors.run_program4()
            elif choice == 5:
                try:
                    To_Do_List.run_program5()
                except ExitToMainException:
                    continue
            elif choice == 6:
                encoder_decoder.run_program6()
            elif choice == 0:
                print("Exiting...")
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

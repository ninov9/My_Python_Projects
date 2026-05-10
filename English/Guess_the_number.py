"""
A simple number guessing game where you try to guess a randomly chosen number between 1 and 10.
"""

def run_program1():
    """
    Runs the guessing game.
    """

    import random
    from time import sleep
    import os


    def clear():
        """
        Clears the console screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')


    clear()

    def play_game():
        """
        Plays the number guessing game.
        """
        num = random.randint(1, 10)
        print ("A number between 1 and 10 has been chosen.")
        sleep(2)
        clear()
        while True:
            try:
                guess = int(input("Take a guess : "))
            except ValueError:
                print ("Please type a number !")
                sleep(2)
                clear()
            else:
                # Check if guess is out of range
                if guess < 1 or guess > 10:
                    print("Please choose a number between 1 and 10 !")
                    sleep(2)
                    clear()
                elif guess < num:
                    print ("The number to guess is higher.")
                    sleep(1.5)
                    clear()
                elif guess > num:
                    print ("The number to guess is lower.")
                    sleep(1.5)
                    clear()
                else:
                    print("Congratulations ! You found the right answer !")
                    sleep(1)
                    break


    play_game()
    input("\nPress Enter to continue...")
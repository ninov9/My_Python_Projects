def run_program1():

    import random
    from time import sleep
    import os


    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


    clear()

    def play_game():
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
                if 1 < guess > 10:
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
import random

def play_game():
    num = random.randint(1, 10)
    print ("A number between 1 and 10 has been chosen.")
    
    while True:
        guess = int(input("Take a guess : "))
        if 1 < guess > 10:
            print("Please choose a number between 1 and 10 !")
        elif guess < num:
            print ("The number to guess is higher.")
        elif guess > num:
            print ("The number to guess is lower.")
        else:
            print("Congratulations ! You found the right answer !")
            break

play_game()
input("\nPress Enter to continue...")
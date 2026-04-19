# HANGMAN HAME
def run_program2():

    import os
    import time

    
    #CLEAR

    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")


    def write(sentence):
        for char in sentence:
            print(char, end='', flush=True)
            time.sleep(0.01)


    # Default Settings

    right_guess = 0
    fault = 0
    word = " "
    clear()
    time.sleep(0.5)


    # Check Faults

    def hangman_check():
        if fault == 0:
            print("   |‾‾‾‾‾‾‾‾")
            print("   |        ")
            print("   |        ")
            print("   |        ")
            print("   |        ")
            print(" ------")
        if fault == 1:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print(" ------")
        if fault == 2:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print(" ------")
        if fault == 3:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |        |")
            print("   |         ")
            print("   |         ")
            print(" ------")
        if fault == 4:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |       /|")
            print("   |         ")
            print("   |         ")
            print(" ------")
        if fault == 5:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |       /|\\")
            print("   |         ")
            print("   |         ")
            print(" ------")
        if fault == 6:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |       /|\\")
            print("   |       / ")
            print("   |         ")
            print(" ------")
        if fault == 7:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |       /|\\")
            print("   |       / \\")
            print("   |         ")
            print(" ------")


    # Tutorial and Rules

    def tutorial():
        clear()
        write("Welcome to the hangman Game.")
        time.sleep(2)
        write("\nHere are the rules of the game : ")
        time.sleep(2)
        write("\nThis game requires 2 Players. One chooses a word and the other one must guess the word by suggesting letters.")
        time.sleep(6)
        write("\nThe player who must guess the word is only allowed 7 faults.")
        time.sleep(4)
        write("\nGood luck !")
        time.sleep(2)
        clear()


    # Tutorial ?

    while True:
        tuto = int(input("Wanna see the rules and tutorial ?    (YES = 1  |  NO = 2)   "))
        if tuto == 1:
           tutorial()
           break
        elif tuto == 2:
            break
        else:
            write("Choisi entre 1 et 2 !")
            time.sleep(1)
            clear()


    # Victory

    def win():
        clear()
        time.sleep(0.5)
        hangman_check()
        write("You won !")
        time.sleep(1)
        write("\nYou guessed the word '{}'".format(word))
        time.sleep(4)
        input("\nPress Enter to continue...")
        return


    # Defeat

    def defeat():
        clear()
        time.sleep(0.5)
        hangman_check()
        time.sleep(1.5)
        write("You lost.")
        time.sleep(1)
        write("\nThe word was '{}' .".format(word))
        time.sleep(4)
        input("\nPress Enter to continue...")
        return
        

    # Word Choice

    clear()
    while True:
        word = input("Player 1 chooses a word :  ")
        time.sleep(0.1)
        if word.isalpha():
            clear()
            write("You word is valid.")
            time.sleep(2)
            clear()
            time.sleep(1)
            break
        else:
            write("You can't type digits, only letters !")
            time.sleep(1.5)
            clear()
            time.sleep(1)


    # Game Start

    word = word.lower()
    word_set = set(word)
    hidden_word = ["_"] * len(word)
    hangman_check()
    time.sleep(2)
    clear()


    # Game :

    # Proposition Letter

    while fault != 7:
        write(" ".join(hidden_word))
        letter = input("\nSuggest a letter : ").lower()

        if letter in word_set:

    # Letter is in the word

            write("\nThe letter '{}' is in the word.".format(letter))
            for i, char in enumerate(word):
                if char == letter:
                    hidden_word[i] = letter
                    right_guess += 1
                    time.sleep(2)
            if right_guess == len(word_set):
                win()
                break
            
            clear()

    # Letter is NOT in the word

        else:
            fault += 1
            write("\nThe letter '{}' is not in the word.".format(letter))
            time.sleep(2)
            clear()
            hangman_check()
            time.sleep(2)
            clear()
            if fault == 7:
                defeat()

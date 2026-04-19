def run_program2():

    import os
    from time import sleep

    
    # Clear the console

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


    # Dialog box with a more fluid display

    def write(sentence):
        for char in sentence:
            print(char, end='', flush=True)
            sleep(0.01)


    wrong_guesses = 0

    # Check the number of wrong guesses

    def hangman():
        clear()
        if wrong_guesses == 0:
            print("   |‾‾‾‾‾‾‾‾")
            print("   |        ")
            print("   |        ")
            print("   |        ")
            print("   |        ")
            print(" ------")
            print("\n\nWrong guesses: {}".format(wrong_guesses))
        elif wrong_guesses == 1:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print(" ------")
            print("\n\nWrong guesses: {}".format(wrong_guesses))
        elif wrong_guesses == 2:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |         ")
            print("   |         ")
            print("   |         ")
            print(" ------")
            print("\n\nWrong guesses: {}".format(wrong_guesses))
        elif wrong_guesses == 3:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |        |")
            print("   |         ")
            print("   |         ")
            print(" ------")
            print("\n\nWrong guesses: {}".format(wrong_guesses))
        elif wrong_guesses == 4:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |       /|")
            print("   |         ")
            print("   |         ")
            print(" ------")
            print("\n\nWrong guesses: {}".format(wrong_guesses))
        elif wrong_guesses == 5:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |       /|\\")
            print("   |         ")
            print("   |         ")
            print(" ------")
            print("\n\nWrong guesses: {}".format(wrong_guesses))
        elif wrong_guesses == 6:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |       /|\\")
            print("   |       / ")
            print("   |         ")
            print(" ------")
            print("\n\nWrong guesses: {}".format(wrong_guesses))
        elif wrong_guesses == 7:
            print("   |‾‾‾‾‾‾‾‾|")
            print("   |        O")
            print("   |       /|\\")
            print("   |       / \\")
            print("   |         ")
            print(" ------")
            print("\n\nWrong guesses: {}".format(wrong_guesses))


    # Victory

    def victory():
        hangman()
        write("\n\nYou won!")
        sleep(1)
        write("\n\nYou guessed the word '{}'.".format(word))
        sleep(1)
        input("\n\nPress Enter to go back to the main menu...")
        return


    # Defeat

    def defeat():
        hangman()
        write("\n\nYou lost!")
        sleep(1)
        write("\n\nThe word was '{}'.".format(word))
        sleep(1)
        input("\n\nPress Enter to go back to the main menu...")
        return
        

    # Word selection by player 1

    while True:
        clear()
        word = input("Player 1 chooses a word: ")
        if word.isalpha():
            clear()
            write("The word is valid.")
            sleep(1)
            break
        else:
            write("You cannot use numbers, only letters!")
            sleep(1.5)


    # Game setup
    word = word.lower()
    word_set = set(word)
    guessed_letters = set()
    hidden_word = ["_"] * len(word)
    hangman()
    sleep(2)
    clear()


    # Game loop:

    # The player suggests letters until they either guess the word or make 7 wrong guesses

    while wrong_guesses < 7:
        clear()
        write(" ".join(hidden_word))
        print("\n\nGuessed letters:", ", ".join(sorted(guessed_letters)))
        letter = input("\n\nGuess a letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            write("\nPlease enter a single letter.")
            sleep(1)
            continue

        if letter in guessed_letters:
            write("\nYou already guessed that letter.")
            sleep(1)
            continue

        guessed_letters.add(letter)

        if letter in word_set:

    # The letter is in the word

            write("\nThe letter '{}' is in the word.".format(letter))
            sleep(1.5)
            for i, char in enumerate(word):
                if char == letter:
                    hidden_word[i] = letter
            hangman()
            sleep(1.5)
            if "_" not in hidden_word:
                victory()
                break
            

    # The letter is not in the word

        else:
            wrong_guesses += 1
            write("\nThe letter '{}' is not in the word.".format(letter))
            sleep(1.5)
            hangman()
            sleep(1.5)
            if wrong_guesses == 7:
                defeat()

        
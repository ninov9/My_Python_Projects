def run_program4():

    import random
    import os
    from time import sleep
    
    
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    
    def write(sentence):
        for char in sentence:
            print(char, end='', flush=True)
            sleep(0.01)
    
    
    bot_score = 0
    player_score = 0
    clear()
    
    write("Welcome to Rock, Paper, Scissors !")
    sleep(2)
    while True:
        try:
            num_rounds = int(input("\n\nNumber of rounds : "))
        except ValueError:
            write("\nPlease enter a valid digit !")
            sleep(2)
            clear()
        else:
            if num_rounds < 1:
                write("\nPlease enter a number greater than 0 !")
                sleep(2)
                clear()
            elif num_rounds > 20:
                write("\nPlease enter a number lower than 20 !")
                sleep(2)
                clear()
            else:
                break
            
    clear()
    sleep(1)
    
    # Starting game
    
    for i in range(num_rounds):
        result = None
        player_choice = None
        bot_choice = None
    
    # Bot
    
        bot = random.randint(1, 3)
        if bot == 1:
            bot_choice = "Rock"
        elif bot == 2:
            bot_choice = "Paper"
        elif bot == 3:
            bot_choice = "Scissors"
    
    # Player
    
        while True:
            write(str("Rock = 1   Paper = 2  Scissors = 3"))
            sleep(1)
        
            try:
                player = int(input("\n\nChoice : "))
                if player in (1, 2, 3):
                    break
                else:
                    write("\nChoose a number between 1, 2, 3 !")
                    sleep(1.5)
                    clear()
            except ValueError:
                write("\nChoose a digit !")
                sleep(1.5)
                clear()
    
        if player == 1:
            player_choice = "Rock"
        elif player == 2:
            player_choice = "Paper"
        elif player == 3:
            player_choice = "Scissors"
        sleep(1)
        write("")
    
    # Tie
    
        if player == 1 and bot == 1:
            result = "\n\nTie"
        elif player == 2 and bot == 2:
            result = "\n\nTie"
        elif player == 3 and bot == 3:
            result = "\n\nTie"
    
    # Bot won
    
        elif bot == 1 and player == 3:
            result = "\n\nThe bot won the round."
        elif bot == 2 and player == 1:
            result = "\n\nThe bot won the round."
        elif bot == 3 and player == 2:
            result = "\n\nThe bot won the round."
        
    # Player won   
    
        elif player == 1 and bot == 3:
            result = "\n\nYou won the round."
        elif player == 2 and bot == 1:
            result = "\n\nYou won the round."
        elif player == 3 and bot == 2:
            result = "\n\nYou won the round."
        
    # Changing score
    
        if result == "\n\nYou won the round.":
            player_score += 1
        elif result == "\n\nThe bot won the round.":
            bot_score += 1
        else:
            pass
        
        
    # End of the round
    
        score = "\n\n" + str(player_score) + "  -  " + str(bot_score)
        write("\nThe bot chose : '{}' and you chose : '{}' ".format(bot_choice, player_choice))
        write("")
        sleep(2)
        write(result)
        sleep(2)
        write(score)
        sleep(2.5)
        clear()
        
    
    # End of the game
    
    sleep(1)
    write("Final Score: {} - {}".format(player_score, bot_score))
    sleep(1)
    if bot_score > player_score:
        write("\nThe bot won !")
    elif bot_score < player_score:
        write("\nYou won !")
    else:
        write("\nIt's a tie ! Nobody won.")
    sleep(3)
    print("\nPress Enter to continue...")
    
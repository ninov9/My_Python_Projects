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
    sleep(0.5)
    while True:
        try:
            num_rounds = int(input("\n\nNumber of rounds : "))
        except ValueError:
            write("\nPlease enter a valid integer !")
            sleep(1.5)
        else:
            if num_rounds < 1:
                write("\nPlease enter a number greater than 0.")
                sleep(1.5)
            elif num_rounds > 20:
                write("\nPlease enter a number lower than 20.")
                sleep(1.5)
            else:
                break
        clear()
            
    clear()
    
    # Starting game
    
    choices = ["Rock", "Paper", "Scissors"]

    for _ in range(num_rounds):

    # Bot

        bot = random.randint(1, 3)
        bot_choice = choices[bot - 1]
    
    # Player
    
        while True:
            write("Rock = 1 | Paper = 2 | Scissors = 3")
        
            try:
                player = int(input("\n\nChoice : "))
                if player in (1, 2, 3):
                    player_choice = choices[player - 1]
                    break
                else:
                    write("\nChoose a number between 1, 2, 3 !")
                    sleep(1.5)
            except ValueError:
                write("\nChoose a digit !")
                sleep(1.5)
            clear()

    
    # Determining the winner of the round

        if player == bot:
            result = "tie"
        elif (player - bot) % 3 == 1:
            result = "player"
        else:
            result = "bot"

    # Updating the score and preparing the message to display

        if result == "player":
            player_score += 1
            message = "\n\nYou won the round."
        elif result == "bot":
            bot_score += 1
            message = "\n\nThe bot won the round."
        else:
            message = "\n\nTie"
        
        
    # End of the round
    
        score = f"\n\nScore: {player_score} - {bot_score}"
        write(f"\nBot: {bot_choice} | You: {player_choice}")
        sleep(0.5)
        write(message)
        sleep(0.5)
        write(score)
        sleep(0.5)
        input("\n\nPress Enter to proceed...")
        clear()
        
    
    # End of the game
    
    write(f"Final Score: {player_score} - {bot_score}")
    sleep(0.5)
    if bot_score > player_score:
        write("\n\nThe bot won !")
    elif bot_score < player_score:
        write("\n\nYou won !")
    else:
        write("\n\nIt's a tie ! Nobody won.")
    sleep(1)

    input("\n\nPress Enter to go back to the main menu...")
    

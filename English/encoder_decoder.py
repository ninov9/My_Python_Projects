def run_program6():

    import os
    from time import sleep
    
    # List of all the characters
    char_list = [
                "a", "b", "c", "d", "e", "f", 
                "g", "h", "i", "j", "k", "l", 
                "m", "n", "o", "p", "q", "r", 
                "s", "t", "u", "v", "w", "x", 
                "y", "z", 
    
                 "é", "è", "ç", "ù", "à", 
    
                 "A", "B", "C", "D", "E", "F", 
                 "G", "H", "I", "J", "K", "L", 
                 "M", "N", "O", "P", "Q", "R", 
                 "S", "T", "U", "V", "W", "X", 
                 "Y", "Z", 
                 
                 " ", "!", "?", "#", "$", 
                 "%", "&", "'", "(", ")", 
                 "*", "+", ",", "-", ".", 
                 "/", ":", ";", "@", "=", 
    
                 "0", "1", "2", "3", "4", 
                 "5", "6", "7", "8", "9"
                 ]
    
    encoded_message = []
    decoded_message = []
    global choice
    choice = None
    
    
    # Clear the console screen
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    
    # Make a little animation for the user
    def animation():
        global choice
        if choice == 1:
        
            for i in range(5):
                print("Encoding")
                sleep(0.3)
                clear()
                print("Encoding.")
                sleep(0.3)
                clear()
                print("Encoding..")
                sleep(0.3)
                clear()
                print("Encoding...")
                sleep(0.3)
                clear()
            print("Encoding completed.")
            sleep(2)
            clear()
        elif choice == 2:
        
            for i in range(5):
                print("Decoding")
                sleep(0.3)
                clear()
                print("Decoding.")
                sleep(0.3)
                clear()
                print("Decoding..")
                sleep(0.3)
                clear()
                print("Decoding...")
                sleep(0.3)
                clear()
            print("Decoding completed.")
            sleep(2)
            clear()
    
    
    # Wait for the user to press Enter
    def wait_for_enter():
        try:
            input("\nPress Enter to continue...")
        except KeyboardInterrupt:
            print("\nExiting...")
            sleep(1)
            return
    
    
    # The user chooses between encoding or decoding
    def choose():
        clear()
        global choice
        sleep(0.5)
        while True:
            try:
                choice = int(input("Would you like to ENCODE ( 1 ) or DECODE ( 2 ) or EXIT ( 3 ): "))
            except ValueError:
                print("Please enter a number between 1 and 3.")
                sleep(2)
                clear()
            else:
                if choice == 1:
                    clear()
                    encode()
                    break
                elif choice == 2:
                    clear()
                    decode()
                    break
                elif choice == 3:
                    print("\nExiting...")
                    sleep(2)
                    break
                else:
                    print("Please enter a number between 1 and 3.")
                    sleep(2)
                    clear()
    
    
    # Encode the message
    def encode():
        global encoded_message
        encoded_message = []
        sleep(1)
        message = input("Enter the message to encode : ")
        sleep(0.1)
        clear()
        for char in message:
            current_index = char_list.index(char)
            new_index = current_index + 5
            new_char = char_list[new_index]
            encoded_message.append(new_char)
        
        sleep(0.1)
        clear()
        animation()
        print(f"The encoded message is :", "".join(encoded_message))
        sleep(1)
        wait_for_enter()
        choose()
    
    
    # Decode the encoded message
    def decode():
        global decoded_message
        decoded_message = []
        sleep(1)
        message = input("Enter the message to decode : ")
        sleep(0.1)
        clear()
        for char in message:
            current_index = char_list.index(char)
            new_index = current_index - 5
            new_char = char_list[new_index]
            decoded_message.append(new_char)
    
        sleep(0.1)
        clear()
        animation()
        print(f"The decoded message is :", "".join(decoded_message))
        sleep(4)
        wait_for_enter()
        choose()
    
    
    choose()
    
"""
A tool for encoding and decoding messages using Caesar, Vigenère, and reverse ciphers.
"""

def run_program6():
    """
    Runs the main encoder-decoder menu.
    """

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
    
    char_to_index = {char: i for i, char in enumerate(char_list)}
    
    def clear():
        """
        Clears the console screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    
    
    def wait_for_enter():
        """
        Waits for the user to press Enter.
        """
        try:
            input("\nPress Enter to continue...")
        except KeyboardInterrupt:
            print("\nExiting...")
            sleep(1)
            return
        

    def animation(direction):
        """
        Shows a fun encoding/decoding animation.
        """
        clear()

        if direction == 1:
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
            print("Encoding completed.\n")
            
        else:
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
            print("Decoding completed.\n")
        
        sleep(1.5)

    
    def value_shift(direction, mode_text, result_text):
        """
        Encodes or decodes using a fixed shift (Caesar cipher).
        """
        clear()
        new_message = []
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Please enter a valid integer for the shift value.")
            wait_for_enter()
            return
        shift = shift % len(char_list)
        
        message = input(f"\nEnter the message to {mode_text} : ")
        if not message:
            print("Message cannot be empty.")
            wait_for_enter()
            return

        for char in message:
            if char in char_to_index:
                current_index = char_to_index[char]

                # Calculate new index based on direction and shift
                if direction == 1:
                    new_index = (current_index + shift) % len(char_list)
                else:
                    new_index = (current_index - shift) % len(char_list)

                new_message.append(char_list[new_index])
            else:
                new_message.append(char)

        animation(direction)
        print(f"The {result_text} message is:", "".join(new_message))
        wait_for_enter()


    def key_shift(direction, mode_text, result_text):
        """
        Encodes or decodes using a key (Vigenère cipher).
        """
        clear()
        new_message = []
        key = input("Enter the key: ")
        if not key:
            print("Key cannot be empty.")
            wait_for_enter()
            return
        
        key_shifts = []
        for k in key:
            if k in char_to_index:
                key_shifts.append(char_to_index[k])
            else:
                key_shifts.append(0)

        if all(shift == 0 for shift in key_shifts):
            print("Key must contain at least one valid character.")
            wait_for_enter()
            return

        message = input(f"\nEnter the message to {mode_text} : ")
        if not message:
            print("Message cannot be empty.")
            wait_for_enter()
            return

        key_index = 0

        for char in message:
            if char in char_to_index:
                current_index = char_to_index[char]

                # Get shift from key, cycling through key shifts
                shift = key_shifts[key_index % len(key_shifts)]
                if direction == 1:
                    new_index = (current_index + shift) % len(char_list)
                else:
                    new_index = (current_index - shift) % len(char_list)

                new_message.append(char_list[new_index])
                key_index += 1
            else:
                new_message.append(char)

        animation(direction)
        print(f"The {result_text} message is:", "".join(new_message))
        wait_for_enter()
    

    def reverse(direction, mode_text, result_text):
        """
        Encodes or decodes by reversing the message.
        """
        clear()
        message = input(f"Enter the message to {mode_text}: ")
        if not message:
            print("Message cannot be empty.")
            wait_for_enter()
            return
        new_message = message[::-1]

        animation(direction)
        print(f"The {result_text} message is:", new_message)
        wait_for_enter()

    
    systems = {
    1: value_shift,
    2: key_shift,
    3: reverse
    }

    def choose_system(direction):
        """
        Lets the user pick a cipher method.
        """
        while True:
            clear()
            print("Choose the system you want to use :")
            print("1. Value shift (Caesar Cipher, simple and easy to use)")
            print("2. Key-based (Vigenère Cipher, more secure but requires a key)")
            print("3. Reverse (Reverse Cipher, very simple but not very secure)")
            print("4. Back to main menu")
            try:
                system_choice = int(input("\nEnter your choice: "))
            except ValueError:
                print("Please enter a number between 1 and 4.")
                sleep(1.5)
                continue

            mode_text = "encode" if direction == 1 else "decode"
            result_text = "encoded" if direction == 1 else "decoded"

            if system_choice in systems:
                systems[system_choice](direction, mode_text, result_text)
                break
            elif system_choice == 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
                sleep(1.5)

    while True:
        clear()
        try:
            direction = int(input("Would you like to ENCODE ( 1 ) or DECODE ( 2 ) or EXIT ( 3 ): "))
        except ValueError:
            print("Please enter a number between 1 and 3.")
            sleep(1.5)
            continue

        if 0 < direction < 3:
            choose_system(direction)
        elif direction == 3:
            print("\nExiting...")
            sleep(2)
            input("Press Enter to go back to the main menu...")
            break
        else:
            print("Please enter a number between 1 and 3.")
            sleep(1.5)
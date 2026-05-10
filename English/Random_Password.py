"""
A secure random password generator that creates passwords of user-specified lengths using a variety of characters.
"""

def run_program3():
    """
    Runs the password generator.
    """

    import secrets
    import os
    from time import sleep


    def clear():
        """
        Clears the console screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')


    # List of characters for password generation
    characters = [
                  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                  "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
                  "@", "_", "-", "*", "!", "?"
                  ]

    def generate(length):
        """
        Generates a random password of the given length.
        """
        password = []
        for _ in range(length):
            password.append(secrets.choice(characters))
        return "".join(password)


    # Handling user input for password length
    while True:
        clear()
        try:
            length = int(input("Length of the password : "))
        except ValueError:
            print("\nPlease enter a valid number.")
            sleep(1.5)
        else:
            if length <= 0:
                print("\nPlease choose a higher number.")
                sleep(1.5)
            elif length > 30:
                print("\nPlease choose a lower number.")
                sleep(1.5)
            else:
                print("\nGenerating password...")
                sleep(3)
                break


    password = generate(length)
    print(f"\nYour password is: {password}")
    print("\nYou can copy it now.")
    sleep(1)
    input("\n\nPress enter to continue...")

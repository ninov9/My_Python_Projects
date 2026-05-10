"""
A simple to-do list application that allows users to add, remove, edit, and manage tasks, with data saved to a JSON file.
"""

# TO-DO LIST

class ExitToMainException(Exception):
        pass


def run_program5():
    """
    Runs the to-do list application.
    """

    import os
    from time import sleep
    from colorama import Fore
    import json
    

    def write(sentence):
        """
        Displays text with a typing effect.
        """
        for char in sentence:
            print(char, end='', flush=True)
            sleep(0.01)

            
    def write_red(sentence):
        """
        Displays text in red.
        """
        write(Fore.RED + sentence + Fore.RESET)


# list_tasks.json stores the to-do list tasks as a JSON array
    def load_tasks():
        """
        Loads tasks from the JSON file.
        """
        try:
            with open("list_tasks.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            with open("list_tasks.json", "w") as file:
                json.dump([], file)
            return []
        except json.JSONDecodeError:
            write_red("Error decoding JSON file. The file might be corrupted.")
            sleep(1)
            input(Fore.CYAN + "Press Enter to continue..." + Fore.RESET)
            return []
    
    
    list_tasks = load_tasks()
    
    def save_tasks():
        """
        Saves tasks to the JSON file.
        """
        with open("list_tasks.json", "w") as file:
            json.dump(list_tasks, file)

    
    def clear():
        """
        Clears the console screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
    
    
    def write_green(sentence):
        """
        Displays text in green.
        """
        write(Fore.LIGHTGREEN_EX + sentence + Fore.RESET) 

    
    def display_list():
        """
        Displays the current list of tasks.
        """
        if not list_tasks:
            write_green("Your TO-DO List is empty.")
        else:
            write_green("You have " + Fore.LIGHTWHITE_EX + str(len(list_tasks)) + Fore.GREEN + " tasks to do:" + Fore.RESET)
            for i, task in enumerate(list_tasks, 1):
                write_green("\n\n{}. {}".format(i, task))


    def empty():
        """
        Clears all tasks from the list.
        """
        list_tasks.clear()
        write_green("\nThe list has been emptied successfully !\n")
        input(Fore.CYAN + "\n\nPress Enter to continue..." + Fore.RESET)
        save_tasks()
    
    
    def add_task():
        """
        Adds a new task to the list.
        """
        task_name = input(Fore.CYAN + "\n\nEnter the name of the task you want to add: " + Fore.RESET)
        list_tasks.append(task_name)
        write_green(f"\nTask '{task_name}' added successfully !\n")
        input(Fore.CYAN + "\n\nPress Enter to continue..." + Fore.RESET)
        save_tasks()
    
    
    def remove_task():
        """
        Removes a task from the list.
        """
        while True:
            try:
                index_task = int(input(Fore.CYAN + "\n\nNumber of the task you want to remove: " + Fore.RESET))
                if 1 <= index_task <= len(list_tasks):
                    break
                else:
                    write_red("\nChoose an existing task!")
            except ValueError:
                write_red("\nPlease enter a valid digit!")
            sleep(1.5)
            clear()
            display_list()
        write_green(f"\nTask '{list_tasks[index_task - 1]}' removed successfully !\n")
        list_tasks.pop(index_task - 1)
        input(Fore.CYAN + "\n\nPress Enter to continue..." + Fore.RESET)
        save_tasks()
    
    
    def edit_task():
        """
        Edits an existing task.
        """
        while True:
            try:
                index_task = int(input(Fore.CYAN + "\n\nNumber of the task you want to edit: " + Fore.RESET))
                if 1 <= index_task <= len(list_tasks):
                    break
                else:
                    write_red("\nChoose an existing task!")
            except ValueError:
                write_red("\nPlease enter a digit!")
            
            sleep(1.5)
            clear()
            display_list()

        list_tasks[index_task - 1] = input(Fore.CYAN + f"\nEnter the new name of the task N°{index_task}: " + Fore.RESET)
        write_green(f"\nTask N°{index_task} edited successfully!\n")
        input(Fore.CYAN + "\n\nPress Enter to continue..." + Fore.RESET)
        save_tasks()
    
    
    def help():
        """
        Displays the help menu.
        """
        clear()
        write_green("Here are all the available options : ")
        write_green("\n\n0 = HELP\n1 = ADD TASK\n2 = REMOVE TASK\n3 = EDIT TASK\n4 = EMPTY LIST\n5 = EXIT PROGRAM")
        input(Fore.CYAN + "\n\n\nPress Enter to continue..." + Fore.RESET)
    
    
    def exit_program():
        """
        Exits the program.
        """
        clear()
        write_green("Exiting...")
        sleep(1.5)
        raise ExitToMainException()
    
    
    # THE USER CHOOSES AN OPTION
    
    while True:
        clear()
        display_list()
        try:
            choice = int(input(Fore.CYAN + "\n\n\nChoose an option (0 for help) : " + Fore.RESET))
        except ValueError:
            write_red("\nPlease enter a valid digit !")
            sleep(1.5)
            continue
        if 0 <= choice <= 5:
            if choice == 0:
                help()
            elif choice == 1:
                add_task()
            elif choice == 2:
                if not list_tasks:
                    write_green("\nThe list is empty.")
                    sleep(2)
                else:
                    remove_task()
            elif choice == 3:
                if not list_tasks:
                    write_green("\nThe list is empty.")
                    sleep(2)
                else:
                    edit_task()
            elif choice == 4:
                empty()
            elif choice == 5:
                exit_program()
                break
        else:
            write_red("\nChoose a valid digit !")
            sleep(1.5)

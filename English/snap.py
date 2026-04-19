# SNAPSCORE BOT

# Requires scrcpy, an Android mobile, and a USB to USB type C cable OR a double USB type C cable.

try:
   from colorama import Fore
   import ctypes, pyautogui, keyboard, os, time, platform
   from datetime import datetime
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")


ascii_text = """
       ╭━━━╮
       ┃╭━╮┃
       ┃╰━━┳━╮╭━━┳━━┳━━┳━━┳━━┳━┳━━╮
       ╰━━╮┃╭╮┫╭╮┃╭╮┃━━┫╭━┫╭╮┃╭┫┃━┫
       ┃╰━╯┃┃┃┃╭╮┃╰╯┣━━┃╰━┫╰╯┃┃┃┃━┫
       ╰━━━┻╯╰┻╯╰┫╭━┻━━┻━━┻━━┻╯╰━━╯
                 ┃┃
                 ╰╯    """

global nb
nb = 0

def onLinux():
    if platform.system() == "Linux":
        return True
    else:
        return False

class snapchat:

    def __init__(self):
        self.sent_snaps = 0
        self.delay = 1.5    # <-------- Change the delay corresponding to your needs 

    def get_positions(self):
        self.print_console("Go to the person you want to send and move your mouse to the picture button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.click_on_camera = pyautogui.position()
                break
        time.sleep(0.5)

        self.print_console("Move your mouse to take a picture, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.take_picture = pyautogui.position()
                break
        time.sleep(0.5)
        
        self.print_console("Move your mouse to the Send To button, then press F")
        while True:
            if keyboard.is_pressed("f"):
                self.send_to = pyautogui.position()
                break
        time.sleep(0.5)

    
    def send_snap(self, shortcut_users):
        global nb
        pyautogui.moveTo(self.click_on_camera)         # Click on camera
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.take_picture)             # Take a picture
        pyautogui.click()
        time.sleep(self.delay)
        pyautogui.moveTo(self.send_to)                  # Send the snap
        pyautogui.click()
        time.sleep(self.delay)
        nb += 1
        self.update_title(shortcut_users)

    
    def update_title(self, shortcut_users):
        global nb
        now = time.time()
        elapsed = str(now - self.started_time).split(".")[0]
        sent_snaps = self.sent_snaps * shortcut_users
        if onLinux() == False:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Snapchat Score Botter | Sent Snaps: {sent_snaps} | Elapsed: {elapsed}s | Developed by @useragents on Github")
        print(f"\r       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Sent snaps : {Fore.GREEN}{nb}{Fore.WHITE}.", end='', flush=True)

    def print_console(self, arg, status = "Console"):
        print(f"\n       {Fore.WHITE}[{Fore.RED}{status}{Fore.WHITE}] {arg}")
    
    def main(self):
        if onLinux() == False:
            os.system("cls")
            ctypes.windll.kernel32.SetConsoleTitleW("Snapchat Score Botter | Developed by @useragents on Github")
        else:
            os.system("clear")

        print(Fore.RED + ascii_text)

        self.get_positions()

        while True:
            try:
                shortcut_users = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] How many people are in this shortcut: "))
                break
            except ValueError:
                print(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] There was an error with that input, please try again :) ")

        self.print_console("Slow PC", "1")
        self.print_console("Fast PC", "2")
        options = int(input(f"\n       {Fore.WHITE}[{Fore.RED}Console{Fore.WHITE}] Option: "))
        if options == 1:
            self.delay = 1.5
        self.print_console("Go to the the person you want to send snaps, then press F when you're ready.")
         
        while True:
            if keyboard.is_pressed("f"):
                break
        if onLinux() == False:
            os.system("cls")
        else:
            os.system("clear")
        print(Fore.RED + ascii_text)
        self.print_console("DO NOT TOUCH THE COMPUTER !\n")
        time.sleep(0.1)
        self.started_time = time.time()
        while True:
            if keyboard.is_pressed("F4"):
                break
            self.send_snap(shortcut_users)
        self.print_console(f"Finished sending {nb} snaps.")

obj = snapchat()
obj.main()

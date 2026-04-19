from time import sleep


sleep(1)

def write(sentence):
    for char in sentence:
        print(char, end='', flush=True)
        sleep(0.01)


write("This program prints the characters one by one to make it better looking.")

sleep(2)

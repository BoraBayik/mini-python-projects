import random

def printRock():
    print('''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    \n''')

def printPaper():
    print('''
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    \n''')


def printScissor():
    print('''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    \n''')


print('''
█▀█ █▀█ █▀▀ █▄▀  
█▀▄ █▄█ █▄▄ █░█  

█▀█ ▄▀█ █▀█ █▀▀ █▀█  
█▀▀ █▀█ █▀▀ ██▄ █▀▄  

█▀ █▀▀ █ █▀ █▀ █▀█ █▀█ █▀
▄█ █▄▄ █ ▄█ ▄█ █▄█ █▀▄ ▄█
''')
print("********** WELCOME **********\n")


counter = 1
computerWin = 0
youWin=0

while counter > 0:
    you = int(input("1 for Rock | 2 for Paper | 3 for Scissor | ELSE for Stop\n"))
    computer = random.randint(1, 3)

    ##I know this is not that optimal :))

    if you == 1 and computer == 1:
        print("YOU CHOSE ROCK\n")
        printRock()
        print("COMPUTER CHOSE ROCK\n")
        printRock()
        print("TIED, TRY AGAIN.\n")

    elif you == 1 and computer == 2:
        print("YOU CHOSE ROCK\n")
        printRock()
        print("COMPUTER CHOSE PAPER\n")
        printPaper()
        print("COMPUTER WIN  :((")
        computerWin+=1

    elif you == 1 and computer == 3:
        print("YOU CHOSE ROCK\n")
        printRock()
        print("COMPUTER CHOSE SCISSOR\n")
        printScissor()
        print("YOU WIN!! :))\n")
        youWin+=1

    elif you == 2 and computer == 1:
        print("YOU CHOSE PAPER\n")
        printPaper()
        print("COMPUTER CHOSE ROCK\n")
        printRock()
        print("YOU WIN!! :))\n")
        youWin+=1

    elif you == 2 and computer == 2:
        print("YOU CHOSE PAPER\n")
        printPaper()
        print("COMPUTER CHOSE PAPER\n")
        printPaper()
        print("TIED, TRIED AGAIN.\n")

    elif you == 2 and computer == 3:
        print("YOU CHOSE PAPER\n")
        printPaper()
        print("COMPUTER CHOSE SCISSOR\n")
        printScissor()
        print("COMPUTER WINS :((\n")
        computerWin+=1

    elif you == 3 and computer == 1:
        print("YOU CHOSE SCISSOR\n")
        printScissor()
        print("COMPUTER CHOSE ROCK\n")
        printRock()
        print("COMPUTER WIN :((\n")
        computerWin+=1

    elif you == 3 and computer == 2:
        print("YOU CHOSE SCISSOR\n")
        printScissor()
        print("COMPUTER CHOSE PAPER\n")
        printPaper()
        print("YOU WIN!! :))\n")
        youWin+=1

    elif you == 3 and computer == 3:
        print("YOU CHOSE SCISSOR\n")
        printScissor()
        print("COMPUTER CHOSE SCISSOR\n")
        printScissor()
        print("TIED, TRY AGAIN.)\n")

    else:
        counter-=1
        print(f'''                 ********************
                 |   YOU ARE  = {youWin}   |
                 |   COMPUTER = {computerWin}   |
                 ********************''')


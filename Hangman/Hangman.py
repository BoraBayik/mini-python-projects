import random
def hangman(a):
    if a == 6:
        print(r'''
          +---+
          |   |
              |
              |
              |
              |
        =========''' + '\n')

    elif a == 5:
        print(r'''
          +---+
          |   |
          O   |
              |
              |
              |
        =========''' + '\n')

    elif a == 4:
        print(r'''
          +---+
          |   |
          O   |
          |   |
              |
              |
        =========''' + '\n')

    elif a == 3:
        print(r'''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========''' + '\n')

    elif a == 2:
        print(r'''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        ========='''+'\n')

    elif a == 1:
        print(r'''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========''' + '\n')

    elif a == 0:
        print(r'''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========''' + '\n')


print('''
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝ ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
                                                                
-------------------------------------------------------------------\n''')

words_tr=["kalem", "defter", "masa", "sandalye", "bilgisayar", "telefon", "şemsiye", "anahtar", "çorap", "mutfak", "pencere", "kapı", "koltuk", "sehpa", "çanta", "gözlük", "kitap", "araba", "televizyon", "dolap", "yastık", "battaniye", "fırın", "bahçe", "market"]
words_en=["pencil", "notebook", "table", "chair", "computer", "phone", "umbrella", "key", "sock", "kitchen", "window", "door", "sofa", "bag", "glasses", "book", "car", "television", "closet", "pillow", "blanket", "oven", "garden", "market", "store"]
health=6
language= int(input("1 for English | 2 for Turkish | else for How to play \n"))
i=1
wordselected = ""
guessedword = ""


if language == 1:
    wordselected = random.choice(words_en)
elif language == 2:
    wordselected = random.choice(words_tr)

wordhidden =["_" for _ in wordselected]

while i>0:
    find = False

    if language == 1:
        hangman(health)
        if health == 0:
            print("\n**** GAME OVER ****\n")
            print("The Word was => "+ wordselected)
            i-=1
        elif ''.join(wordhidden) == wordselected:
            print(''.join(wordhidden))
            print("\n**** YOU WIN ****\n")
            i-=1
        else:
            print(f"Your word {''.join(wordhidden)}\n")
            guessedword = input("Tahmin et = ")
            for x in range(len(wordselected)):
                for y in range(len(guessedword)):
                    if wordselected[x] == guessedword[y] and wordhidden[x] == '_':
                        wordhidden[x] = wordselected[x]
                        find = True

            if find == False:
                health -=1



    elif language == 2:
        hangman(health)
        if health == 0:
            print("\n**** OYUN BITTI ****\n")
            print("Bulamadın => " + wordselected)
            i-=1
        elif ''.join(wordhidden) == wordselected:
            print(''.join(wordhidden))
            print("\n **** KAZANDIN ****\n")
            i-=1
        else:
            print(f"Kelimen {''.join(wordhidden)}\n")
            guessedword = input("Tahmin et = ")
            for x in range(len(wordselected)):
                for y in range(len(guessedword)):
                    if wordselected[x] == guessedword[y]  and wordhidden[x] == '_':
                        wordhidden[x] = wordselected[x]
                        find = True

            if find == False:
                health -= 1


    else:
        print('''_______________________________________________________
|  EN = Hangman is a word-guessing game. One player chooses a secret word, and others guess letters. Each wrong guess adds a part to the "hangman" drawing. The goal is to guess the word correctly before the drawing is completed.
|        
|  TR=Hangman, bir kelime tahmin oyunudur. Bir oyuncu gizli bir kelime seçer ve diğer oyuncular harf tahmin eder. Her yanlış tahminde, "adam" resmi tamamlanır. Çok fazla yanlış yapmadan kelimeyi doğru tahmin etmek gerekir.
_______________________________________________________\n''')
        language = int(input("1 for Play English | 2 for Play Turkish\n"))
        if language == 1:
            wordselected = random.choice(words_en)
        elif language == 2:
            wordselected = random.choice(words_tr)
        wordhidden = ["_" for _ in wordselected]


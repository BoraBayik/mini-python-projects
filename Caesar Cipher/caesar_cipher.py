

print('''
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓███████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░        ░▒▓██████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░       ░▒▓█▓▒░      ░▒▓█▓▒░▒▓███████▓▒░░▒▓████████▓▒░▒▓██████▓▒░ ░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                                                                                                                                                                                                                                                   
''')

def caesar(mission, text, shift):
    alphabet_normal_en=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    alphabet_normal_tr=['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']
    alphabet_shifted=[]
    a = True
    while a == True:
        if lan == "en":
            if mission == "encode":
                for i in range(len(text)):
                    if (alphabet_normal_en.index(text[i]) + shift) >= 0 and (alphabet_normal_en.index(text[i]) + shift) < len(alphabet_normal_en):
                        alphabet_shifted.append(alphabet_normal_en[alphabet_normal_en.index(text[i]) + shift])
                    else:
                        if alphabet_normal_en.index(text[i]) + shift < 0:
                            j = (alphabet_normal_en.index(text[i]) + shift)+len(alphabet_normal_en)
                            while j < 0:
                                j+= len(alphabet_normal_en)
                            alphabet_shifted.append(alphabet_normal_en[j])
                        elif alphabet_normal_en.index(text[i]) + shift >= len(alphabet_normal_en):
                            j = (alphabet_normal_en.index(text[i]) + shift) - len(alphabet_normal_en)
                            while j >= len(alphabet_normal_en):
                                j -= len(alphabet_normal_en)
                            alphabet_shifted.append(alphabet_normal_en[j])


                a = False


            elif mission == "decode":
                for i in range(len(text)):
                    if (alphabet_normal_en.index(text[i])) - shift >= 0 and (alphabet_normal_en.index(text[i])) - shift < len(alphabet_normal_en):
                        alphabet_shifted.append(alphabet_normal_en[(alphabet_normal_en.index(text[i])) - shift])

                    else:
                        if (alphabet_normal_en.index(text[i])) - shift < 0:
                            j=((alphabet_normal_en.index(text[i])) - shift) + len(alphabet_normal_en)
                            while j < 0:
                                j+=len(alphabet_normal_en)
                            alphabet_shifted.append(alphabet_normal_en[j])

                        elif (alphabet_normal_en.index(text[i])) - shift >= len(alphabet_normal_en):
                            j = ((alphabet_normal_en.index(text[i])) - shift) - len(alphabet_normal_en)
                            while j >= len(alphabet_normal_en):
                                j -= len(alphabet_normal_en)
                            alphabet_shifted.append(alphabet_normal_en[j])


                a = False

            else:
                print(f"*{mission}* is Unknown mission Try again!!")
                break


        elif lan == "tr":
            if mission == "şifrele":
                for i in range(len(text)):
                    if (alphabet_normal_tr.index(text[i]) + shift) >= 0 and (alphabet_normal_tr.index(text[i]) + shift) < len(alphabet_normal_tr):
                        alphabet_shifted.append(alphabet_normal_tr[alphabet_normal_tr.index(text[i]) + shift])
                    else:
                        if alphabet_normal_tr.index(text[i]) + shift < 0:
                            j = (alphabet_normal_tr.index(text[i]) + shift) + len(alphabet_normal_tr)
                            while j < 0:
                                j += len(alphabet_normal_tr)
                            alphabet_shifted.append(alphabet_normal_tr[j])
                        elif alphabet_normal_tr.index(text[i]) + shift >= len(alphabet_normal_tr):
                            j = (alphabet_normal_tr.index(text[i]) + shift) - len(alphabet_normal_tr)
                            while j >= len(alphabet_normal_tr):
                                j -= len(alphabet_normal_tr)
                            alphabet_shifted.append(alphabet_normal_tr[j])

                a = False


            elif mission == "kır":
                for i in range(len(text)):
                    if (alphabet_normal_tr.index(text[i])) - shift >= 0 and (alphabet_normal_tr.index(text[i])) - shift < len(alphabet_normal_tr):
                        alphabet_shifted.append(alphabet_normal_tr[(alphabet_normal_tr.index(text[i])) - shift])

                    else:
                        if (alphabet_normal_tr.index(text[i])) - shift < 0:
                            j = ((alphabet_normal_tr.index(text[i])) - shift) + len(alphabet_normal_tr)
                            while j < 0:
                                j += len(alphabet_normal_tr)
                            alphabet_shifted.append(alphabet_normal_tr[j])

                        elif (alphabet_normal_tr.index(text[i])) - shift >= len(alphabet_normal_tr):
                            j = ((alphabet_normal_tr.index(text[i])) - shift) - len(alphabet_normal_tr)
                            while j >= len(alphabet_normal_tr):
                                j -= len(alphabet_normal_tr)
                            alphabet_shifted.append(alphabet_normal_tr[j])

                a = False

            else:
                print(f"*{mission}* bilinmeyen bir işlem tekrar deneyin!!")
                break


    print(''.join(alphabet_shifted))


while True:
    lan = input("en OR tr = ")
    if lan == "tr":
        caesar(input("şifrele veya kır = "), input("kelime = "), int(input("kaydırma = ")))
        break
    elif lan == "en":
        caesar(input("encode or decode = "), input("word= "), int(input("shift = ")))
        break
    else:
        print("********************************")
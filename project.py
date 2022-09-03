# Ayden Dazo 2022

import random


def decryptWord(letter):
    match letter:
        case 1:
            new = "a"
        case 2:
            new = "b"
        case 3:
            new = "c"
        case 4:
            new = "d"
        case 5:
            new = "e"
        case 6:
            new = "f"
        case 7:
            new = "g"
        case 8:
            new = "h"
        case 9:
            new = "i"
        case 10:
            new = "j"
        case 11:
            new = "k"
        case 12:
            new = "l"
        case 13:
            new = "m"
        case 14:
            new = "n"
        case 15:
            new = "o"
        case 16:
            new = "p"
        case 17:
            new = "q"
        case 18:
            new = "r"
        case 19:
            new = "s"
        case 20:
            new = "t"
        case 21:
            new = "u"
        case 22:
            new = "v"
        case 23:
            new = "w"
        case 24:
            new = "x"
        case 25:
            new = "y"
        case 26:
            new = "z"
        case default:
            new = "?"
    return new


def encryptOTP(word):
    numbers = []
    numberDictionary = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in word.lower():
        if i in alphabet:
            numberOfWords = alphabet.split(i)
            for i in numberOfWords:
                numberOfWords.pop(1)
            numbers.append(str(len(numberOfWords[0])+1))

    print(numbers)

    for i in range(len(numbers)):
        numberDictionary["number{}".format(i)] = int((random.random()*49)+1)
        numbers[i] = str(int(numbers[i]) + numberDictionary["number{}".format(i)])

    print("\nSAVE THIS FOR DECRYPTION PURPOSES!")
    for i in range(len(numberDictionary)):
        print("Letter {}:".format(i+1), numberDictionary["number{}".format(i)])

    print("\nEncrypted word:")
    for i in range(len(numbers)):
        print(numbers[i], end=" ")


def decryptOTP(code):
    numbers = code.split(",")
    for i in range(len(numbers)):
        if numbers[i].startswith("0"):
            numbers[i] = numbers[i].replace("0", "", 1)
    print(numbers)

    oneTimeNumbers = input("Please input the numbers given for decryption purposes. Seperate only by commas, no spaces (Numbers only!). ")
    while (any(char.isalpha() for char in oneTimeNumbers or (" " in oneTimeNumbers) == True)):
            print("Your text contains letters/spaces.", end=" ")
            oneTimeNumbers = input("Please enter the text that you want to decrypt, seperated by only commas (Numbers Only!). ")
    oneTimeNumbers = oneTimeNumbers.split(",")
    for i in range(len(oneTimeNumbers)):
        if oneTimeNumbers[i].startswith("0"):
            oneTimeNumbers[i] = oneTimeNumbers[i].replace("0", "", 1)

    if (oneTimeNumbers[0] == int(7527)):
        main()

    numsInOldCode = 0
    numsInNewCode = 0
    for i in range(len(numbers)):
        numsInOldCode += 1
    for i in range(len(oneTimeNumbers)):
        numsInNewCode += 1
    if (numsInNewCode != numsInOldCode):
        print("Please re-enter your numbers as the amount does not match.", 
        "\nIf you put in your original numbers wrong, please enter \"7527\" by itself.\n", sep="")
        decryptOTP(code)

    decryptedWord = []
    for i in range(len(numbers)):
        decryptedWord.append(int(numbers[i]) - int(oneTimeNumbers[i]))
    print(decryptedWord)

    for i in range(len(decryptedWord)):
        decryptedWord[i] = decryptWord(decryptedWord[i])
    print("Decrypted word: ", end="")
    for i in range(len(decryptedWord)):
        print(decryptedWord[i], end="")


def encryptCaeser(word):
    shift = input("Please input the amount (between 0-26) you want to shift your text. ")
    while (any(char.isalpha() for char in shift) or int(shift) < 0 or int(shift) > 26):
        print("Contains letters/not in range. Please only input numbers that are in range. ", end="")
        shift = input("Please input the amount (between 0-26) you want to shift your text. ")
    rightorLeft = input("Please input whether you want to shift your text to the right or left. ")
    while (rightorLeft.lower() not in ('right', 'left')):
        print("Not valid. ", end="")
        rightorLeft = input("Please input whether you want to shift your text to the right or left. ")
    
    numbers = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in word.lower():
        if i in alphabet:
            numberOfWords = alphabet.split(i)
            for i in numberOfWords:
                numberOfWords.pop(1)
            numbers.append(str(len(numberOfWords[0])+1))
    print("Before encryption:", end="\n")
    print(numbers)

    print("\nYou're shifting your text by:", shift, "numbers.")
    print("You're shifting your text to the ", rightorLeft.lower(), ".", sep="")

    for i in range(len(numbers)):
        if (rightorLeft.lower() == 'right'):
            if (int(numbers[i]) + int(shift) > 26):
                numbers[i] = (int(numbers[i]) + int(shift)) - 26
            else:
                numbers[i] = int(numbers[i]) + int(shift)
        else:
            if (int(numbers[i]) - int(shift) < 1):
                numbers[i] = int(numbers[i]) - int(shift) + 26
            else:
                numbers[i] = int(numbers[i]) - int(shift)
    print("\nAfter encryption:", end="\n")
    print(numbers)


def decryptCaeser(code):
    numbers = code.split(",")
    for i in range(len(numbers)):
        if numbers[i].startswith("0"):
            numbers[i] = numbers[i].replace("0", "", 1)
    print(numbers)

    shift = input("Please enter the shift (between 1-26). If you do not know it, enter \"0\" (Numbers only!). ")
    while (any(char.isalpha() for char in shift) or int(shift) < 0 or int(shift) > 26):
        print("Contains letters/not in range. Please only input numbers that are in range. ", end="")
        shift = input("Please enter the shift (between 1-26). If you do not know it, enter 0 (Numbers only!). ")
    
    rightOrLeft = input("Please enter whether the text is shifted left or right. Enter \"Unknown\" if you do not know. ")
    while (rightOrLeft.lower() not in ('right', 'left', 'unknown')):
        print("Not valid. ", end="")
        rightOrLeft = input("Please enter whether the text is shifted left or right. Enter \"Unknown\" if you do not know. ")
    rightOrLeft.lower()

    confirmed = "n"
    timesShifted = 0
    if (rightOrLeft == 'unknown' and shift == 0):
        while confirmed == "n":
            for i in range(len(numbers)):
                    if (int(numbers[i]) - int(timesShifted) > 26):
                        numbers[i] = int(numbers[i]) - int(timesShifted) - 26
                    else:
                        numbers[i] = int(numbers[i]) - int(timesShifted)

            decryptedWord = []
            for i in range(len(numbers)):
                decryptedWord.append(numbers[i]) 

            for i in range(len(decryptedWord)):
                decryptedWord[i] = decryptWord(decryptedWord[i])
            print("Decrypted word: ", end="")
            for i in range(len(decryptedWord)):
                print(decryptedWord[i], end="")

            timesShifted += 1
            confirmed = input("\nDoes this look right? y/n ")
            while (confirmed.lower() not in ('y','n')):
                print("Not valid. ", end="")
                confirmed = input("Does this look right? y/n ")
        quit()
    elif (rightOrLeft == 'unknown'):
        rightOrLeft = 'right'
        while confirmed == "n":
            if rightOrLeft == 'right':
                for i in range(len(numbers)):
                    if (int(numbers[i]) - int(timesShifted) > 26):
                        numbers[i] = int(numbers[i]) - int(timesShifted) - 26
                    else:
                        numbers[i] = int(numbers[i]) - int(timesShifted)
            else:
                for i in range(len(numbers)):
                    if (int(numbers[i]) - int(timesShifted) < 1):
                        numbers[i] = int(numbers[i]) - int(timesShifted) + 26
                    else:
                        numbers[i] = int(numbers[i]) - int(timesShifted)

            decryptedWord = []
            for i in range(len(numbers)):
                decryptedWord.append(numbers[i]) 

            for i in range(len(decryptedWord)):
                decryptedWord[i] = decryptWord(decryptedWord[i])
            print("Decrypted word: ", end="")
            for i in range(len(decryptedWord)):
                print(decryptedWord[i], end="")
            
            questionMarks = 0
            for i in decryptedWord:
                if i == "?":
                    questionMarks += 1
                
            if questionMarks == len(decryptedWord):
                rightOrLeft = 'left'

            timesShifted += 1
            confirmed = input("\nDoes this look right? y/n ")
            while (confirmed.lower() not in ('y','n')):
                print("Not valid. ", end="")
                confirmed = input("Does this look right? y/n ")
        quit()
            
    elif (shift == "0"):
        while confirmed == "n":
            if rightOrLeft == 'right':
                for i in range(len(numbers)):
                    if (int(numbers[i]) - int(timesShifted) > 26):
                        numbers[i] = int(numbers[i]) - int(timesShifted) - 26
                    else:
                        numbers[i] = int(numbers[i]) - int(timesShifted)
            else:
                for i in range(len(numbers)):
                    if (int(numbers[i]) - int(timesShifted) < 1):
                        numbers[i] = int(numbers[i]) - int(timesShifted) + 26
                    else:
                        numbers[i] = int(numbers[i]) - int(timesShifted)

            decryptedWord = []
            for i in range(len(numbers)):
                decryptedWord.append(numbers[i]) 

            for i in range(len(decryptedWord)):
                decryptedWord[i] = decryptWord(decryptedWord[i])
            print("Decrypted word: ", end="")
            for i in range(len(decryptedWord)):
                print(decryptedWord[i], end="")

            timesShifted += 1
            confirmed = input("\nDoes this look right? y/n ")
            while (confirmed.lower() not in ('y','n')):
                print("Not valid. ", end="")
                confirmed = input("Does this look right? y/n ")
        quit()
    

    for i in range(len(numbers)):
        if (rightOrLeft == 'right'):
            if (int(numbers[i]) - int(shift) < 1):
                numbers[i] = int(numbers[i]) - int(shift) + 26
            else:
                numbers[i] = int(numbers[i]) - int(shift)
        else:
            if (int(numbers[i]) + int(shift) > 26):
                numbers[i] = (int(numbers[i]) + int(shift)) - 26
            else:
                numbers[i] = int(numbers[i]) + int(shift)
    print(numbers)

    decryptedWord = []
    for i in range(len(numbers)):
        decryptedWord.append(numbers[i]) 

    for i in range(len(decryptedWord)):
        decryptedWord[i] = decryptWord(decryptedWord[i])
    print("Decrypted word: ", end="")
    for i in range(len(decryptedWord)):
        print(decryptedWord[i], end="")


def main():
    encryptOrDecrypt = input("Would you like to encrypt or decrypt (You can also type e/d)? ")
    while (encryptOrDecrypt.lower() not in ('encrypt', 'decrypt', 'e', 'd')):
        print("Not a valid option. You can also put in e/d. ", end="")
        encryptOrDecrypt = input("Would you like to encrypt or decrypt?")
    encryptOrDecrypt = encryptOrDecrypt.lower()

    if (encryptOrDecrypt == 'encrypt' or encryptOrDecrypt == 'e'):
        plaintext = input("Please enter the text that you want to encrypt (Letters Only!). ")
        while any(char.isdigit() for char in plaintext):
            print("Your text contains numbers.", end=" ")
            plaintext = input("Please enter the text that you want to encrypt (Letters Only!). ")

        caeserOrOTP = ""

        print("\nCaeser Cipher")
        print("One Time Pad\n")

        caeserOrOTP = input("Please type your encryption method using one of the above prompts, or type in 1 / 2. ")
        while (caeserOrOTP.lower() not in ('caeser cipher', 'one time pad', '1', '2')):
            print("Not a valid option.", end=" ")
            caeserOrOTP = input("Please type your encryption method using one of the above prompts, or type in 1 / 2. ")
        if (caeserOrOTP.lower() == "caeser cipher" or caeserOrOTP == '1'):
            encryptCaeser(plaintext)
        else:  
            encryptOTP(plaintext)

    else:
        cipherText = input("Please enter the text that you want to decrypt, seperated by only commas (Numbers Only!). ")
        while (any(char.isalpha() for char in cipherText) or (" " in cipherText) == True):
            print("Your text contains letters/spaces.", end=" ")
            cipherText = input("Please enter the text that you want to decrypt, seperated by only commas (Numbers Only!). ")

        caeserOrOTP = ""

        print("\nCaeser Cipher")
        print("One Time Pad\n")

        caeserOrOTP = input("Please type your decryption method using one of the above prompts, or type in 1 / 2. ")
        while (caeserOrOTP.lower() not in ('caeser cipher', 'one time pad', '1', '2')):
            print("Not a valid option.", end=" ")
            caeserOrOTP = input("Please type your decryption method using one of the above prompts, or type in 1 / 2. ")
        if (caeserOrOTP.lower() == "caeser cipher" or caeserOrOTP == '1'):
            decryptCaeser(cipherText)
        else:  
            decryptOTP(cipherText)

main()
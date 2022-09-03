# Ayden Dazo 2022

import random


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
        numberDictionary["number{}".format(i)] = int(random.random()*50)
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
        match decryptedWord[i]:
            case 1:
                decryptedWord[i] = "a"
            case 2:
                decryptedWord[i] = "b"
            case 3:
                decryptedWord[i] = "c"
            case 4:
                decryptedWord[i] = "d"
            case 5:
                decryptedWord[i] = "e"
            case 6:
                decryptedWord[i] = "f"
            case 7:
                decryptedWord[i] = "g"
            case 8:
                decryptedWord[i] = "h"
            case 9:
                decryptedWord[i] = "i"
            case 10:
                decryptedWord[i] = "j"
            case 11:
                decryptedWord[i] = "k"
            case 12:
                decryptedWord[i] = "l"
            case 13:
                decryptedWord[i] = "m"
            case 14:
                decryptedWord[i] = "n"
            case 15:
                decryptedWord[i] = "o"
            case 16:
                decryptedWord[i] = "p"
            case 17:
                decryptedWord[i] = "q"
            case 18:
                decryptedWord[i] = "r"
            case 19:
                decryptedWord[i] = "s"
            case 20:
                decryptedWord[i] = "t"
            case 21:
                decryptedWord[i] = "u"
            case 22:
                decryptedWord[i] = "v"
            case 23:
                decryptedWord[i] = "w"
            case 24:
                decryptedWord[i] = "x"
            case 25:
                decryptedWord[i] = "y"
            case 26:
                decryptedWord[i] = "z"
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
    pass

def main():
    #fileOrPrompt = input("Would you like to encrypt a word from a file or from a prompt? ")

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
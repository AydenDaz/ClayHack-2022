# Ayden Dazo 2022

import random


def otp(word):
    numbers = []
    numberDictionary = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for i in word:
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


def caeser(word):
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
    for i in word:
        if i in alphabet:
            numberOfWords = alphabet.split(i)
            for i in numberOfWords:
                numberOfWords.pop(1)
            numbers.append(str(len(numberOfWords[0])+1))
    print(numbers)

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
    print(numbers)


def main():
    #fileOrPrompt = input("Would you like to encrypt a word from a file or from a prompt? ")

    encryptOrDecrypt = input("Would you like to encrypt or decrypt?")

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
      caeser(plaintext)
    else:  
        otp(plaintext)

main()
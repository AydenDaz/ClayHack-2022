# Ayden Dazo 2022

import random

def encryptWord(word):
    numbers = []
    theNum = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in word:
        if i in alphabet:
            theThing = alphabet.split(i)
            for i in theThing:
                theThing.pop(1)
            numbers.append(str(len(theThing[0])+1))
    print(numbers)
    for i in range(len(numbers)):
        theNum["number{}".format(i)] = int(random.random()*50)
        numbers[i] = str(int(numbers[i]) + theNum["number{}".format(i)])
    print("\nSAVE THIS FOR DECRYPTION PURPOSES!")
    for i in range(len(theNum)):
        print("Letter {}:".format(i+1), theNum["number{}".format(i)])
    print("\n",numbers, sep="")

def main():
    #fileOrPrompt = input("Would you like to encrypt a word from a file or from a prompt? ")
    plaintext = input("Please enter a word that you want to encrypt (Letters Only!). ")

    print("\nCaeser Cipher")
    print("One Time Pad\n")

    encryptWord(plaintext)

main()
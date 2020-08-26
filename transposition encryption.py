#this program is an transposition Encrption
import math
#the main part of program
def main():
    print("welcome to jsk's encryption ")
    print("""\t 1. encrypt
\t 2. decrypt""")
    choose = int(input("select encrypt or decrypt the message : "))
    while (choose < 1) or (choose > 2):
        choose = int(input("enter either 1 or 2 to select option : "))
    if choose == 1:
        encrypt()
    else:
        decrypt()



#this is encryption part of the program
def encrypt():
    plaintext = input("enter the message you want to encrypt : ")
    key = int(input("enter the key to encrypt the message : "))
#it take key and message to enrypt
    cipherText = encryption(key, plaintext)

    print(cipherText + '|')


def encryption(key, message):
#multiply the list length with key
    cipher = [''] * key
#create column with range key
    for column in range(key):
        currentIndex = column

        while currentIndex < len(message):

            cipher[column] += message[currentIndex]

            currentIndex += key

    return ''.join(cipher)

#decryption part of the program
def decrypt():
    ciphertext = input("Enter the message to decrypt : ")
    key = int(input("Enter the key to decrypt the message : "))

    plaintext = decryption(key, ciphertext)

    print(plaintext)

def decryption(key, message):

    numofRows = key
    numofColumn = int(math.ceil(len(message)/ float(key)))

    numofShaded = (numofColumn * numofRows) - len(message)

    plaintext = [''] * numofColumn

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (column == numofColumn) or (column == numofColumn -1 and
                                       row >= numofRows - numofShaded):
            column = 0
            row += 1

    return ''.join(plaintext)


start= True
while start:
    main()
    again = input("if you want to encrypt or decrypt another message, enter y : ")
    if again == 'y':
        start = True
    else:
        start = False

print("bye")
        

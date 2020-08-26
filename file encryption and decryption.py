#this program encrypt and decrypt file using transposition encryption

import time, os, sys, easygui, transpositionencryption

def main():
    print("""\t1. encrypt
\t2. decrypt """)

#ask the user to select the mode
    choose = int(input("enter 1 or 2 to select the mode : "))

    while(choose < 1) or (choose > 2):
        choose = int(input("Enter 1 or 2 to select the mode : "))

    if choose == 1:
        mode = "Encrypt"
    else:
        mode = "Decrypt"
        
#both encrypt and decrypt are same some part is only changed
#we use easygui module to open the file and save the file 
#ask the user to enter the key to encrypt or decrypt        
#save the output file in location given by user and store as txt file

    inputFile = easygui.fileopenbox(msg = "select the file to %s" %(mode), filetypes = 'txt')
    key = int(input("Enter the key to %s : " %(mode)))    
    outputFile = easygui.filesavebox(msg = "Enter the output file name : ", filetypes = 'txt')
        
#if output file name is already exists ask the user what to do 
    if os.path.exists(outputFile):
        print("This will overwrite the file %s. (C)ontinue or (Q)uit ?" %(outputFile))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

#open the input file 

    fileObj = open(inputFile)
#read the opened file and store in content
    content = fileObj.read()
#finnaly close the file after read it
    fileObj.close()

#print the mode is start
    print('%s starts .........' %(mode))

#calculate the time taken to encrypt or decrypt
    startTime = time.time()
    if choose == 1:
        translate = transpositionencryption.encryption(key, content)
    else:
        translate = transpositionencryption.decryption(key, content)

    totalTime = round(time.time() - startTime, 2)

#show the time taken in  display 
    print('%sion timetaken: %s second' %(mode, totalTime))

#open the ouput file and write the encrypted message and close
    outputFileObj = open(outputFile, 'w')
    outputFileObj.write(translate)
    outputFileObj.close()

#after writen the content in output file show how many charaters it encrypted it
    print('Done %sing %s (%s charaters). ' %(mode, inputFile, len(content)))
    print('%sed file is %s. ' %(mode, outputFile))

print("welcome to jsk's file  encryption")

start = True
while start:
    main()
    again = input("if you want to encrypt or decrypt another file : enter 'y' :" )
    if again == 'y':
        start = True
    else:
        start = False
        

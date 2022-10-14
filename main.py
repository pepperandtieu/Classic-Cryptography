from caesar import caesar
from affine import affine
from vigenere import vigenere
from autokey import autokey
from numeral import numeral
from columnar import columnar
from transposition import transposition

def __main__():
     alphabetNum = 3
     # alphabetNum:
         #0: classic uppercase and lowercase
         #1: classic uppercase, lowercase, and numbers
         #2: qwerty uppercase, lowercase, numbers and space
         #3: classic uppercase, lowercase, numbers, space and some punctuations
         #4: all available qwerty letters and symbols on keyboard
    
     while 1:
          # print all available ciphers
          cipherList = ["Caesar [0]","Affine [1]","Vigenere [2]","Autokey [3]","Numeral [4]","Columnar [5]","Transposition [6]"]
          cipherDict = {"0":caesar,"1":affine,"2":vigenere,"3":autokey,"4":numeral,"5": columnar,"6":transposition}
          print("Available ciphers:")
          print(cipherList)
          
          
          
          #print("[1]: Use 1 cipher")
          #print("[2]: Use multiple ciphers")
          cipherOption = 1
          #while cipherOption != 1 and cipherOption != 2:
          #     cipherOption = int(input("Enter a number of ciphers to use: "))
          
          # Choose the cipher wanted to use
          print("\nAvailable number: 0 to",len(cipherList)-1)
          
          
          cipherSequence = ""
          if cipherOption == 1:
               while cipherSequence not in cipherDict.keys():
                    cipherSequence = input("Enter the cipher number: ")
          #else:
          #     while len(cipherSequence) == 0:
          #          cipherSequence = input("Enter sequence of ciphers: ")
                  
          
          #print("[1]: By File")
          #print("[2]: Python Console")
          inputType = 2
          while inputType != 1 and inputType != 2:
               inputType = int(input("Choose the input option: "))
               
          outputType = 2
          while outputType != 1 and outputType != 2:
               outputType = int(input("Choose the output option: "))
          
          
          mode = 0
          while mode != 1 and mode != 2:
               mode = int(input("Encrypt[1] or Decrypt[2]: "))
          
          if inputType == 1:
               inFile = input("Enter input file name (no extension): ")
               inFile = inFile + ".txt"
               message = ""
               try:
                   with open(inFile) as file:
                       for line in file.readlines():
                            message += line
               except FileNotFoundError:
                   print("Error! File not Found")
                   exit(1)
          else:
               message = input("Enter message: ")
          
             
          # encode or decode messages
          inputText = message
          if mode == 1:
               for cipher in cipherSequence:
                    print("\n" + cipherList[int(cipher)])
                    translated = cipherDict[cipher](inputText,alphabetNum,mode,cipherSequence)
                    inputText = translated
          else:
               for cipher in cipherSequence[::-1]:
                    print("\n" + cipherList[int(cipher)])
                    translated = cipherDict[cipher](inputText,alphabetNum,mode,cipherSequence)
                    inputText = translated
          if outputType == 1:
               outFile = input("Enter output file name: ")
               fileName = open(outFile + ".txt","w")
               fileName.write(translated)
               fileName.close()
          else:
               print(translated)
               print()
               print()





__main__()
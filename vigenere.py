from alphabet import baseCall

def vigenere(message,alphabetOption,choice,cipherSequence):
     alphabet = baseCall(alphabetOption)
     keyword = input("Enter keyword: ")
     if choice == 1:
          encrypted = encrypt(message,keyword,alphabet)
          return encrypted
     else:
          decrypted = decrypt(message,keyword,alphabet)
          return decrypted
          
def encrypt(message,keyword,alphabet):
     outMessage = ""
     key_loc = 0
     for item in message:
          while keyword[key_loc] not in alphabet and key_loc < len(keyword):
               key_loc += 1
          if item in alphabet:
               key_start = alphabet.index(keyword[key_loc])
               loc = alphabet.index(item)
               newLoc = (key_start + loc) % len(alphabet)
               outMessage += alphabet[newLoc]
               key_loc += 1
          else:
               outMessage += item
          
          if key_loc >= len(keyword):
               key_loc = 0
     return outMessage
               
def decrypt(message,keyword,alphabet):
     outMessage = ""
     key_loc = 0
     for item in message:
          while keyword[key_loc] not in alphabet and key_loc < len(keyword):
               key_loc += 1
          if item in alphabet:
               key_start = alphabet.index(keyword[key_loc])
               loc = alphabet.index(item)
               newLoc = (loc - key_start) % len(alphabet)
               outMessage += alphabet[newLoc]
               key_loc += 1
          else:
               outMessage += item
          
          if key_loc >= len(keyword):
               key_loc = 0
     return outMessage

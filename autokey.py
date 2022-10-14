from alphabet import baseCall

def autokey(message,alphabetOption,mode,cipherSequence=""):
     alphabet = baseCall(alphabetOption)
     keyword = input("Enter keyword: ")
     if mode == 1:
          encrypted = encrypt(message,keyword,alphabet)
          return encrypted
     else:
          decrypted = decrypt(message,keyword,alphabet)
          return decrypted
     
def encrypt(message,keyword,alphabet):
     translated = ""
     keyIndex = 0
     keyword = keyword + message
     for symbol in message:
          while keyword[keyIndex] not in alphabet and keyIndex < len(keyword):
               keyIndex += 1
          if symbol in alphabet:
               keyLoc = alphabet.index(keyword[keyIndex])
               symbolIndex = alphabet.index(symbol)
               newLoc = (keyLoc + symbolIndex) % len(alphabet)
               translated += alphabet[newLoc]
               keyIndex += 1
          else:
               translated += symbol
          
          if keyIndex >= len(keyword):
               keyIndex = 0
     return translated

def decrypt(message,keyword,alphabet):
     translated = ""
     keyIndex = 0
     for symbol in message:
          while keyword[keyIndex] not in alphabet:
               keyIndex += 1
          if symbol in alphabet:
               keyLoc = alphabet.index(keyword[keyIndex])
               symbolIndex = alphabet.index(symbol)
               newLoc = (symbolIndex - keyLoc) % len(alphabet)
               translated += alphabet[newLoc]
               keyword += alphabet[newLoc]
               keyIndex += 1
          else:
               translated += symbol
          
          if keyIndex >= len(keyword):
               keyIndex = 0
     return translated

     
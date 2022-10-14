from alphabet import baseCall

def caesar(message,alphabetOption,mode,cipherSequence = ""):
     alphabet = baseCall(alphabetOption)
     key = int(input("Enter number key: "))
     if mode == 1:
          encrypted = encrypt(message,key,alphabet)
          return encrypted
     else:
          decrypted = decrypt(message,key,alphabet)
          return decrypted


def encrypt(message,key,alphabet):
     translated = ""
     for symbol in message:
          if symbol in alphabet:
               loc = alphabet.index(symbol)
               newLoc = (loc + key) % len(alphabet)
               translated += alphabet[newLoc]
          else:
               translated += symbol
     return translated
          
def decrypt(message,key,alphabet):
     translated = ""
     for symbol in message:
          if symbol in alphabet:
               loc = alphabet.index(symbol)
               newLoc = (loc - key) % len(alphabet)
               translated += alphabet[newLoc]
          else:
               translated += symbol
      
     return translated


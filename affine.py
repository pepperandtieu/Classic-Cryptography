from alphabet import baseCall

def affine(message,alphabetOption,mode,cipherSequence=""):
     alphabet = baseCall(alphabetOption)
     invMod = -1
     while invMod == -1:
          key1 = int(input("Enter number key 1: "))
          invMod = inverseMod(key1,len(alphabet))
          if invMod == -1:
               print("Enter another value for number key 1")
     
     key2 = int(input("Enter number key 2: "))
     key = [key1,key2]
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
               newLoc = (key[0]*loc + key[1]) % len(alphabet)
               translated += alphabet[newLoc]
          else:
               translated += symbol
     return translated

def decrypt(message,key,alphabet):
     translated = ""
     a_alpha = inverseMod(key[0],len(alphabet))
     for symbol in message:
          if symbol in alphabet:
               loc = alphabet.index(symbol)
               newLoc = (a_alpha*(loc - key[1])) % len(alphabet)
               translated += alphabet[newLoc]
          else:
               translated += symbol
      
     return translated
 
    
def inverseMod(a,b):
     x = 0
     found = False
     while x < b and found == False:
          if (a*x) % b == 1:
               found = True
               return x
          else:
               x+= 1
     return -1
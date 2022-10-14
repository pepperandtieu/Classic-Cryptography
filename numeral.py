from alphabet import baseCall

def numeral(message,alphabetOption,mode,cipherSequence):
     alphabet = baseCall(alphabetOption)
     base = 1
     while base < 2 or base > 10:
          base = int(input("Enter base number (2-10): "))
     if mode == 1:
          encrypted = encrypt(message,base,alphabet)
          return encrypted
     else:
          decrypted = decrypt(message,base,alphabet)
          return decrypted

def encrypt(message,base,alphabet):
     translated = ""
     for item in message:
          if item in alphabet:
               temp = toNum(item,alphabet,base)
               translated += temp
          else:
               translated += item
     return translated

def decrypt(message,base,alphabet):
     translated = ""
     length = 0
     exponent = 0
     while base**exponent < len(alphabet):
          length += 1
          exponent += 1
     
     i = 0
     while i < len(message):
          group = ""
          while len(group) < length:
               if message[i].isnumeric():
                    group += message[i]
                    i += 1
               else:
                    translated += message[i]
                    i += 1
                    
          if len(group) == length:          
               loc = 0          
               for n in range(length):
                    loc += int(group[n])*(base**n)
               translated += alphabet[loc]
     
     return translated

def toNum(letter,alphabet,base):
     length = 0
     
     # Determine the length of numbers representing the alphabet
     # base^length is the maximum number of representation available having the same length
     while base**length < len(alphabet):
          length += 1
     
     remainder = alphabet.index(str(letter))
     result = ""
     # Translation
     # first letter in alphabet is all 0
     if remainder == 0:
          result = "0"*length
     else:
          while remainder > 0:
               temp = remainder % base
               result += str(temp)
               remainder = remainder // base
     while len(result) < length:
          result += "0"
          
     return result

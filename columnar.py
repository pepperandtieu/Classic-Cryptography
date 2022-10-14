from alphabet import baseCall
import random

def columnar(message,alphabetOption,mode,cipherSequence=""):
     alphabet = baseCall(alphabetOption)
     keyword = ""
     while len(keyword) == 0 or checkKeyword(keyword,alphabet) == False:
          keyword = input("Enter keyword: ")

     if mode == 1:
          if "4" in cipherSequence:
               while len(message) % len(keyword) != 0:
                    numberList = [1,0]
                    message += str(numberList[random.randint(0,len(numberList)-1)])
          else:
               while len(message) % len(keyword) != 0:
                    message += alphabet[random.randint(0,len(alphabet)-1)]
          encrypted = encrypt(message,keyword,alphabet)
          return encrypted
     else:
          decrypted = decrypt(message,keyword,alphabet)
          return decrypted
     
def encrypt(message,keyword,alphabet):
     groupList = []
     translated = ""
     sortedKeyword = sortKeyword(keyword,alphabet)          
     #print(message)
     
     for element in range(len(keyword)):
          groupList.append("")
     
     loc = 0
     for letter in message:
          group = loc % len(keyword)
          groupList[group] += letter
          loc += 1
     #print(groupList)
     
     for i in range(len(keyword)):
          loc = sortedKeyword.index(str(i))
          translated += groupList[loc]
          #print(outMessage)
          
     return translated
               
def decrypt(message,keyword,alphabet):
     translated = ""
     sortedKeyword = sortKeyword(keyword,alphabet)
     groupList = list()
     for i in range(len(keyword)):
          groupList.append("")
     
     size = len(message) // len(keyword)
     #print(size)
     for i in range(len(keyword)):
          group = message[(i*size):(size*(i + 1))]
          #print(group)
          loc = sortedKeyword.index(str(i))
          groupList[loc] = group
          #print(groupList)
     
     for i in range(len(groupList[0])):
          for group in groupList:
               translated += group[i]
               #print(outMessage)
     return translated

def sortKeyword(keyword,alphabet):
     sortedKeyword = []
     for i in range(len(keyword)):
          sortedKeyword.append(-1)
               
     keywordList = list(keyword)     
     value = 0
     for x in range(len(keyword)):
          minLetter = keywordList[0]
          for y in range(len(keywordList)):
               if alphabet.index(keywordList[y]) < alphabet.index(minLetter):
                    minLetter = keywordList[y]
          realLoc = keyword.index(minLetter)
          #print("realLoc",realLoc)
          while sortedKeyword[realLoc] > -1:
               tempLoc = realLoc + 1
               realLoc = keyword[tempLoc::].index(minLetter) + tempLoc
               #print("real LOC",realLoc)
          sortedKeyword[realLoc] = value
          value += 1
          keywordList.remove(minLetter)
          
          #print("sorted Keyword:",sortedKeyword)
          #print("keywordList",keywordList)
          #print("keyword:",keyword)
          #print()
     for i in range(len(sortedKeyword)):
          sortedKeyword[i] = str(sortedKeyword[i])
     return sortedKeyword

def checkKeyword(keyword,alphabet):
     for letter in keyword:
          if letter not in alphabet:
               return False
     return True

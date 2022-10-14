from alphabet import baseCall

def transposition(message,alphabetOption,mode,cipherSequence):
     alphabet = baseCall(alphabetOption)
     key = int(input("Enter number key: "))
     if mode == 1:
          encrypted = encrypt(message,key)
          return encrypted
     else:
          decrypted = decrypt(message,key)
          return decrypted
def encrypt(message,key):
    groupList = []
    translated = ""
    for i in range(key):
        groupList.append("")
          
    for SymbolIndex in range(len(message)):
        insertLoc = SymbolIndex % key
        groupList[insertLoc] += message[SymbolIndex]
        
    for group in groupList:
        translated += group
        
    return translated

def decrypt(message,key):
    groupList = []
    translated = ""
    for i in range(key):
        groupList.append("")
    
    reduceStartPt = 0
    if len(message) % key != 0:
        groupLength = len(message) // key + 1
        reduceStartPt = len(message) % key
    else:
        groupLength = len(message) // key
    
    endPt = 1
    for groupIndex in range(key):
        if groupIndex < reduceStartPt:
            startPt = groupIndex * groupLength
            endPt = startPt + groupLength
        else:
            startPt = endPt
            endPt = startPt + groupLength - 1
            
        groupList[groupIndex] += message[startPt : endPt]
    
    for symbolIndex in range(groupLength):
        for group in groupList:
            if symbolIndex < len(group):
                translated += group[symbolIndex]

    return translated

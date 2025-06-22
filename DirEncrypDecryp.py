# Direct Text File Encrypting Decrpyting System
MasterDictionary =  {'A': '9', 'B': 'I', 'C': 'R', 'D': 'r', 'E': '5', 'F': '-', 'G': ':', 'H': 'a', 'I': 'S', 'J': "'", 'K': '@', 'L': 'F', 'M': '4', 'N': 't', 'O': 'm', 'P': 'u', 'Q': 'c', 'R': 'K', 'S': 'k', 'T': 'Y', 'U': '[', 'V': 'C', 'W': 'Z', 'X': 's', 'Y': ';', 'Z': 'M', 'a': '/', 'b': 'E', 'c': 'Q', 'd': '*', 'e': '?', 'f': '!', 'g': ',', 'h': 'A', 'i': '$', 'j': 'N', 'k': '%', 'l': '3', 'm': '\\', 'n': 'v', 'o': 'z', 'p': 'P', 'q': 'L', 'r': 'W', 's': 'p', 't': '>', 'u': 'o', 'v': '=', 'w': '0', 'x': 'H', 'y': 'b', 'z': '2', '1': 'i', '2': '6', '3': 'w', '4': '(', '5': '<', '6': 'T', '7': '^', '8': 'g', '9': ']', '0': 'n', '!': '{', '@': 'J', '#': '_', '$': '}', '%': 'X', '^': 'G', '&': '"', '*': '7', '(': '8', ')': 'V', '-': ')', '_': 'd', '=': '1', '+': '.', '[': '+', ']': 'D', '{': 'j', '}': 'U', '\\': 'h', ';': 'O', ':': 'f', "'": 'e', '"': 'x', ',': 'l', '<': 'q', '.': '&', '>': 'B', '?': 'y', '/': '#'}
KeyDictionary =  {'9': 'A', 'I': 'B', 'R': 'C', 'r': 'D', '5': 'E', '-': 'F', ':': 'G', 'a': 'H', 'S': 'I', "'": 'J', '@': 'K', 'F': 'L', '4': 'M', 't': 'N', 'm': 'O', 'u': 'P', 'c': 'Q', 'K': 'R', 'k': 'S', 'Y': 'T', '[': 'U', 'C': 'V', 'Z': 'W', 's': 'X', ';': 'Y', 'M': 'Z', '/': 'a', 'E': 'b', 'Q': 'c', '*': 'd', '?': 'e', '!': 'f', ',': 'g', 'A': 'h', '$': 'i', 'N': 'j', '%': 'k', '3': 'l', '\\': 'm', 'v': 'n', 'z': 'o', 'P': 'p', 'L': 'q', 'W': 'r', 'p': 's', '>': 't', 'o': 'u', '=': 'v', '0': 'w', 'H': 'x', 'b': 'y', '2': 'z', 'i': '1', '6': '2', 'w': '3', '(': '4', '<': '5', 'T': '6', '^': '7', 'g': '8', ']': '9', 'n': '0', '{': '!', 'J': '@', '_': '#', '}': '$', 'X': '%', 'G': '^', '"': '&', '7': '*', '8': '(', 'V': ')', ')': '-', 'd': '_', '1': '=', '.': '+', '+': '[', 'D': ']', 'j': '{', 'U': '}', 'h': '\\', 'O': ';', 'f': ':', 'e': "'", 'x': '"', 'l': ',', 'q': '<', '&': '.', 'B': '>', 'y': '?', '#': '/'}

def Encrypt():
    Path = input("Enter the text documents complete file path: ")
    f = open(Path,"r")
    txt = f.read()
    ntxt = ""
    for i in txt:
        if i in MasterDictionary.keys():
            ntxt += MasterDictionary[i]
        else:
            ntxt += i
    f.close()
    
    f = open(Path,"w")
    f.write(ntxt)
    f.close()

    print("File has been encrypted")

def Decrypt():
    Path = input("Enter the text documents complete file path: ")
    f = open(Path,"r")
    txt = f.read()
    ntxt = ""
    for i in txt:
        if i in KeyDictionary.keys():
            ntxt += KeyDictionary[i]
        else:
            ntxt += i
    f.close() 
    
    f = open(Path,"w")
    f.write(ntxt)
    f.close()

    print("File has been decrypted")

ch = "y"

while ch == "y":
    print("1.Encrypt a file","2.Decrypt a file", sep = "\n")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        Encrypt()
    elif choice == 2:
        Decrypt()
    else:
        print("Invalid input!")
    ch = input("Do you want to continue? (y/n) :")
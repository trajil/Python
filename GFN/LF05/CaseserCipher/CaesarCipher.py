import json

# Set Values
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keyLengthLimiter = len(alphabet)
text_output = ""

encode_decode =""
key = 0 
text_input =""
crypting = ""

# User Input
#encode_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#text_input = input("Type your message:\n").lower()
#print("Maximum key length: ", keyLengthLimiter)
#key = abs(int(input("Type the shift number:\n")))



def readInputfileAndSetParameters():
    global encode_decode, key, text_input
    with open('input.json', 'r') as file:
        input = json.load(file)
        encode_decode = input["encode_decode"]
        print(encode_decode)
        key = input["key"]
        print(key)
        text_input = input["text_input"].lower()
        print('"',text_input,'"')
    
def checkDirection(encode_decode):
    global crypting, decode
    if encode_decode == 'encode':
        decode = False
        crypting = "encrypted"
        print("encoding...")
        return decode
    elif encode_decode == 'decode':
        decode = True
        crypting = "decrypted"
        print("decoding...")
        return decode
    else:
        print("Please only use 'decode' or 'encode'!")
    
def checkAndLimitKeyLength(key, decode):   
    #global key 
    if key > keyLengthLimiter:
        key = keyLengthLimiter  
        print("key: ", key)
    if decode:
        key = -abs(key)
    return key 
               
def encryptAndPrint(text_input, key):
    global text_output
    print("opening output.txt...\n ")
    outputFile = open('output.txt', 'w')
    
    for char in text_input:
        if char in alphabet:
            new_index = (alphabet.index(char) + key) % keyLengthLimiter
            text_output += alphabet[new_index]
        elif char == " ":
            text_output += char
        
    print("Input: ", text_input,"\nOutput: ", text_output,"\nUsed Key: ", key, "[", crypting ,"]", file = outputFile)
    print("closing output.txt: ")
    
    outputFile.close()  


readInputfileAndSetParameters()
checkDirection(encode_decode)
key = checkAndLimitKeyLength(key, decode)
encryptAndPrint(text_input, key)

input("")
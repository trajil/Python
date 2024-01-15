# Set Values
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
keyLengthLimiter = len(alphabet) - 1
text_output = ""


# User Input
direction_iput = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text_input = input("Type your message:\n").lower()
print("Maximum key length: ", keyLengthLimiter)
key = abs(int(input("Type the shift number:\n")))

def readInputfileAndSetParameters():
    print("PIPI")
    
def checkDirection():
    global decode
    if direction_iput == 'encode':
        decode = False
        print("encoding...")
    elif direction_iput == 'decode':
        decode = True
        print("decoding...")
    else:
        print("Please only use 'decode' or 'encode'!")
    
def checkAndLimitKeyLength(key, decode):    
    if key > keyLengthLimiter:
        key = keyLengthLimiter  
        print("key: ", key)
        return key  
    if decode:
        key = -key
        print("key: ", key)
        return key 
               
def encryptAndPrint(text_input):
    global text_output
    print("OUTPUT BEFORE FUNCTION: ",text_output)
    for char in text_input:
        if char in alphabet:
            new_index = (alphabet.index(char) + key) % keyLengthLimiter
            text_output += alphabet[new_index]
        elif char == " ":
            text_output += char
        
    print("OUTPUT AFTER FUNCTION: ",text_output)
    


# readInputfileAndSetParameters()

checkDirection()
checkAndLimitKeyLength(key,decode)
encryptAndPrint(text_input)
# OUTPUT OLD
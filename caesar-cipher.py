def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
    
def encryptMessage(message,cipherKey,alphabet):
    encryptedMessage = ""
    uppercaseMessage = message.upper()
    for cur in uppercaseMessage:
        newpos = alphabet.find(cur) + int(cipherKey)
        if cur in alphabet:
            encryptedMessage += alphabet[newpos]
        else:
            encryptedMessage += cur
    return encryptedMessage

def decryptmessage(message,cipherkey,alphabet):
    decryptKey = -1 * int(cipherkey)
    return encryptMessage(message,decryptKey,alphabet)

def runCaesarCipherProgram():
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')
    myMessage = getMessage()
    print(myMessage)
    myCipherKey = getCipherKey()
    print(myCipherKey)
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decryptmessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')


runCaesarCipherProgram()
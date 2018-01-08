from collections import Counter

MAX_KEY_SIZE = 26

engDictionary = "EARIOTNSLCUDPMHGBFYWKVXZJQ"
latinDictionary = "eituasrnomcpldqbgvfhxykzjw"


def getMessage():
    print("Enter your message to decript: ")
    return input()

def getKey():
    count = 0
    print("Enter the language you want to use: (eng/latin)")
    if(input() == "eng"):
        dictionaryValue = engDictionary[count]
    else:
        dictionaryValue = latinDictionary[count]
    key = ord(frequency(message)[0][0]) - ord(dictionaryValue)
    count+=1
    return key

def frequency(message):
    message = "".join(message.split())
    counter = Counter(message)
    return counter.most_common(1)


def showMessage(counter):
    print("Your translated text is: ")
    print(getTranslatedMessage(message, key + counter))
    print("Is it translated well? (y/n)")
    if(input() == "n"):
        counter += 1
        showMessage(counter)





def getTranslatedMessage(message,key):
    key = -key
    translated = ""
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated


message = getMessage()
key = getKey()


print("Most frequent letter is:")
print(frequency(message))

showMessage(counter=0)





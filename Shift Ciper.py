# Code example found:
# https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
# Separating encrypted and decrypted code:
# https://stackoverflow.com/questions/37505224/add-a-space-between-each-word-in-the-string



import re

def encrypt(text, s):
    result = ""
    # transverse the plain text
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


def decrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text

        if char.isupper():
            result += chr((ord(char) - s - 65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
    return result


# check the above function
text = input("Type in text:")
tokens = text.split(" ")
c_text = ''.join(tokens)
s = int(input("Enter in shift value:"))
ask = input('Would you like to encrypt or decrypt a message:')

if ask == 'encrypt':
    print("Plain Text : " + text)
    print("Shift pattern : " + str(s))
    print("Cipher: " + re.sub('([A-Z])', r' \1', encrypt(c_text, s)))
elif ask == 'decrypt':
    print("Plain Text : " + text)
    print("Shift pattern : " + str(s))
    print("Cipher: " + re.sub('([A-Z])', r' \1', decrypt(c_text, s)))

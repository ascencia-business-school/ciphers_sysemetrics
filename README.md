# Encryption and Decryption Script
This Python script provides a simple implementation of a Caesar cipher, a basic encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

the above function is encrypts a given text by shifting its characters by a specified number of positions.


text = "Welcome to Malta"
shift = 4
result = encrypt(text, shift)
print("Original Text:", text)
print("Encrypted Text:", result)

# In the above code 
text is used for The input string that needs to be encrypted or decrypted.
shift: The number of positions each character in the string is shifted by 4.

# the output
Original Text: Welcome to Malta
Encrypted Text: Aipgsqi xs Qepxe


# for the decrypt
text = " Aipgsqi xs Qepxe  " # the encrypted text
shift = -4
result = encrypt(text, shift)
print("original Tect", text)
print("encrypted text: ", result)

# in the above code
text is used for The input string that needs to be decrypted.
shift: The number of positions each character in the string is shifted by -4. 

# the output
Original Text: Aipgsqi xs Qepxe
Encrypted Text: Welcome to Malta


def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - ascii_offset + shift ) % 26 + ascii_offset)
        else:
            result += char
    return result   

text = "Welcome to Malta "
shift = 4
result = encrypt(text, shift)
print("original Tect", text)
print("encrypted text: ", result)

'''
to decrypt the encrypted text, 
we can use the same function with a negative shift value

'''
text = " Aipgsqi xs Qepxe  "
shift = -4
result = encrypt(text, shift)
print("original Tect", text)
print("encrypted text: ", result)
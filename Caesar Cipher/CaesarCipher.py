def encrypt(text, s):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z': 
            # Calculate the position of the character (0-25)
            p = ord(char) - ord('A')
            # Apply the Caesar Cipher formula
            c = (p + s) % 26
            # Convert back to character
            result += chr(c + ord('A'))
        elif 'a' <= char <= 'z':  # Support for lowercase letters
            p = ord(char) - ord('a')
            c = (p + s) % 26
            result += chr(c + ord('a'))
        else:
            result += char  # Keep non-alphabet characters unchanged

    return result

# Get user input
text = input("Enter text to encrypt: ")
s = int(input("Enter shift value: "))

# Encrypt and display the result
print("Cipher: " + encrypt(text, s))


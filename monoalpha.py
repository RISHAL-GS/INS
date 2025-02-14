def monoencrypt(text):  # Encrypt function
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Reference table
    cipher = "ZXCVBNMLKJHGFDSAPOIUYTREWQ"
    
    encrypted_text = ""  # Encrypted data storage
    msg = text.upper()  # Convert plain text to uppercase
    
    for i in msg:
        if i.isalpha():  # Check if character is an alphabet
            indexx = alphabets.index(i)
            encrypted_text += cipher[indexx]
        else:
            encrypted_text += i
    
    return encrypted_text

def monodecrypt(encrypted_text):  # Decrypt function
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cipher = "ZXCVBNMLKJHGFDSAPOIUYTREWQ"
    
    decrypted_text = ""
    
    for i in encrypted_text:
        if i.isalpha():
            ind = cipher.index(i)  # Get index of letter in cipher
            decrypted_text += alphabets[ind]  # Get corresponding letter in alphabet
        else:
            decrypted_text += i
    
    return decrypted_text

# User input
text = input("Enter plaintext here: ")
encrypted_text = monoencrypt(text)
print("Encrypted text: " + encrypted_text)

decrypted_text = monodecrypt(encrypted_text)
print("Decrypted text: " + decrypted_text)

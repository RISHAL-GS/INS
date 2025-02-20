Vignere_Cipher:
def vigenere_encrypt(plaintext, key):
    key = key.upper()
    ciphertext=""
    key_index=0
    for char in plaintext.upper():
        if char.isalpha():
            shift = ord(key[key_index])-ord('A')
            ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

plaintext =input("Enter the plaintext:")
key = input("Enter the Key:")
Cipher=vigenere_encrypt(plaintext, key)
print("Encrypted:",Cipher )

def vigenere_decrypt(plaintext, key):
    key=key.upper()
    decrypt=""
    key_index=0
    for char in plaintext.upper():
        if char.isalpha():
            shift = ord(key[key_index])-ord('A')
            decrypt += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            decrypt += char
    return decrypt
print("Decrypted:", vigenere_decrypt(Cipher,key))

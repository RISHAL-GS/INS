# Vigenère Cipher Encryption & Decryption

## Description
This Python script implements the Vigenère cipher encryption and decryption algorithm. It encrypts messages using a repeating keyword-based shift, making it more secure than a simple Caesar cipher.

## Features
- Encrypts plaintext using a Vigenère cipher key.
- Decrypts the encrypted text back to its original form.
- Retains non-alphabetical characters as they are.

## Encryption & Decryption Algorithm
### Encryption
- The key is converted to uppercase.
- Each letter in the plaintext is shifted based on the corresponding letter in the key.
- Non-alphabetical characters remain unchanged.

### Decryption
- The key is converted to uppercase.
- Each letter in the ciphertext is shifted backward based on the corresponding letter in the key.
- Non-alphabetical characters remain unchanged.

## Usage
1. Run the script in a **Python environment**.
2. Enter a plaintext message when prompted.
3. Enter a key for encryption.
4. View the encrypted output.
5. View the decrypted output, which should match the original plaintext.

## Example
```sh
Enter the plaintext: HELLO WORLD
Enter the Key: KEY
Encrypted: RIJVS UYVJN
Decrypted: HELLO WORLD
```

## Requirements
- **Python 3.x**

## How to Run
1. Save the script as `vigenere_cipher.py`.
2. Open a **terminal** or **command prompt**.
3. Navigate to the script's directory.
4. Run the command:
   ```sh
   python vigenere_cipher.py
   ```

## License
This project is **open-source** and free to use.



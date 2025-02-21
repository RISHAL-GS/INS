# Monoalphabetic Cipher Encryption & Decryption

## Description
This Python script implements a simple monoalphabetic substitution cipher for encrypting and decrypting messages. It replaces each letter in the plaintext with a corresponding letter from a predefined cipher alphabet.

## Features
- Encrypts plaintext using a fixed monoalphabetic cipher.
- Decrypts the encrypted text back to its original form.
- Retains non-alphabetical characters as they are.

## Encryption & Decryption Algorithm
- The script uses a predefined mapping:
  - **Plaintext Alphabet**: `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
  - **Cipher Alphabet**: `ZXCVBNMLKJHGFDSAPOIUYTREWQ`
- Each letter in the plaintext is replaced by the corresponding letter in the cipher alphabet.
- Decryption reverses the process, retrieving the original text.

## Usage
1. Run the script in a Python environment.
2. Enter a plaintext message when prompted.
3. View the encrypted output.
4. The script automatically decrypts the encrypted text and displays the original message.

## Example
```sh
Enter plaintext here: HELLO WORLD
Encrypted text: GFDDI VIDSN
Decrypted text: HELLO WORLD
```
# Requirements
- Python 3.x

## How to Run
- Save the script as mono_cipher.py.
- Open a terminal or command prompt.
- Navigate to the script's directory.
  
## Run the command:
```sh
python mono_cipher.py
```
## License
- This project is open-source and free to use.



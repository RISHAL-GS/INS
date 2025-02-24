# Caesar Cipher Encryption Script

## Description
This Python script implements a simple Caesar Cipher encryption algorithm. The Caesar Cipher is a basic encryption technique that shifts each letter in the plaintext by a fixed number of positions in the alphabet.

## How It Works
1. The script takes user input for a text string and a shift value (integer).
2. It then encrypts the text using the Caesar Cipher algorithm by shifting each letter by the given shift value.
3. The encrypted text (ciphertext) is displayed as output.
4. Non-alphabetical characters remain unchanged.

## Usage
### Running the Script
1. Run the script in a Python environment.
2. Enter the text you want to encrypt when prompted.
3. Enter a numeric shift value.
4. The encrypted text (cipher) will be displayed.

### Example
#### Input:
```
Enter text to encrypt: Hello, World!
Enter shift value: 3
```
#### Output:
```
Cipher: Khoor, Zruog!
```

## Code Explanation
- The `encrypt` function processes each character in the input string:
  - If the character is an uppercase letter (A-Z), it is shifted within the uppercase range.
  - If the character is a lowercase letter (a-z), it is shifted within the lowercase range.
  - Any other characters (such as punctuation and spaces) remain unchanged.
- The shift value wraps around the alphabet (e.g., 'Z' shifted by 1 becomes 'A').

## Requirements
- Python 3.x
- No additional libraries are required.

## Limitations
- This script only supports encryption, not decryption.
- It does not handle non-English alphabets or special character encodings.

## License
This script is open-source and free to use for educational purposes.


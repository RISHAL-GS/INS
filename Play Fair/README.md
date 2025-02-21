Playfair Cipher Encryption
Description
This Python script implements the Playfair cipher encryption algorithm. It encrypts messages using a 5x5 matrix generated from a given keyword, following Playfair cipher rules.

Features
Generates a 5x5 Playfair cipher matrix based on a key.
Processes messages to remove duplicate letters and format them into digraphs.
Encrypts messages using Playfair cipher rules.
Retains non-alphabetical characters as they are.
Encryption Algorithm
Matrix Creation
The key is converted to uppercase, and duplicate letters are removed.
The letter 'J' is replaced with 'I'.
The remaining letters of the alphabet (excluding 'J') are added to fill the matrix.
Message Processing
The message is converted to uppercase, and 'J' is replaced with 'I'.
Repeated letters in a pair are separated by 'X'.
If the message has an odd number of characters, 'X' is added at the end.
Encryption
If both letters of a pair are in the same row, each is replaced by the letter to its right (wrapping around if necessary).
If both letters are in the same column, each is replaced by the letter below it (wrapping around if necessary).
Otherwise, letters swap positions diagonally.
Usage
Run the script in a Python environment.
Enter a plaintext message when prompted.
Enter a key for matrix generation.
View the encrypted output.
Example
sh
Copy
Edit
Enter the message: HELLO WORLD
Enter the key: SECRET
Encrypted message: DMBBN VAJNF
Requirements
Python 3.x
How to Run
Save the script as playfair_cipher.py.
Open a terminal or command prompt.
Navigate to the script's directory.
Run the command:
sh
Copy
Edit
python playfair_cipher.py
License
This project is open-source and free to use.

# 🔢 Hill Cipher

This project implements the **Hill Cipher**, a polygraphic substitution cipher that uses matrix multiplication for encryption. The algorithm works by converting plaintext into numerical values and applying a key matrix transformation.

## 📜 Overview
The **Hill Cipher** is based on linear algebra and matrix operations:
- It requires a **square key matrix** (n × n).
- The **plaintext** is divided into blocks of size **n**.
- The **encryption** process involves multiplying the key matrix with the plaintext vector modulo 26.

## 🔐 Encryption Process
1. Convert plaintext into numerical values (A=0, B=1, ..., Z=25).
2. Divide the plaintext into **n-sized blocks** based on the key matrix size.
3. Multiply each block with the **key matrix**.
4. Take the result **mod 26** and convert it back to letters.

## ⚠️ Important Note on Key Matrix
- The **key matrix must be invertible modulo 26** for decryption to be possible.
- If the determinant of the key matrix **does not have a modular inverse**, a new matrix must be chosen.

## 🛠️ Features
✔ Converts **plaintext** to numerical form.  
✔ Supports **custom key matrix** input.  
✔ Ensures the **key matrix is invertible** mod 26.  
✔ Encrypts plaintext **block by block**.

## 🚀 Setup and Installation

### 📌 Prerequisites
Ensure you have the following installed:
- **Python 3.8 or later**  
- **NumPy** library for matrix operations (`pip install numpy`)

### 📥 Clone the Repository
```sh
git clone https://github.com/YourUsername/Hill-Cipher.git
cd Hil💻 How to Run
``` 
Run the script using:
``` sh
python hill_cipher.py
3```

The program will prompt for:

-Plaintext message
-Matrix size (n × n)
-Key matrix values (entered row-wise)

###📝 Example Usage
🔐 Encryption

Enter plaintext: HELLO
Enter the matrix size: 2
Enter the key matrix row-wise:
3 3
2 5
Ciphertext: ZEBB
## 🚫 Error Handling (Invalid Matrix)
`` sh
-Enter plaintext: TEST
-Enter the matrix size: 2
-Enter the key matrix row-wise:
2 4
6 8
-Invalid input: Key matrix is not invertible modulo 26. Choose a different matrix.
```
📂 File Structure
-plaintext
`` sh
Hill-Cipher/
│── hill_cipher.py   # Python script for encryption
│── README.md        # This file
```
📜 References
- Hill, Lester S. "Cryptography in an Algebraic Alphabet." The American Mathematical Monthly, 1929.
Wikipedia - Hill Cipher


### ✅ **Fixes Applied**
1. **Proper Sectioning** (Overview, Features, Setup, Running, Examples)
2. **Correct Code Blocks (` ```sh ` for shell commands)**
3. **Error Handling Example** for invalid key matrix
4. **Markdown Formatting** for readability  
5. **Added References** for more info  l-Cipher
```

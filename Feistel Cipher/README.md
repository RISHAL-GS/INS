
# 🔐 Feistel Cipher

This project implements the **Feistel Cipher**, a symmetric structure widely used in block cipher designs. The Feistel network divides plaintext into two halves and applies multiple rounds of encryption using a round function and subkeys.

## 📜 Overview
The **Feistel Cipher** is the basis for many modern encryption algorithms like **DES**. It operates by splitting plaintext into **left (L) and right (R) halves** and applying a function `F` combined with subkeys.

### 🔑 **Encryption Process**
1. Divide the plaintext into `L` (left half) and `R` (right half).
2. Apply the Feistel function `F` to `R`, then XOR with `L`.
3. Swap halves.
4. Repeat for multiple rounds.

### 🔓 **Decryption Process**
- The decryption process is identical to encryption but with subkeys applied in reverse order.

## 🛠️ Features
- Implements **multiple rounds** for increased security.
- Uses a **simple round function (F)** for demonstration.
- Supports **encryption and decryption**.

## 🚀 Setup and Installation
### 📌 Prerequisites
- Ensure you have **Python 3.8 or later** installed.

### 📥 Clone the Repository
```sh
git clone https://github.com/YourUsername/INS.git
cd "Feistel Cipher"
```

##💻 How to Run
Run the script using:

-sh
-Copy
-Edit
-python feistel_cipher.py  

#The program will prompt for:

-Plaintext to encrypt
-Number of rounds
Kwy for encryption
-📝 Example Usage
-Encryption
-vbnet
-Copy
-Edit
-Enter text to encrypt: HELLO
-Enter number of rounds: 4
-Enter key: SECRET
-Ciphertext: 9f3a2c...

##Decryption
vbnet
Copy
Edit
-Enter text to decrypt: 9f3a2c...
-Enter number of rounds: 4
-Enter key: SECRET
-Decrypted text: HELLO
📂 File Structure
nginx
Copy
Edit
Feistel Cipher/
│── feistel_cipher.py   # Python script for encryption & decryption
│── README.md           # This file

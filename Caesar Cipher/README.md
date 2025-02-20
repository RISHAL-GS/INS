# 🔐 Vigenère Cipher

This project implements the **Vigenère Cipher**, a polyalphabetic substitution cipher that enhances security by using a keyword to shift letters.

## 📜 Overview
The **Vigenère Cipher** is an improvement over the **Caesar Cipher** by using a **repeating keyword** to determine shifting values instead of a fixed shift.

### 🔑 **Encryption Formula:**
Each letter **P** in the plaintext is shifted based on the corresponding letter **K** in the keyword:
E = (P + K) % 26

### 🔓 **Decryption Formula:**
To decrypt, we reverse the shift:

P = (E - K) % 26

## 🛠️ Features
- Encrypts and decrypts messages using a **keyword-based shifting technique**.
- Supports both **uppercase and lowercase** letters.
- Preserves spaces, punctuation, and numbers.

## 🚀 Setup and Installation
### 📌 Prerequisites
Ensure you have **Python 3.8 or later** installed.

### 📥 Clone the Repository
```sh
git clone https://github.com/YourUsername/INS.git
cd "Vigenère Cipher"
```

### 💻 How to Run
Run the script using:

sh
Copy
Edit
python vigenere_cipher.py

## 📝 Example Usage
Encryption
vbnet
Copy
Edit
- Enter text to encrypt: HELLO
- Enter keyword: KEY
- Ciphertext: RIJVS
- Decryption
- vbnet
Copy
Edit
Enter text to decrypt: RIJVS
Enter keyword: KEY
Decrypted text: HELLO

## 📂 File Structure
bash
Copy
Edit
- Vigenère Cipher/
- │── vigenere_cipher.py   # Python script for encryption & decryption
1- ── README.md            # This file

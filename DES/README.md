# 🔐 Data Encryption Standard (DES) Key Generation

This project implements a **DES Key Generation** algorithm that creates pseudo-random keys using bitwise operations, random selection, and custom transformations.

## 📜 Overview

The **DES Key Generation Script** is part of the **Data Encryption Standard (DES)**, a symmetric-key algorithm for the encryption of digital data. This script generates multiple unique keys required for the encryption and decryption processes of DES.

## 🔑 Key Generation Process

1. **Input Handling:** Accepts a user-input string and converts it into an 8-bit binary representation for each character.
2. **Binary Transformation:** The binary string is split into `left` and `right` halves, and unnecessary bits are removed.
3. **Bit Manipulation:** Applies left shifts using a predefined `lt` array and combines the left and right halves.
4. **Random Bit Selection:** A random subset of bits is removed to generate the final key.
5. **Key Storage:** Stores all generated keys in a list and displays them.

## 🛠️ Features

- Generates **8 unique keys** for DES encryption and decryption.
- Utilizes **bitwise operations** and **randomization** for added complexity.
- Supports **pseudo-random key generation**, enhancing cryptographic strength.

## 🚀 Setup and Installation

### 📌 Prerequisites

Ensure you have **Python 3.8 or later** installed.

### 📥 Clone the Repository

```sh
git clone https://github.com/YourUsername/DES.git
cd "DES Key Generation"
```

### 💻 How to Run
Run the script using:
```sh
python des_key_generation.py
```
The program will prompt for:

- Input string for key generation

### 📝 Example Usage
```sh
Enter a string: hello
Key 1 = 1101000011100011100011011011010111001
Key 2 = 111000111000110111011010111001
...
Key 8 = 1100011100011011011010111001
```

📂 File Structure
```sh
DES Key Generation/
│── des_key_generation.py   # Python script for key generation
│── README.md               # This file
```



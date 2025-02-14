# Hybrid Cipher: AES-128 with Random Permutation  

## 📌 Overview  
This project implements a **Hybrid Cipher** that enhances security by combining:  

- **AES-128 encryption** (substitution-based encryption).  
- **Random permutation** (transposition to increase diffusion).  

This combination provides **strong encryption** while preventing frequency analysis and pattern-based cryptanalysis.  

---

## 🚀 Features  
✔ **AES-128 encryption** for strong security.  
✔ **Random permutation** of ciphertext blocks for added diffusion.  
✔ **Padding** to ensure compatibility with AES block size (16 bytes).  
✔ **Reversible decryption process** using the inverse permutation.  

---

## ⚙️ How It Works  

### 🔐 **Encryption Process**  
1. **AES-128 Encryption**  
   - The plaintext is **padded** to a multiple of **16 bytes**.  
   - AES-128 encrypts the padded data in **ECB mode**.  

2. **Random Permutation**  
   - A secure **random permutation** is generated.  
   - The ciphertext is **shuffled** using this permutation.  

### 🔓 **Decryption Process**  
1. **Reverse Permutation**  
   - The ciphertext is **unshuffled** using the **inverse permutation**.  

2. **AES-128 Decryption**  
   - The reordered data is **decrypted** using AES-128.  
   - Padding is removed to retrieve the **original plaintext**.  

---

## 📜 Requirements  
- **Python 3.x**  
- **PyCryptodome** library (`pip install pycryptodome`)  

---

## 💻 Usage  

### 1️⃣ **Encrypt a Message**  
Run the script:  
```sh
python hybrid_cipher.py

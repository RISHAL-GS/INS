Hybrid Cipher: AES-128 with Random Permutation
📌 Overview
This project implements a Hybrid Cipher that enhances security by combining:

AES-128 encryption (substitution-based encryption).
Random permutation (transposition to increase diffusion).
This combination provides strong encryption while preventing frequency analysis and pattern-based cryptanalysis.

🚀 Features
✔ AES-128 encryption for strong security.
✔ Random permutation of ciphertext blocks for added diffusion.
✔ Padding to ensure compatibility with AES block size (16 bytes).
✔ Reversible decryption process using the inverse permutation.

⚙️ How It Works
🔐 Encryption Process
AES-128 Encryption
The plaintext is padded to a multiple of 16 bytes.
AES-128 encrypts the padded data in ECB mode.
Random Permutation
A secure random permutation is generated.
The ciphertext is shuffled using this permutation.
🔓 Decryption Process
Reverse Permutation
The ciphertext is unshuffled using the inverse permutation.
AES-128 Decryption
The reordered data is decrypted using AES-128.
Padding is removed to retrieve the original plaintext.
📜 Requirements
Python 3.x
PyCryptodome library (pip install pycryptodome)
💻 Usage
1️⃣ Encrypt a message
sh
Copy
Edit
python hybrid_cipher.py
Enter the plaintext when prompted.
The encrypted ciphertext (Hex format) will be displayed.
2️⃣ Decrypt a message
sh
Copy
Edit
python hybrid_cipher.py
Input the Hex ciphertext when prompted.
The decrypted plaintext will be shown.
📂 File Structure
hybrid_cipher.py → Python script for encryption & decryption
README.md → Documentation
📌 Example Output
Encryption
pgsql
Copy
Edit
Enter text to encrypt: Hello, World!
Encrypted (Hex): bdb3db9c367f639be57098539778ac4856a253b70e5624c1e295a3e8c60a44fb
Decryption
vbnet
Copy
Edit
Enter ciphertext to decrypt (Hex): bdb3db9c367f639be57098539778ac4856a253b70e5624c1e295a3e8c60a44fb
Decrypted: Hello, World!
🛡 Security Advantages
✔ AES-128 ensures strong encryption and resists brute-force attacks.
✔ Random permutation prevents pattern recognition & statistical attacks.
✔ Dual-layer encryption makes cryptanalysis difficult.

📜 License
This project is licensed under the MIT License.

Feistel cipher:
# Taking input string from the user
s = input("Enter a string : ")

# Converting each character to its ASCII value and then to an 8-bit binary representation
result = "".join(format(ord(i), '08b') for i in s)
print("Result : ", result)

# Splitting the binary string into two equal halves: Left and Right
l = int(len(result)/2)
left = result[:l]  # Left half
right = result[l:]  # Right half

# Taking the key input from the user
k = input("Enter a key : ")

# Converting the key into an 8-bit binary representation
key = "".join(format(ord(i), '08b') for i in k)

# Feistel function: Applying key to the right half
s = bin(int(right, 2) + int(key, 2))  # Addition operation

# XOR operation between the modified right half and the left half
answer = bin(int(s[2:], 2) ^ int(left, 2))  

# Swapping the left and right halves after one Feistel round
newr = answer[2:]
newl = right
newr, newl = newl, newr  # Swap operation

# Second round of Feistel function
s = bin(int(newr, 2) + int(key, 2))
ans = bin(int(s[2:], 2) ^ int(newl, 2))

# Swapping again after the second round
nl = newr
nr = ans[2:]
nl, nr = nr, nl  # Swap operation

# Final ciphertext after two rounds of encryption
cipher = nl + nr

# Ensuring the cipher text length matches the original binary length
if len(cipher) != len(result):
    while len(cipher) != len(result):
        cipher = "0" + cipher  # Padding with zeros if required

print("Cipher: ", cipher)

# Converting binary ciphertext back to string (decryption)
plainText = ""
for i in range(0, len(cipher), 8):
    temp = cipher[i:i+8]  # Taking 8-bit binary chunks
    d = int(temp, 2)  # Converting binary to decimal
    plainText = plainText + chr(d)  # Converting decimal to character

print("Plaintext: ", plainText)  # Printing the decrypted text


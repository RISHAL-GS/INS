import math

# Input values
q = int(input("Enter a prime number: "))  # Prime number
a = int(input("Enter a primitive root: "))  # Primitive root

Xa = int(input("Enter the private key of A: "))  # Private key of A
Xb = int(input("Enter the private key of B: "))  # Private key of B

# Calculate public keys
Ya = pow(a, Xa, q)  # Public key of A (a^Xa % q)
Yb = pow(a, Xb, q)  # Public key of B (a^Xb % q)

print("Public key of A:", Ya)
print("Public key of B:", Yb)

# Calculate shared secret keys
Ka = pow(Yb, Xa, q)  # (Yb^Xa) % q
Kb = pow(Ya, Xb, q)  # (Ya^Xb) % q

print("Shared key for A:", Ka)
print("Shared key for B:", Kb)

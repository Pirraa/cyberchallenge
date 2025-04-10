def discrete_log(g, p, target):
    # Brute-force method to find the discrete logarithm
    for i in range(p):
        if pow(g, i, p) == target:
            return i
    return None

# Given values
p = 467
g = 2
A = 228  # public key of Alice
B = 86   # public key of Bob

# Find private key of Alice (a) and Bob (b)
a = discrete_log(g, p, A)
b = discrete_log(g, p, B)

# Calculate the shared secret
shared_secret = pow(B, a, p)  # or pow(A, b, p), both should be the same
print(f"Alice's private key (a): {a}")
print(f"Bob's private key (b): {b}")
print(f"Shared secret: {shared_secret}")

n = 2147483647
s0 = 125778740
s1 = 513146825
s2 = 1999511474

# Step 1: Solve for m using the formula
# s1 = (m * s0 + c) % n ==> c = (s1 - m * s0) % n
# We know: s2 = (m * s1 + c) % n, we substitute c from above into this equation
# so we have: s2 = (m * s1 + (s1 - m * s0) % n) % n

# Step 2: Rearrange to isolate m
# s2 = (m * s1 + (s1 - m * s0) % n) % n
# => m * (s1 - s0) = (s2 - s1) % n
# => m = (s2 - s1) * mod_inverse(s1 - s0) % n

# Calculate the modular inverse of (s1 - s0) mod n using extended Euclidean algorithm

def mod_inverse(a, n):
    # Using extended Euclidean algorithm to find the modular inverse of a mod n
    t, new_t = 0, 1
    r, new_r = n, a
    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r
    if r > 1:
        raise Exception("No modular inverse")
    if t < 0:
        t = t + n
    return t

# Calculate m
m = (s2 - s1) * mod_inverse(s1 - s0, n) % n

# Now calculate c using the formula c = (s1 - m * s0) % n
c = (s1 - m * s0) % n

print(f"m = {m}")
print(f"c = {c}")

# Step 3: Use m and c to generate the next 50 numbers in the sequence
def generate_sequence(m, c, s0, n, count=100):
    sequence = [s0]
    for _ in range(count):
        next_value = (m * sequence[-1] + c) % n
        sequence.append(next_value)
    return sequence

# Generate the next 50 numbers
next_numbers = generate_sequence(m, c, s0, n, 100)
print("Next 50 numbers in the sequence:", next_numbers)

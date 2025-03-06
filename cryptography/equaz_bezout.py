def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # Caso base: MCD(a, 0) = a, x = 1, y = 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)  # Ricorsione
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Esempio
a = 51
b = 198
gcd, x, y = extended_gcd(a, b)

print(f"Soluzione: x = {x}, y = {y}, gcd = {gcd}")

import math

def mod_inverse(a, n):
    if math.gcd(a, n) != 1:
        return None  # L'inverso non esiste se gcd(a, n) ≠ 1
    return pow(a, -1, n)  # Calcola l'inverso usando pow

# Esempio
a = 92
n = 183
inverse = mod_inverse(a, n)

if inverse:
    print(f"L'inverso di {a} modulo {n} è {inverse}")
else:
    print(f"{a} non è invertibile modulo {n}")

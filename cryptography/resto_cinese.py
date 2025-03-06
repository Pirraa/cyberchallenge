from sympy import mod_inverse

# Definizione delle congruenze
congruences = [
    (22, 27),
    (55, 59),
    (58, 61),
    (37, 68),
    (86, 91)
]

# Calcola N (prodotto di tutti i moduli)
N = 1
for _, mod in congruences:
    N *= mod

# Applica il Teorema del Resto Cinese
x = 0
for ai, mi in congruences:
    Ni = N // mi  # N_i = N / mi
    Mi = mod_inverse(Ni, mi)  # Inverso moltiplicativo modulo mi
    x += ai * Ni * Mi

# Trova x mod N
x = x % N

print(f"x ≡ {x} mod {N}")

m = 10
e = 5
n = 119

# Cifra il messaggio
c = pow(m, e, n)

print(f"Messaggio cifrato: {c}")

e = 5
phi_n = 96

# Troviamo l'inverso di e modulo phi(n)
d = pow(e, -1, phi_n)

print(f"Esponente privato d: {d}")


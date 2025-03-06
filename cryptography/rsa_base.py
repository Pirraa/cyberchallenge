from math import gcd

def inverse_mod(a, m):
    """Calcola l'inverso di a modulo m usando l'algoritmo di Euclide Esteso."""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def rsa():
    print("Benvenuto nel programma di cifratura RSA!")

    # Chiediamo p e q, i numeri primi
    while True:
        p = int(input("Inserisci il primo numero primo p: "))
        q = int(input("Inserisci il secondo numero primo q: "))
        if p <= 1 or q <= 1 or gcd(p, q) != 1:
            print("p e q devono essere numeri primi distinti! Riprova.")
        else:
            break
    
    # Calcoliamo n = p * q
    n = p * q
    print(f"n (modulo) = {n}")

    # Calcoliamo φ(n) = (p - 1) * (q - 1)
    phi_n = (p - 1) * (q - 1)
    print(f"ϕ(n) (Funzione di Eulero di n) = {phi_n}")

    # Chiediamo e, l'esponente pubblico
    while True:
        e = int(input("Inserisci l'esponente pubblico e (1 < e < ϕ(n) e gcd(e, ϕ(n)) = 1): "))
        if e <= 1 or e >= phi_n or gcd(e, phi_n) != 1:
            print(f"e deve essere coprimo di ϕ(n) e deve essere compreso tra 1 e {phi_n}. Riprova.")
        else:
            break

    # Calcoliamo d, l'esponente privato (inverso di e modulo ϕ(n))
    d = inverse_mod(e, phi_n)
    print(f"Esponente privato d = {d}")

    # Chiediamo il messaggio da cifrare (m)
    while True:
        m = int(input(f"Inserisci il messaggio da cifrare m (0 <= m < {n}): "))
        if m < 0 or m >= n:
            print(f"Il messaggio m deve essere un numero intero compreso tra 0 e {n}. Riprova.")
        else:
            break

    # Cifriamo il messaggio: c = m^e % n
    c = pow(m, e, n)
    print(f"Messaggio cifrato c = {c}")

    # Decifriamo il messaggio: m' = c^d % n
    m_decifrato = pow(c, d, n)
    print(f"Messaggio decifrato m' = {m_decifrato}")

# Eseguiamo il programma
rsa()

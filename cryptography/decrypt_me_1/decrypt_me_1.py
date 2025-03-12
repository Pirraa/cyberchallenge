import sympy

# Parametri RSA
n = 6978643725301034687
e = 65537

# Step 1: Fattorizza n
p, q = sympy.factorint(n).keys()  # p e q sono i fattori primi di n
print(f"p = {p}, q = {q}")

# Step 2: Calcola phi(n)
phi_n = (p - 1) * (q - 1)
print(f"φ(n) = {phi_n}")

# Step 3: Calcola d usando l'algoritmo di Euclide Esteso
def extended_gcd(a, b):
    # Algoritmo di Euclide Esteso
    if a == 0:
        return b, 0, 1
    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

# Calcolare l'inverso di e modulo φ(n)
g, d, _ = extended_gcd(e, phi_n)
if g != 1:
    raise ValueError("e e φ(n) non sono coprimi, quindi non è possibile calcolare la chiave privata.")
d = d % phi_n  # Assicurati che d sia positivo
print(f"d = {d}")

# Step 4: Decifra i messaggi
def decrypt(c, n, d):
    return pow(c, d, n)

# Funzione per convertire un numero decifrato in una stringa di caratteri ASCII
def int_to_ascii(num):
    message = ""
    while num > 0:
        # Ottieni l'ultimo carattere (modulo 256 per l'ASCII standard)
        message = chr(num % 256) + message
        num = num // 256  # Riduci il numero
    return message

# Lista dei cifrati (messaggi cifrati)
c = [330491619614655704, 330491619614655704, 3091954281444416978, 466972204857341594, 
     6003475009957582261, 5339981105013139679, 6596974661489421904, 2822161913993247701, 
     5547032995651184365, 3269518217593410063, 3736400100981045498, 3616150431731140245, 
     4136155834429311356, 1488012991442385800, 5547032995651184365, 4136155834429311356, 
     4971367358312153171, 5547032995651184365, 4158822776603671884, 3616150431731140245, 
     6596974661489421904, 5465781155217766773, 1488012991442385800, 5547032995651184365, 
     2822161913993247701, 6596974661489421904, 4136155834429311356, 3491402966579516587, 
     6596974661489421904, 886641009203121273, 4693728892056613413]

# Decifra i messaggi cifrati
decrypted_messages = [decrypt(c_i, n, d) for c_i in c]

# Stampa i messaggi decifrati come numeri
print("Messaggi decifrati (numeri):")
for m in decrypted_messages:
    print(m)

# Converte ogni messaggio decifrato da numero a stringa ASCII
decrypted_strings = [int_to_ascii(m) for m in decrypted_messages]

# Stampa i messaggi decifrati come stringhe, uno accanto all'altro
print("  nMessaggi decifrati (stringhe ASCII):")
print(" ".join(decrypted_strings))

import math

# Funzione per calcolare il logaritmo discreto usando l'algoritmo Baby-step Giant-step
def baby_step_giant_step(g, h, p):
    m = int(math.ceil(math.sqrt(p - 1)))  # Calcola la dimensione della ricerca

    # Baby steps: calcoliamo g^j mod p per j da 0 a m-1
    baby_steps = {}
    current = 1
    for j in range(m):
        baby_steps[current] = j
        current = (current * g) % p
    
    # Precomputiamo g^(-m) mod p (usiamo l'inverso di g^m modulo p)
    g_m = pow(g, m * (p - 2), p)  # g^(p-2) è l'inverso di g modulo p, usando il piccolo teorema di Fermat
    
    # Giant steps: calcoliamo h * g^(-m*k) mod p per k da 0 a m-1
    giant_step = h
    for k in range(m):
        if giant_step in baby_steps:
            # Se h * g^(-m*k) mod p è tra i baby steps, abbiamo trovato la soluzione
            return k * m + baby_steps[giant_step]
        giant_step = (giant_step * g_m) % p
    
    return None  # Se non troviamo una soluzione

# Parametri
p = 156822504356229435610557871928318388209  # Modulo
g = 2  # Base
h = 512  # Valore per cui trovare il logaritmo discreto

# Calcola il logaritmo discreto
result = baby_step_giant_step(g, h, p)

# Stampa il risultato
if result is not None:
    print(f"Il logaritmo discreto di {h} in base {g} modulo {p} è: {result}")
else:
    print("Non è stato possibile trovare il logaritmo discreto.")

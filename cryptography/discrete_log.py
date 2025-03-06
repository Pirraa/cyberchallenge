import sympy

# Funzione per calcolare il logaritmo discreto
def discrete_log(base, value, modulus):
    try:
        # Utilizza la funzione discrete_log di SymPy per calcolare il logaritmo discreto
        return sympy.discrete_log(modulus, value, base)
    except Exception as e:
        return f"Errore: {str(e)}"

# Parametri
p = 156822504356229435610557871928318388209  # Modulo
g = 2  # Base
x = 512  # Numero di cui trovare il logaritmo discreto

# Calcola il logaritmo discreto
result = discrete_log(g, x, p)

# Stampa il risultato
print(f"Il logaritmo discreto di {x} in base {g} modulo {p} è: {result}")

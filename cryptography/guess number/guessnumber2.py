def find_c(m, n, v0, v1):
    """
    Trova il valore di c (incremento) dato m, n, v0 e v1.
    """
    c = (v1 - m * v0) % n
    return c

def lcg_sequence(m, c, n, initial_state, num_values):
    """
    Genera una sequenza di numeri pseudocasuali usando un LCG.
    """
    sequence = [initial_state]
    current_state = initial_state

    for _ in range(num_values - 1):
        next_state = (m * current_state + c) % n
        sequence.append(next_state)
        current_state = next_state

    return sequence

# Parametri forniti
m = 2115495185
n = 2147483647
v0 = 1680462708
v1 = 77243019
num_values = 60  # Numero di valori da generare

# Trova c
c = find_c(m, n, v0, v1)
print(f"Valore di c trovato: {c}")

# Genera la sequenza
sequence = lcg_sequence(m, c, n, v0, num_values)

# Stampa la sequenza
for i, value in enumerate(sequence):
    print(f"v[{i}] = {value}")

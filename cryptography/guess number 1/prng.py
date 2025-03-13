def lcg_sequence(m, c, n, s0, num_values):
    """
    Genera una sequenza di numeri pseudocasuali usando un LCG.

    :param m: Moltiplicatore
    :param c: Incremento
    :param n: Modulo
    :param s0: Valore iniziale (seme)
    :param num_values: Numero di valori da generare
    :return: Lista contenente la sequenza generata
    """
    sequence = [s0]  # Inizia con il valore iniziale
    s_current = s0

    for _ in range(num_values - 1):
        s_next = (m * s_current + c) % n  # Calcola il prossimo valore
        sequence.append(s_next)
        s_current = s_next  # Aggiorna il valore corrente

    return sequence

# Parametri forniti
m = 1076867677
c = 1265354953
n = 2147483647
s0 = 1862611659
num_values = 54  # Numero di valori da generare

# Genera la sequenza
sequence = lcg_sequence(m, c, n, s0, num_values)

# Stampa la sequenza
for i, value in enumerate(sequence):
    print(f"v[{i}] = {value}")
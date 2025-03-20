def copy(v):
    return [[v[j][i] for i in range(len(v))] for j in range(len(v[0]))]

def transpose(v):
    return [[v[j][i] for j in range(len(v))] for i in range(len(v[0]))]

def rotate(v, k):
    k = k % len(v)
    return v[k:] + v[:k]

def decipher(C, K):
    C = copy(C)
    for _ in range(2):
        C = transpose(C)  # Inverti la trasposizione
        for i in range(len(K)):
            C[i] = rotate(C[i], -K[i])  # Inverti la rotazione
    return C

# Matrice cifrata
C = [
    ['l', 'c', '3', 'b'],
    ['?', '4', 'C', 'd'],
    ['I', '}', 'r', 'C'],
    ['S', 'T', 'm', '{']
]

# Parte nota della matrice originale
M_known = [
    ['C', 'C', 'I', 'T'],
    ['{', '?', '?', '?'],
    ['?', '?', '?', '?'],
    ['?', '?', '?', '}']
]

# Funzione per trovare la chiave K
def find_key(C, M_known):
    for k0 in range(4):
        for k1 in range(4):
            for k2 in range(4):
                for k3 in range(4):
                    K = [k0, k1, k2, k3]
                    M = decipher(C, K)
                    if M[0] == M_known[0] and M[3][3] == M_known[3][3]:
                        return K
    return None

# Trova la chiave K
K = find_key(C, M_known)
if K:
    print("Chiave trovata:", K)
    M = decipher(C, K)
    flag = "".join(["".join(row) for row in M])
    print("Flag decifrata:", flag)
else:
    print("Chiave non trovata.")
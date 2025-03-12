from Crypto.Hash import SHA3_384

def enc(plain):
    res = b''
    for c in plain:
        res += SHA3_384.new(bytes([c])).digest()[:2]
    return res.hex()

# Risultato dell'hash da confrontare
target_hash = "7b957b95daf0daf25dbf0312d87854284303dfe8f39ddfe801c117c0f01f7ccae013daf2dfe8636417c0dfe8bef3d17e5f97dfe8d878dfe85c615f97405602d6"

# Prova di forza bruta su una lista di caratteri ammissibili
import itertools

chars = "abcdefghijklmnopqrstuvwxyz0123456789{}"  # Include lettere e numeri
prefix = "CCIT{"

for length in range(1, 50):  # Prova lunghezze variabili
    for comb in itertools.product(chars, repeat=length):
        candidate = prefix + ''.join(comb) + '}'
        if enc(candidate.encode()) == target_hash:
            print(f"Flag trovata: {candidate}")
            break

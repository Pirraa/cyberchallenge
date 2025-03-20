from itertools import permutations

def unscramble(message, key):
    W = len(key)
    for _ in range(128):
        # Inverti la permutazione
        res = ""
        for j in range(0, len(message), W):
            block = message[j:j+W]
            # Crea una lista per il blocco riordinato
            original_block = [''] * W
            for k in range(W):
                original_block[key[k]] = block[k]
            res += ''.join(original_block)
        message = res

        # Inverti la rotazione e la divisione in pari/dispari
        message = message[-1:] + message[:-1]  # Ruota a destra di 1
        half = len(message) // 2
        even = message[:half]
        odd = message[half:]
        message = ''.join([even[i//2] if i % 2 == 0 else odd[i//2] for i in range(len(message))])
        message = message[-1:] + message[:-1]  # Ruota a destra di 1

    # Rimuovi i caratteri di riempimento (#)
    message = message.rstrip('#')
    return message

# Stringa scramble
scrambled = "l_4Tnb_3cnnbcg3r3slCCm4Id__gb4u}ct{0mr3sds"

# Prova tutte le permutazioni della chiave
for key in permutations(range(7)):
    key = list(key)
    try:
        unscrambled = unscramble(scrambled, key)
        if unscrambled.startswith("CCIT{") and unscrambled.endswith("}"):
            print("Chiave trovata:", key)
            print("Flag decifrata:", unscrambled)
            break
    except:
        continue
else:
    print("Chiave non trovata.")
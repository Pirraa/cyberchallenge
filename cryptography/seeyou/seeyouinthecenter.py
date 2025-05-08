import base64
import string

def encrypt(clear, key):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 128)
        enc.append(enc_c)
    return str(base64.urlsafe_b64encode("".join(enc).encode('ascii')), 'ascii')

def decrypt(enc, key):
    dec = []
    enc = str(base64.urlsafe_b64decode(enc.encode('ascii')), 'ascii')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((128 + ord(enc[i]) - ord(key_c)) % 128)
        dec.append(dec_c)
    return "".join(dec)

m = "See you later in the city center"
c = "QSldSTQ7HkpIJj9cQBY3VUhbQ01HXD9VRBVYSkE6UWRQS0NHRVE3VUQrTDE="

# Step 1: Genera tutti i possibili d = encrypt(m, k1) per k1 di 4 caratteri
k1_candidates = {}
for k1 in [''.join([a, b, c, d]) for a in string.ascii_lowercase 
                               for b in string.ascii_lowercase 
                               for c in string.ascii_lowercase 
                               for d in string.ascii_lowercase]:
    d = encrypt(m, k1)
    k1_candidates[d] = k1

# Step 2: Genera tutti i possibili d_decrypt = decrypt(c, k2) per k2 di 4 caratteri
for k2 in [''.join([a, b, c, d]) for a in string.ascii_lowercase 
                               for b in string.ascii_lowercase 
                               for c in string.ascii_lowercase 
                               for d in string.ascii_lowercase]:
    d_decrypt = decrypt(c, k2)
    if d_decrypt in k1_candidates:
        print(f"Found: k1 = {k1_candidates[d_decrypt]}, k2 = {k2}")
        print(f"KEY = {k1_candidates[d_decrypt] + k2}")
        break
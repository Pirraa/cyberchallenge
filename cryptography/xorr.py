#Una funzione in Python per fare lo xor tra due oggetti bytes può essere:

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

import binascii

# Messaggi in esadecimale
m1_hex = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf"
m2_hex = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"

# Converti da esadecimale a bytes
m1_bytes = bytes.fromhex(m1_hex)
m2_bytes = bytes.fromhex(m2_hex)

# Esegui XOR byte per byte
xor_result = xor(m1_bytes, m2_bytes)

# Converti il risultato in stringa leggibile
#flag = xor_result.decode()

print(xor_result)
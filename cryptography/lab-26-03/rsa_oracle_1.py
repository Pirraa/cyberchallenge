from Crypto.Util.number import inverse
from os import environ
import numpy as np
from sympy import factorint

# Leggi i valori
n = 5462632872421231321
e = 65537
# Fattorizza n per trovare p e q
factors = factorint(n)
p, q = list(factors.keys())
# Lista dei ciphertext (copiala da output del programma)
c = [1976851341607452414, 1185727060797389921, 4865279477060676415, 522565073012240825, 2319009610410345498, 2987443239246454428, 2003048640967507728, 5444558698548001131, 2126530202466942260, 2398743834201735944, 522565073012240825, 1809409027298810762, 348932351439576604, 5186567008737312530, 5177981167233311718, 434438206781198552, 2398743834201735944, 2023948732050315870, 2843405373984514327, 1191313636729270273]

# Calcola phi(n)
phi = (p - 1) * (q - 1)

# Calcola d
d = inverse(e, phi)

# Decripta ogni blocco
m = [pow(x, d, n) for x in c]

# Ricostruisci il flag
flag = ''.join(chr(x) for x in m)

print("[+] Flag decifrato:", flag)

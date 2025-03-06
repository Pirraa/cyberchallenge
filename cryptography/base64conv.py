import base64  

# Prima parte: decodifica da base64  
b64_string = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
decoded_part1 = base64.b64decode(b64_string).decode()

# Seconda parte: conversione del numero in bytes (big endian)
num = 664813035583918006462745898431981286737635929725
decoded_part2 = num.to_bytes((num.bit_length() + 7) // 8, 'big').decode()

# Flag completa
flag = decoded_part1 + decoded_part2
print(flag)

#In Python per convertire un oggetto bytes in un oggetto int è conveniente utilizzare la funzione int.from_bytes(b, endianness), 
#ove b è il nostro oggetto bytes, mentre endianness è una stringa 'big' oppure 'little'

#Per convertire un intero z in bytes puoi usare invece la funzione (z).to_bytes(n, endianness):
#n indica il numero di bytes da utilizzare per la conversione, seguendo l'ordine dato da endianness.

#!/usr/bin/env python3
#from base64 import b64decode
#s = 'aGVubG8gOik='
#print(b64decode(s))
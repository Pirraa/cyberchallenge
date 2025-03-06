from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import binascii

# Chiave in formato hex
key = bytes.fromhex('386282451f971435')

# Testo in chiaro
plaintext = 'La lunghezza di questa frase non è divisibile per 8'

# Padding x923
padded_data = pad(plaintext.encode(), DES.block_size, style='x923')

# Inizializzazione del vettore di inizializzazione (IV) (viene generato randomicamente per CBC)
iv = get_random_bytes(DES.block_size)

# Creazione dell'oggetto DES con modalità CBC
cipher = DES.new(key, DES.MODE_CBC, iv)

# Cifrazione
ciphertext = cipher.encrypt(padded_data)

# Stampa del risultato in esadecimale
print(f'IV (hex): {binascii.hexlify(iv).decode()}')
print(f'Ciphertext (hex): {binascii.hexlify(ciphertext).decode()}')

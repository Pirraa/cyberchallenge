from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

# Chiave e plaintext
key = bytes.fromhex('06d6a93d5c6578b3f142e812cd4882c864b4866a4d68e30accb962ab81ceef46')
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'

# Padding PKCS7
padded_data = pad(plaintext.encode(), AES.block_size)

# Generazione di un IV casuale
iv = get_random_bytes(AES.block_size)

# Inizializzazione dell'oggetto AES in modalità CFB (segmento = 24 byte)
cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=24)

# Cifrazione
ciphertext = cipher.encrypt(padded_data)

# Stampa del risultato in esadecimale
print(f'Ciphertext (hex): {ciphertext.hex()}')
print(f'IV (hex): {iv.hex()}')

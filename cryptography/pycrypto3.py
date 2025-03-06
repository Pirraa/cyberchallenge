from Crypto.Cipher import ChaCha20
from Crypto.Util.Padding import unpad
import binascii

# Dati forniti
key = bytes.fromhex('462b913ec959324b0e9cf1f0c19a76ac1fd6fe21544d3739d2db8da74b9cd5dc')
ciphertext = bytes.fromhex('6c7b280a5811cf884c5cd52bf2e181326370c2692aeea690d28db1be')
nonce = bytes.fromhex('0266f5d068ccf139')

# Inizializzazione dell'oggetto ChaCha20 con la chiave e il nonce
cipher = ChaCha20.new(key=key, nonce=nonce)

# Decifrazione
plaintext = cipher.decrypt(ciphertext)

# Stampa del testo in chiaro (ASCII)
print(f'Plaintext (ASCII): {plaintext.decode("utf-8")}')

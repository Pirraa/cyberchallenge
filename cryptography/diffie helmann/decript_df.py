from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

# Parametri del protocollo Diffie-Hellman
p = 116380985491824090325129844789112286332083391265895152129465014443746791080270094908306173356948049602080367201186496952521629999955473411222999072948126828141591409522231171600394707782838433305822081083182310906651241994160453341205893238986532718941534006395046983218100076390117181064616415622747127920363
g = 2  # Generatore scelto
A = int("998959a77a67f81bda8500e660359795cc630582e165752255c5ebe234e17496a7e83f9cdc3f29de91cdf49af64ce98a26201310f0d6d935741ae215a8dbf8c1419da36474f85502fc9f0cb23d149f66f98f7051e369d5f721355e9b610a77e3fac5dc70af86ce21eb3e9abc442593515fa5c86573c8da5021698dd41e60e512", 16)  # La chiave pubblica di Alice (in esadecimale)

# La tua chiave privata (scegli un numero segreto)
a = 123456789  # Sostituisci con la tua chiave privata

# Calcola il segreto condiviso S
S = pow(A, a, p)
print(f"Il segreto condiviso S è: {S}")

# Derivazione della chiave AES tramite PBKDF2 con il segreto condiviso
salt = b"saltsalt"  # Un salt fisso, in un caso reale usa un salt casuale
iterations = 100000
key_length = 32  # per AES-256

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=key_length,
    salt=salt,
    iterations=iterations,
    backend=default_backend()
)

# Deriva la chiave AES dal segreto condiviso
key = kdf.derive(str(S).encode())  # Deriva la chiave AES
print(f"Chiave AES derivata: {key.hex()}")

# IV fornito da Alice (in esadecimale)
iv = bytes.fromhex("32f1526815d15e5c604c78e53dbbedff")

# Messaggio cifrato fornito da Alice (in esadecimale)
msg = bytes.fromhex("c2debdc528f61c74166668a286c31e2237045c519d21666d0c6505a419f6148cc95ca91a65476a714060d04f0c2acdf3ac3d5e7b972f68d9e33d785cd54c5374")

# Decrypt il messaggio usando AES-CBC
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
decryptor = cipher.decryptor()

# Decrypt the message and unpad
decrypted_msg = decryptor.update(msg) + decryptor.finalize()

# Aggiungi la rimozione del padding (se usato)
unpadder = padding.PKCS7(128).unpadder()
decrypted_msg_unpadded = unpadder.update(decrypted_msg) + unpadder.finalize()

# Decodifica in UTF-8 (se il messaggio è in formato testo)
try:
    decrypted_msg_str = decrypted_msg_unpadded.decode("utf-8")
    print(f"Messaggio decriptato: {decrypted_msg_str}")
except UnicodeDecodeError:
    print("Errore nella decodifica del messaggio: potrebbe non essere testo.")
    # In alternativa, salva i dati decriptati come file binario
    with open("decrypted_message.bin", "wb") as f:
        f.write(decrypted_msg_unpadded)
    print("Messaggio decriptato salvato come 'decrypted_message.bin'.")

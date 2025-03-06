from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

messaggio = "Questo è un messaggio segreto!".encode("utf-8")

chiave_aes = b"1chiave_segreta1"

key_alice = RSA.generate(2048)
private_key_alice = key_alice.export_key()
public_key_alice = key_alice.publickey().export_key()

key_bob = RSA.generate(2048)
private_key_bob = key_bob.export_key()
public_key_bob = key_bob.publickey().export_key()

hash_msg = SHA256.new(messaggio)
# Alice firma l'hash del messaggio usando la propria chiave PRIVATA
msg_firmato = PKCS1_v1_5.new(key_alice).sign(hash_msg)

print(f"Hash SHA-256 messaggio per Bob:\n{hash_msg.digest().hex()}\n")
print(f"Messaggio firmato per Bob:\n{msg_firmato.hex()}\n")

# Alice cifra la signature con AES usando la chiave simmetrica
cipher_alice = AES.new(chiave_aes, AES.MODE_CBC)
firma_cifrata = cipher_alice.encrypt(msg_firmato)

print(f"Firma cifrata in AES per Bob:\n{firma_cifrata.hex()}\n")

# Alice trasmette a Bob il messaggio in chiaro (messaggio)
# e la firma cifrata (firma_cifrata)

# Bob decifra la firma usando la chiave simmetrica
cipher_bob = AES.new(chiave_aes, AES.MODE_CBC)
msg_decifrato = cipher_bob.decrypt(firma_cifrata)

# Bob calcola l'hash del messaggio in chiaro
hash_msg_bob = SHA256.new(messaggio)
print(f"Hash SHA-256 calcolato da Bob:\n{hash_msg_bob.digest().hex()}\n")

# Bob verifica la firma inviatagli da Alice usando la chiave pubblica di Alice
try:
    pub_key_alice = RSA.import_key(public_key_alice)
    PKCS1_v1_5.new(pub_key_alice).verify(hash_msg_bob, msg_decifrato)
    print(
        "La firma del messaggio è valida, quindi è verificato che il mittente è Alice.\n"
    )
except (ValueError, TypeError):
    print("La firma non è valida, non posso verificare che il mittente sia Alice.\n")

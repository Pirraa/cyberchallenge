from pwn import xor

# Quello che ottieni dal programma (stampa iniziale)
output = input("Inserisci l'IV+ciphertext esadecimale: ").strip()
data = bytes.fromhex(output)

iv_original = data[:16]
ciphertext = data[16:]

# Comando originale e comando target (devono essere entrambi 16 byte!)
P1_original = b"print_helloworld"
P1_target   = b"print_the_flag!!"

# Calcolo il nuovo IV che decritterà in "print_the_flag!!"
iv_new = xor(iv_original, xor(P1_original, P1_target))

# Costruisco il nuovo ciphertext (solo IV cambia)
payload = iv_new + ciphertext
print("\n>> Payload da inviare (hex):")
print(payload.hex())

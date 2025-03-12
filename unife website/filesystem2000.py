import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time

class X:
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.char

class Y:
    def __init__(self):
        # Lista dei valori che saranno trasformati in caratteri
        self.chars = np.array([50+22, 202//((4*2)//4), 108, 54*2, 1110//(2*(3+2)), 2*22, 64//((8//8)+1), 87, 1110//(2*(3+2)), 110+2+2, ((104-100)*2)+100, 1*10*10, 3*11])

    def get_key(self):
        # Usa una chiave fissa che abbia esattamente 16 byte per AES-128
        key = b'MyFixedKey12345'  # 15 byte
        key = key.ljust(16, b'  0')  # Aggiungi un byte '  0' per fare in modo che la lunghezza sia 16 byte
        return key

    def get_cock(self):
        cock = []
        # Crea una lista di oggetti X dai caratteri generati dai valori numerici
        for char_code in self.chars:
            cock.append(X(chr(int(char_code))))  # Converti il valore in intero prima di passarlo a chr
        return cock

    def encrypt_text(self, text, key):
        # Cifra il testo usando AES in modalità ECB con padding
        cipher = AES.new(key, AES.MODE_ECB)
        padded_text = pad(text.encode(), AES.block_size)  # Aggiunge padding
        encrypted_text = cipher.encrypt(padded_text)
        return encrypted_text

    def decrypt_text(self, encrypted_data, key):
        # Decripta il testo usando la stessa chiave e modalità AES
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)  # Rimuove il padding
        return decrypted_data.decode()

    def write_encrypted_to_file(self, encrypted_data):
        # Scrive i dati cifrati nel file Flag.txt
        with open("Flag.txt", "wb") as f:
            f.write(encrypted_data)

    def write_decrypted_to_file(self, decrypted_data):
        # Scrive i dati decriptati in un altro file (DecryptedFlag.txt)
        with open("DecryptedFlag.txt", "w") as f:
            f.write(decrypted_data)

    def exc(self):
        # Funzione per criptare il testo e salvarlo in un file
        key = self.get_key()
        cock = self.get_cock()
        encrypted_text = ''
        for lilCock in cock:
            encrypted_text += str(lilCock)

        encrypted_data = self.encrypt_text(encrypted_text, key)
        self.write_encrypted_to_file(encrypted_data)

    def exc_decrypt(self):
        # Funzione per decriptare il file Flag.txt
        with open("Flag.txt", "rb") as f:
            encrypted_data = f.read()  # Leggi il file cifrato

        key = self.get_key()  # Usa lo stesso timestamp per ottenere la chiave
        decrypted_text = self.decrypt_text(encrypted_data, key)
        self.write_decrypted_to_file(decrypted_text)  # Scrivi il testo decriptato nel file DecryptedFlag.txt


# Esegui la criptazione e salvataggio nel file Flag.txt
y = Y()
y.exc()

# Esegui la decriptazione e salvataggio nel file DecryptedFlag.txt
y.exc_decrypt()

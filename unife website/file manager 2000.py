import numpy as np
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import time

class X:
    def __init__(self, char):
        self.char = char

    def __str__(self):
        return self.char

class Y:
    def __init__(self):
        self.chars = np.array([50+22, 202/((4*2)/4), 108, 54*2, 1110/(2*(3+2)), 2*22, 64/((8/8)+1), 87, 1110/(2*(3+2)), 110+2+2, ((104-100)*2)+100, 1*10*10, 3*11])

    def get_key(self):
        timestamp = str(time.time())  # Utilizziamo il timestamp attuale come base per la chiave
        # Trasformiamo il timestamp in una chiave di 16 byte (128 bit)
        key = timestamp.encode('utf-8')
        key = key[:16]  # Assicuriamoci che la chiave sia lunga 16 byte
        return key

    def get_cock(self):
        cock = []
        for char_code in self.chars:
            cock.append(X(chr(char_code)))
        return cock

    def encrypt_text(self, text, key):
        cipher = AES.new(key, AES.MODE_ECB)
        padded_text = pad(text.encode(), AES.block_size)
        encrypted_text = cipher.encrypt(padded_text)
        return encrypted_text

    def exc(self):
        key = self.get_key()
        cock = self.get_cock()
        encrypted_text = ''
        for lilCock in cock:
            encrypted_text += str(lilCock)

        encrypted_data = self.encrypt_text(encrypted_text, key)
        with open("Flag.txt", "wb") as f:
            f.write(encrypted_data)

y = Y()
y.exc()
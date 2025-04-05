import os
from Crypto.Cipher import AES
import signal

TIMEOUT = 100
FLAG = os.environ["FLAG"]
key = os.urandom(16)

allowed_commands = ["print_helloworld"]


def handle():
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    command_enc = cipher.encrypt(b"print_helloworld")
    print(iv.hex() + command_enc.hex())

    print("Flip me!!")

    ciphertext = bytes.fromhex(input("Encrypted command (hex): "))
    iv, command_enc = ciphertext[:16], ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    command = cipher.decrypt(command_enc)
    if command == b"print_helloworld":
        print("Hello World!!!")
    elif command == b"print_the_flag!!":
        print(FLAG)
    else:
        print("Invalid command")


if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()

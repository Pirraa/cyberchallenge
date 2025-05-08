from pwn import *
import re

# Connessione
conn = remote("piecewise.challs.cyberchallenge.it", 9110)

while True:
    try:
        line = conn.recvline(timeout=5).decode().strip()
    except EOFError:
        print("[*] Connessione chiusa dal server.")
        break

    print(f"[SERVER] {line}")

    # Caso 1: invio di un numero (con bit + endian)
    number_match = re.search(r"number (\d+) as a (\d+)-bit (big|little)-endian", line)
    if number_match:
        num = int(number_match.group(1))
        num_bits = int(number_match.group(2))
        endian = number_match.group(3)
        num_bytes = num_bits // 8
        byteorder = "big" if endian == "big" else "little"
        payload = num.to_bytes(num_bytes, byteorder=byteorder)
        print(f"[→] Inviando {num} come {num_bytes} byte in {byteorder}-endian: {payload.hex()}")
        conn.send(payload)
        continue

    # Caso 2: invio di un singolo byte specifico (es. byte 10)
    byte_match = re.search(r"just the byte (\d+)", line)
    if byte_match:
        byte_val = int(byte_match.group(1))
        print(f"[→] Inviando il byte: {byte_val} (0x{byte_val:02x})")
        conn.send(byte_val.to_bytes(1, byteorder="big"))
        continue

    # Caso 3: output finale o altro
    elif line:
        print(f"[Output] {line}")


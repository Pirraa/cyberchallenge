from pwn import *

l = listen(54321)
conn = l.wait_for_connection()

sh = process("/bin/bash")

while True:
    line = conn.recv()  # Non facciamo la decode, perchè a sh.sendline
    if line:  # dobbiamo mandare dei bytes (non una stringa)
        sh.sendline(line)
        output = sh.recv(timeout=3)  # Anche qui non facciamo la encode,
        if output:  # inviamo al client direttamente dei bytes
            conn.send(output)
        else:
            conn.send(b"(no output)")

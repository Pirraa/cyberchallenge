from pwn import *

conn = remote("localhost", 54321)

while True:
    i = input("Comando: ")
    tosend = i.encode("utf-8")
    conn.send(tosend)
    line = conn.recv().decode("utf-8")
    print(line)

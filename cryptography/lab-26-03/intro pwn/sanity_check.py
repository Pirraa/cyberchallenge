from pwn import remote

conn=remote('ctf.unife.it',8002)

print(conn.recvline().decode())
print(conn.recvline().decode())
print(conn.recvline().decode())
conn.sendline(b'ciao')
print(conn.recvline().decode())
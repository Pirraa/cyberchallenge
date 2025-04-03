import string
from pwn import remote

conn= remote('ctf.unife.it', 8003)


def caesar(s, k = 13, decode = False, *, memo={}):
    if decode: k = 26 - k
    k = k % 26
    table = memo.get(k)
    if table is None:
        table = memo[k] = str.maketrans(
            string.ascii_uppercase + string.ascii_lowercase,
            string.ascii_uppercase[k:] + string.ascii_uppercase[:k] +
            string.ascii_lowercase[k:] + string.ascii_lowercase[:k])
    return s.translate(table)

for i in range(4):
    line = conn.recvline(timeout=1).decode()
    print(line)
t3 = conn.recvline().decode().strip()
for i in range(26):
    c3 = caesar(t3, i, True)
    c3 = "unief{" + str(c3) + "}"
    conn.sendline(c3.encode())
    if conn.recvline().decode().startswith("That's right"):
        print(c3)
        break
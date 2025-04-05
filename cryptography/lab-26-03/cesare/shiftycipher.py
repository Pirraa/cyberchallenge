from pwn import remote

conn= remote('ctf.unife.it', 8003)

def decrypt(ciphertext, key):
    decrypted = ""
    letters="abcdefghijklmnopqrstuvwxyz"
    for char in ciphertext:
        if char.isalpha():
            position=letters.find(char)
            new_pos=(position - key) % 26
            new_char=letters[new_pos]
            decrypted += new_char
        else:
            decrypted += char
    return decrypted

for i in range(4):
    line = conn.recvline(timeout=1).decode()
    print(line)

letters=[]
for i in range(26):
    letters.append(chr(i+65))
    
while True:
    line = conn.recvline(timeout=1).decode()
    print(line)
    #words=line.split()
    for key in range (26):
        decrypted=decrypt(line, key)
        print(decrypted)
        if 'unife' in decrypted or 'flags' in decrypted:
            print(decrypted)
            conn.sendline(str(decrypted).encode())
            break 
    line=conn.recvline(timeout=1).decode()
    print(line)
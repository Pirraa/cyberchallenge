from pwn import remote
conn = remote('ctf.unife.it', 8001)


line = conn.recvline(timeout=1).decode()
print(line)
line = conn.recvline(timeout=1).decode()
print(line)
line = conn.recvline(timeout=1).decode()
print(line)

while True:
    line = conn.recvline(timeout=1).decode()
    print(line)
    numbers = line.split()
    print(numbers)
    a=numbers[0]
    b=numbers[2]
    op=numbers[1]
    if op == '+':
        result = int(numbers[0]) + int(numbers[2])
    elif op == '*':
        result = int(numbers[0]) * int(numbers[2])
    elif op == '/':
        result = int(numbers[0]) / int(numbers[2])
    elif op == '-':
        result = int(numbers[0]) - int(numbers[2])
    elif op == '%':
        result = int(numbers[0]) % int(numbers[2])
    elif op == '^':
        result = int(numbers[0]) ** int(numbers[2])
    elif op == '//':
        result = int(numbers[0]) // int(numbers[2])
    conn.sendline(str(result).encode())
    line=conn.recvline(timeout=1).decode()
    print(line)
    if('unife' in line):
        print(line)
        break

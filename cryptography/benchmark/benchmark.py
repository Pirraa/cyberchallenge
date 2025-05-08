""" CR_1.06 - Benchmark """


# Import
from pwn import *


# Connection
host = "benchmark.challs.cyberchallenge.it"
port = 9031

connection = remote(host, port)


# Initializations
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{!?_}'
optimal_flag = ''
try_flag = ''
found = False


# Brute-force loop
while (found == False):
    max = 0
    try_flag = optimal_flag
    for char in alphabet:
        try_flag += char

        connection.sendline(try_flag.encode())
        print(try_flag)

        output = connection.recvline_contains((b'1',b'2',b'3',b'4',b'5',b'6',b'7',b'8',b'9',b'0'),timeout=0.5)
        print(output.decode())

        value = int.from_bytes(output)

        if value > max:
            max = value
            optimal_flag = try_flag

        try_flag = try_flag[:-1]

    if optimal_flag[-1] == '}':
        found == True
        
print('The flag is: ' + optimal_flag)

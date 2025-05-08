targets = [
    84, 195, 290, 395, 479, 580, 694, 746, 862, 963, 1058, 1163, 1216, 1311,
    1415, 1500, 1609, 1706, 1784, 1879, 1995, 2043, 2138, 2252, 2303, 2370,
    2487, 2569, 2684, 2785, 2880, 2980, 3029, 3147, 3252, 3362, 3463
]

flag_chars = [chr(targets[0])]
for i in range(1, len(targets)):
    diff = targets[i] - targets[i - 1]
    flag_chars.append(chr(diff))

flag = ''.join(flag_chars)
print(f"CTF{{{flag}}}")

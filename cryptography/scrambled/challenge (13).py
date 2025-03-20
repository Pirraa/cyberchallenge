#!/bin/env python3

import random

def scramble(message, key):
    W = len(key)
    while len(message) % (2*W):
        message += "#"

    for _ in range(128):
        message = message[1:] + message[:1]
        message = message[0::2] + message[1::2]
        message = message[1:] + message[:1]
        res = ""
        for j in range(0, len(message), W):
            for k in range(W):
                res += message[j:j+W][key[k]]
        message = res

    return message


def unscramble(message, key):
    # TODO Write decrypt function before the CTF
    pass

flag = "CCIT{write_flag_here_before_the_ctf}"
key = list(range(7))
random.shuffle(key)
scrambled = scramble(flag, key)

print(scrambled)
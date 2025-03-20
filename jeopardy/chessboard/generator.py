#!/bin/env python3

from secret import FLAG, K

assert(len(K) == 4)

M = [list(FLAG[i:i+4]) for i in range(0, len(FLAG), 4)]

def copy(v):
    return [[v[j][i] for i in range(len(v))] for j in range(len(v[0]))] 

def transpose(v):
    return [[v[j][i] for j in range(len(v))] for i in range(len(v[0]))] 

def rotate(v, k):
    k = k % len(v)
    return v[k:] + v[:k]

def cipher(M, K):
    M = copy(M)
    for _ in range(2):
        for i in range(len(K)):
            M[i] = rotate(M[i], K[i])
        M = transpose(M)
    return M

C = cipher(M, K)

for c in C:
    print("".join(c))

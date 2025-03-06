#!/bin/env python3

import sys

# Se vuoi leggere/scrivere da file decommenta qua
# fin = open("input.txt", "r")  # File di input fornito dalla piattaforma
# fout = open("output.txt", "w")  # File di output fornito dalla piattaforma

# Se vuoi leggere/scrivere da linea di comando decommenta qua
fin = sys.stdin  # File di input fornito dalla piattaforma
fout = sys.stdout  # File di output fornito dalla piattaforma


def sanitize(words, banned):
    # SCRIVI QUA IL TUO CODICE
    return []

N, M = map(int, fin.readline().strip().split())

words = []
banned = []

for _ in range(M):
    banned.append(fin.readline().strip())

for _ in range(N):
    words.append(fin.readline().strip())

ans = sanitize(words, banned)

for a in ans:
    print(a)
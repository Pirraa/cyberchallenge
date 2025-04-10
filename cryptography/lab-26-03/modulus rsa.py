import os
import signal
from Crypto.Util.number import getPrime
TIMEOUT = 100
FLAG = os.environ["FLAG"]


def handle():
    p = getPrime(1024)
    q = getPrime(1024)
    n = p*q
    e = 65537

    print("Tell me a number")
    m = int(input())
    if m < 0 or m >= n:
        print("Don't try to fool me")
        exit()
    c = pow(m, e, n)
    print(c)

    print("Tell me another number")
    m = int(input())
    if m < 0 or m >= n:
        print("Don't try to fool me")
        exit()
    c = pow(m, e, n)
    print(c)

    print("Tell me n")
    guess = int(input())
    if guess == n:
        print("Good job")
        print(FLAG)
    else:
        print("Guess harder")


if __name__ == "__main__":
    signal.alarm(TIMEOUT)
    handle()

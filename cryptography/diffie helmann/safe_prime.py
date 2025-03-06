from Crypto.Util import number

# Funzione per generare un safe prime
def generate_safe_prime(bits):
    while True:
        # Genera un primo candidato
        p = number.getPrime(bits)
        # Verifica se (p-1)//2 è primo
        q = (p - 1) // 2
        if number.isPrime(q):
            return p

# Genera un safe prime di almeno 1024 bit
safe_prime = generate_safe_prime(1024)
print(f"Safe Prime: {safe_prime}")

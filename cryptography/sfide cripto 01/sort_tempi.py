# Lista dei caratteri e i relativi cicli di clock
char_cycles = {
    'a': 208,
    'b': 239,
    'c': 14,
    'd': 45,
    'e': 76,
    'f': 107,
    'g': 138,
    'h': 169,
    'i': 200,
    'j': 231,
    'k': 6,
    'l': 37,
    'm': 68,
    'n': 99,
    'o': 130,
    'p': 161,
    'q': 192,
    'r': 223,
    's': 254,
    't': 29,
    'u': 60,
    'w': 122,
    'x': 153,
    'y': 184,
    'z': 215
}

# Ordina i caratteri in base ai cicli di clock
sorted_chars = sorted(char_cycles.items(), key=lambda x: x[1])

# Estrai solo i caratteri ordinati
sorted_password = ''.join([char for char, _ in sorted_chars])

# Stampa la password ordinata
print("Password ordinata:", sorted_password)

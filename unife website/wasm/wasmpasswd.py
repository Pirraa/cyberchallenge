# Funzione per convertire valori esadecimali in decimali
def hex_to_decimal(hex_string):
    # Divido la stringa esadecimale in valori separati da spazi
    hex_values = hex_string.split()
    
    # Lista per memorizzare i valori decimali
    decimal_values = []
    
    # Converte ogni valore esadecimale in decimale
    for hex_value in hex_values:
        try:
            decimal_values.append(int(hex_value, 16))  # Convertiamo da esadecimale a decimale
        except ValueError:
            # Se il valore non è un esadecimale valido, saltiamo
            continue
    
    return decimal_values

# Funzione per convertire valori decimali in caratteri ASCII
def decimal_to_ascii(decimal_values):
    # Lista per memorizzare i caratteri ASCII
    ascii_chars = []
    
    # Converte ogni numero decimale nel carattere ASCII corrispondente
    for decimal in decimal_values:
        try:
            ascii_chars.append(chr(decimal))  # Convertiamo il valore decimale in carattere ASCII
        except ValueError:
            # Se non è un valore valido, saltiamo
            continue
    
    return ''.join(ascii_chars)

# La stringa esadecimale che vuoi convertire
hex_string = "0a b8 0b 01 50 0c 01 19 0b 19 19 19 05 09 0b 19 0a 0a 19 19 19 03 0a 07 01 09 0b 18 09 06 0b 0b 06 19 19 19 19 19 19 0e 19 0b 0d 19 19 19 0d 02 09 0e 09 0e 0e 0c 13 13 09 0c 0c 0c 10 0f 04 0f 09 10 10 10 12 11 11 09 12 12 12 1a 1a 1a 1a 1a 1a 1a 09 14 17 17 09 14 14 14 16 15 15 09 16 16 16"

# 1. Converte da esadecimale a decimale
decimal_values = hex_to_decimal(hex_string)

# 2. Converte da decimale a caratteri ASCII
ascii_string = decimal_to_ascii(decimal_values)

# Stampa i risultati
print("Valori decimali:", decimal_values)
print("Stringa ASCII risultante:", ascii_string)

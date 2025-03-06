def ascii_to_chars(ascii_values):
    return ''.join(chr(num) for num in ascii_values)
#la funzione inversa è ord() che restituisce il valore ASCII di un carattere
# Esempio di utilizzo
ascii_values=[102, 108, 97, 103, 123, 117, 103, 104, 95, 78, 117, 109, 66, 51, 114, 53, 95, 52, 49, 114, 51, 52, 100, 121, 125]
text = ascii_to_chars(ascii_values)
print(text)  # Output: Hello World!

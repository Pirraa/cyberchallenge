diz_freq = {}

with open("testo.txt", "rt") as file_input:
    for linea in file_input:  # Per ogni riga di testo nel file
        for carattere in linea:  # Per ogni carattere nella riga di testo
            # Se il carattere non è fra le chiavi del dizionario...
            if carattere not in diz_freq:
                diz_freq[carattere] = 1  # ...lo aggiungo con valore 1
            # Altrimenti...
            else:
                diz_freq[carattere] += 1  # ...ne incremento il valore di 1


print(f"freq_dict: {diz_freq}\n\n")

diz_freq_ordinato = dict(sorted(diz_freq.items(), key=lambda x: x[1], reverse=True))
print(f"freq_dict ordinato: {diz_freq_ordinato}")

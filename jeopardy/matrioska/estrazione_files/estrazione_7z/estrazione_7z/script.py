# Funzione per estrarre la parte ASCII da un dump esadecimale
def estrai_ascii_da_dumper(file_path):
    with open(file_path, 'r') as file:
        result = []
        
        for line in file:
            # Separiamo la parte esadecimale da quella ASCII
            # Le righe sono strutturate come: "00000000: fd37 7a58 ...  .7zXZ......F..!"
            parts = line.strip().split('  ')
            
            if len(parts) > 1:
                # Prendiamo la parte ASCII (dopo l'ultimo spazio)
                ascii_part = parts[1]
                # Aggiungiamo la parte ASCII al risultato
                result.append(ascii_part)
        
        # Uniamo tutte le parti ASCII e le restituiamo
        return ''.join(result)

# Percorso del file di input
file_path = 'oFalHuG5P6C7ROUo_decoded'

# Chiamata della funzione
ascii_output = estrai_ascii_da_dumper(file_path)

# Stampa del risultato finale
# Scrivi l'output su un file
with open('output', 'w') as output_file:
    output_file.write(ascii_output)


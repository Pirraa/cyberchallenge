def check_strings(file_path):
    # Legge il contenuto del file
    with open(file_path, 'r') as f:
        lines = f.read().splitlines()
    
    # Prima riga: numeri N e M
    N, M = map(int, lines[0].split())
    
    # Prossime M righe: parole bannate
    banned_words = set(lines[1:M+1])
    
    # Prossime N righe: stringhe di input
    input_strings = lines[M+1:M+1+N]
    
    # Risultati
    results = []
    for string in input_strings:
        if any(banned_word in string for banned_word in banned_words):
            results.append("BANNED")
        else:
            results.append("SAFE")
    
    # Stampa i risultati
    for result in results:
        print(result)

# Esempio di utilizzo
file_path = "input/input1.txt"  # Specificare il percorso del file
check_strings(file_path)

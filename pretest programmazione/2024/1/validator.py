import os

def process_input(input_file_path):
    """Processa un singolo file di input e restituisce i risultati."""
    with open(input_file_path, 'r') as file:
        lines = file.read().splitlines()
    
    # Leggi il numero di stringhe (N) e parole bannate (M)
    N, M = map(int, lines[0].split())
    
    # Leggi le parole bannate
    banned_words = set(lines[1:M+1])
    
    # Leggi le stringhe da verificare
    input_strings = lines[M+1:]
    
    # Risultati per ogni stringa
    results = []
    for string in input_strings:
        if any(banned_word in string for banned_word in banned_words):
            results.append("BANNED")
        else:
            results.append("SAFE")
    return results

def validate_results(input_dir, output_dir):
    """Confronta i risultati generati con quelli attesi."""
    # Elenca tutti i file di input e output
    input_files = sorted([f for f in os.listdir(input_dir) if f.startswith('input') and f.endswith('.txt')])
    output_files = sorted([f for f in os.listdir(output_dir) if f.startswith('output') and f.endswith('.txt')])
    
    if len(input_files) != len(output_files):
        print("Numero di file di input e output non corrispondono.")
        return
    
    for input_file, output_file in zip(input_files, output_files):
        input_path = os.path.join(input_dir, input_file)
        output_path = os.path.join(output_dir, output_file)
        
        # Processa il file di input
        results = process_input(input_path)
        
        # Leggi il file di output atteso
        with open(output_path, 'r') as file:
            expected_results = file.read().splitlines()
        
        # Confronta i risultati
        if results == expected_results:
            print(f"{input_file} -> {output_file}: CORRETTO")
        else:
            print(f"{input_file} -> {output_file}: ERRATO")
            print("Risultati generati:")
            print(results)
            print("Risultati attesi:")
            print(expected_results)

# Esempio di utilizzo
input_directory = "input"  # Percorso della cartella con i file di input
output_directory = "output"  # Percorso della cartella con i file di output
validate_results(input_directory, output_directory)

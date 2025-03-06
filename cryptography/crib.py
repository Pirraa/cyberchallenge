import subprocess

# Percorso del file output.txt
file_path = "output.txt"

# Comando per eseguire MTP
try:
    result = subprocess.run(["mtp", file_path], capture_output=True, text=True, check=True)
    
    # Stampa il risultato della decodifica
    print("Decodifica completata:\n")
    print(result.stdout)

except FileNotFoundError:
    print("Errore: il comando 'mtp' non è installato o non è trovato nel PATH.")
except subprocess.CalledProcessError as e:
    print(f"Errore durante l'esecuzione di mtp: {e}")

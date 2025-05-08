import subprocess
import re

# Avvia il processo
process = subprocess.Popen(
    ["./esercizio5"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

# Legge una riga dall'output
line = process.stdout.readline().strip()
print("Domanda:", line)

# Estrae i numeri dalla domanda
match = re.match(r"(\d+)\s*\+\s*(\d+)", line)
if match:
    num1 = int(match.group(1))
    num2 = int(match.group(2))
    risultato = num1 + num2
    print("Risposta:", risultato)

    try:
        # Invia la risposta al processo il più velocemente possibile
        process.stdin.write(f"{risultato}\n")
        process.stdin.flush()
    except BrokenPipeError:
        print("⚠️ Il processo ha chiuso lo stdin prima della scrittura.")
    
    # Continua a leggere l'output per ottenere la flag (local_98)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print("Output:", output.strip())

else:
    print("❌ Domanda non riconosciuta!")

# Aspetta che il processo termini
process.wait()

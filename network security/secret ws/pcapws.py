import pyshark
import os

# File di input e output
pcap_file = 'challenge.pcap'
output_file = 'estratti_drawcommands.txt'
keylog_path = 'challenge-ssl.keys'

# Caricamento pcap con chiavi TLS
cap = pyshark.FileCapture(
    pcap_file,
    display_filter='tcp.port == 5002',  # puoi mettere 'http' o 'ws' più tardi
    #decode_as={'tcp.port==5002': 'ssl'},  # cambia la porta se necessario
    #custom_parameters=[
        #'-o', f'tls.keylog_file:{keylog_path}'
    #],
     override_prefs={'ssl.keylog_file': os.path.abspath('challenge-ssl.keys')},
)
# Lista per memorizzare i messaggi
estratti = []

print("[*] Analizzando pacchetti WebSocket...")

# Ciclo sui pacchetti
for pkt in cap:
    # Verifica se il pacchetto contiene un layer WebSocket
    if 'websocket' in [layer.layer_name.lower() for layer in pkt.layers]:
        print("  - Contiene un layer WebSocket")
        
        # Stampa tutti i campi del layer WebSocket
        if hasattr(pkt.websocket, '_all_fields'):
            for field, value in pkt.websocket._all_fields.items():
                print(f"    {field}: {value}")
        else:
            print("  - Nessun campo WebSocket disponibile")
    
    try:
        # Controlla se contiene dati testuali line-based
        if hasattr(pkt, 'websocket') and hasattr(pkt.websocket, 'payload_text'):
            testo = pkt.websocket.payload_text

            # Cerca "drawcommands" nel testo
            if 'drawcommands' in testo.lower():
                estratti.append(testo)
                print(f"[+] Trovato pacchetto: {testo[:80]}...")
    except Exception as e:
        # Salta pacchetti malformati
        continue

# Scrive su file
with open(output_file, 'w', encoding='utf-8') as f:
    for linea in estratti:
        f.write(linea + '\n')

print(f"\n[✓] Estrazione completata. Salvato in: {output_file}")

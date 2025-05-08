import os
import pyshark

pcap_path = 'challenge.pcap'
keylog_path = 'challenge-ssl.keys'
output_file = 'drawcommands_output.txt'

# Apri il file in modalità scrittura
with open(output_file, 'w', encoding='utf-8') as out:
    # Caricamento del pcap con le chiavi TLS
    cap = pyshark.FileCapture(
        pcap_path,
        display_filter='tcp.port == 5002',
        override_prefs={'ssl.keylog_file': os.path.abspath(keylog_path)},
    )

    for pkt in cap:
        print(f"\n=== Packet #{pkt.number} ({pkt.length} bytes) ===")

        for layer in pkt.layers:
            print(f" - Layer: {layer.layer_name}")

        if 'websocket' in pkt:
            print("[+] Layer WebSocket trovato.")
            try:
                for field, value in pkt.websocket._all_fields.items():
                    print(f"    [WS Field] {field}: {value}")
                    if "drawcommands" in value.lower():
                        print(">>> Trovato 'drawcommands' nel WebSocket field!")
                        out.write(f"[WebSocket] Packet #{pkt.number}: {value}\n")
            except Exception as e:
                print(f"[!] Errore nei campi WebSocket: {e}")

        if 'data-text-lines' in pkt:
            print("[+] Layer 'data-text-lines' presente.")
            try:
                lines_layer = pkt['data-text-lines']
                for attr in dir(lines_layer):
                    if not attr.startswith('_'):
                        val = getattr(lines_layer, attr)
                        if isinstance(val, str):
                            print(f"[Text Line Field] {attr}: {val}")
                            if 'drawcommands' in val.lower():
                                print(">>> Trovato 'drawcommands' in data-text-lines!")
                                out.write(f"[TextLines] Packet #{pkt.number}: {val}\n")
            except Exception as e:
                print(f"[!] Errore nel leggere il contenuto di 'data-text-lines': {e}")

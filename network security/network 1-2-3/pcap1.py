import pyshark

# Carica il file PCAP
cap = pyshark.FileCapture("nw-intro01.pcap")

# Stampa i primi 10 pacchetti
for packet in cap:
    print(f"Pacchetto #{packet.number}")
    #print(packet)  # Stampa informazioni di base
    if hasattr(packet, 'data'):
        print(f"Payload: {packet.data.data}")
        try:
            payload = bytes.fromhex(packet.data.data.replace(':', ''))
            print(f"Payload decodificato: {payload.decode('utf-8', errors='replace')}")
        except ValueError as e:
            print(f"Errore nella decodifica del payload: {e}")
    if hasattr(packet, 'ip'):
        print(f"IP Sorgente: {packet.ip.src} → IP Destinazione: {packet.ip.dst}")
    print("-" * 50)

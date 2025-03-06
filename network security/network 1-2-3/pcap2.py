import pyshark

# Carica il file PCAP
cap = pyshark.FileCapture("nw-intro02.pcap")

for i, packet in enumerate(cap):
        if hasattr(packet, 'eth'):
            print(f"MAC Sorgente: {packet.eth.src} → MAC Destinazione: {packet.eth.dst}")
        if hasattr(packet, 'data'):
            print(f"Payload: {packet.data.data}")
            data_length = len(packet.data.data)/2
            print(f"Dimensione pacchetto: {data_length} byte")
        print("-" * 50)
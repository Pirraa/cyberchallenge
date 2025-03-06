import pyshark

def count_unique_conversations(pcap_file):
    conversations = set()
    i=0
    
    # Carica il file pcap
    cap = pyshark.FileCapture(pcap_file, display_filter="ip")
    
    for packet in cap:
        i+=1
        print(f'packet {i}')
        try:
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            conversations.add((src_ip, dst_ip))
        except AttributeError:
            continue  # Salta i pacchetti non IP
    
    cap.close()
    
    print(f"Numero totale di conversazioni uniche: {len(conversations)}")
    for src, dst in conversations:
        print(f"{src} -> {dst}")

# Esempio di utilizzo
if __name__ == "__main__":
    pcap_file = "china.pcapng"  # Sostituisci con il tuo file
    count_unique_conversations(pcap_file)

import pyshark


def count_streams(pcap_file):
    i=0
    capture = pyshark.FileCapture(pcap_file)

    tcp_streams = set()
    udp_streams = set()
    
    for packet in capture:
        i+=1
        print(f'packet {i}')
        if 'TCP' in packet:
            tcp_streams.add(packet.tcp.stream)
        elif 'UDP' in packet:
            udp_streams.add(packet.udp.stream)

    print(f"Flussi TCP unici: {len(tcp_streams)}")
    print(f"Flussi UDP unici: {len(udp_streams)}")

# Esegui lo script con il tuo file PCAP
count_streams("china.pcapng")

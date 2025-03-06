import pyshark

# Funzione per cercare dati sensibili nei pacchetti
def check_sensitive_data(pcap_file):
    # Carica il file pcap
    cap = pyshark.FileCapture(pcap_file)

    # Liste di pattern da cercare nei pacchetti
    sensitive_keywords = [
        "password",
        "username",
        "token",
        "api",
        "secret",
        "admin",
        "cookie",
        "login",
        "authorization"
    ]

    # Crea una lista per raccogliere pacchetti sospetti
    suspicious_packets = []

    # Itera attraverso tutti i pacchetti
    for packet in cap:
        if 'HTTP' in packet:
            try:
                # Analizza la parte HTTP del pacchetto
                http_layer = packet.http

                # Verifica se ci sono parole chiave nei dati HTTP
                for keyword in sensitive_keywords:
                    if hasattr(http_layer, 'host') and keyword in str(http_layer):
                        suspicious_packets.append({
                            'packet': packet,
                            'url': http_layer.host,
                            'details': str(http_layer)
                        })

            except AttributeError:
                # Se il pacchetto non ha una layer HTTP, lo ignoriamo
                continue

    return suspicious_packets

# Funzione per stampare i risultati
def print_results(suspicious_packets):
    if not suspicious_packets:
        print("Nessun dato sensibile trovato.")
        return

    print("Dati sensibili trovati:")
    for packet in suspicious_packets:
        print(f"\nPachetto trovano sospetto: {packet['packet']}")
        print(f"URL: {packet['url']}")
        print(f"Dettagli: {packet['details']}")

if __name__ == "__main__":
    pcap_file = "leopardo.pcapng"  # Sostituisci con il nome del tuo file pcap
    suspicious_packets = check_sensitive_data(pcap_file)
    print_results(suspicious_packets)

import pyshark

# Carica il file PCAP e filtra solo i pacchetti USB HID
cap = pyshark.FileCapture('chall2.pcap')

hid_map = {
    0x04: 'A', 0x05: 'B', 0x06: 'C', 0x07: 'D', 0x08: 'E', 0x09: 'F',
    0x0A: 'G', 0x0B: 'H', 0x0C: 'I', 0x0D: 'J', 0x0E: 'K', 0x0F: 'L',
    0x10: 'M', 0x11: 'N', 0x12: 'O', 0x13: 'P', 0x14: 'Q', 0x15: 'R',
    0x16: 'S', 0x17: 'T', 0x18: 'U', 0x19: 'V', 0x1A: 'W', 0x1B: 'X',
    0x1C: 'Y', 0x1D: 'Z', 0x1E: '1', 0x1F: '2', 0x20: '3', 0x21: '4',
    0x22: '5', 0x23: '6', 0x24: '7', 0x25: '8', 0x26: '9', 0x27: '0',
    0x28: '⏎',  # Enter
    0x2C: ' ',  # Space
    0x2D: '-', 0x2E: '=', 0x2F: '[', 0x30: ']', 0x31: '\\',
    0x33: ';', 0x34: "'", 0x35: '`', 0x36: ',', 0x37: '.', 0x38: '/',
    0x2F + 0x80: '{', 0x30 + 0x80: '}'  # Parentesi graffe
}

def parse_hid_report(hid_data):
    """Estrae i codici HID dall'array e li converte in caratteri."""
    keys = hid_data.split(':')  # I dati HID arrivano come stringa esadecimale separata da ':'
    result = ""

    for key_hex in keys:
        key = int(key_hex, 16)  # Converte in intero
        if key in hid_map:
            result += hid_map[key]
    
    return result

for packet in cap:
    print(f"\n=== Pacchetto #{packet.number} ===")

    # Stampa tutti i layer effettivamente presenti nel pacchetto
    print("Layer presenti:", [layer.layer_name for layer in packet.layers])

    if hasattr(packet, 'data'):
        print(f"Layer DATA trovato! Contenuto: {packet.data}")
    else:
        print("⚠️ Nessun layer DATA trovato!")
cap.close()

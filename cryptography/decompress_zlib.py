import zlib

# Percorso al file zlib
file_path = 'extracted_at_0x3d3c7.zlib'

# Apre il file zlib in modalità binaria e lo decompone
with open(file_path, 'rb') as file:
    compressed_data = file.read()
    try:
        # Decompressione dei dati
        decompressed_data = zlib.decompress(compressed_data)
        
        # Prova a decodificare i dati come testo
        try:
            decoded_data = decompressed_data.decode('utf-8')
            print("Contenuto del file decompresso:")
            print(decoded_data)
        except UnicodeDecodeError:
            print("I dati decompressed non sono testo, sono dati binari.")
            # Se non è testo, salva i dati decompressed come file binario
            with open('decompressed_data.bin', 'wb') as output_file:
                output_file.write(decompressed_data)
            print("Dati decompressi salvati come 'decompressed_data.bin'.")
    except zlib.error as e:
        print(f"Errore nella decompressione del file: {e}")

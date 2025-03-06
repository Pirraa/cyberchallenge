import zlib

# Leggi il file compresso
with open('untraceable.zlib', 'rb') as f:
    compressed_data = f.read()

# Decompressione del file Zlib
decompressed_data = zlib.decompress(compressed_data)

# Salva i dati decompressi su un nuovo file
with open('file_decompressed.txt', 'wb') as f:
    f.write(decompressed_data)

# Se i dati decompressi sono in formato testo, puoi anche stamparli
print(decompressed_data.decode('utf-8'))  # Se il file è in formato testo

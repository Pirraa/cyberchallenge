import base64
import zipfile

# Chunks forniti (incluso il chunk mancante)
chunks = [
    "NOOP 1,UEsDBBQAAgAIANp",
    "NOOP 2,8wlBRaanrIQAAAD",
    "NOOP 3,0AAAAIABwAZmxhZ",
    "NOOP 4,y50eHRVVAkAA2xW",
    "NOOP 5,1l51VtZedXgLAAE",
    "NOOP 6,E6AMAAAToAwAAc3",
    "NOOP 7,b2DKkuyTAsjgeix",
    "NOOP 8,Pgcg7x03ESZcVEl",
    "NOOP 9,hOXm4+heywUAUEs",
    "NOOP 10,BAh4DFAACAAgA2n",
    "NOOP 11,zCUFFpqeshAAAAP",
    "NOOP 12,QAAAAgAGAAAAAAA",
    "NOOP 13,AQAAALSBAAAAAGZ",
    "NOOP 14,sYWcudHh0VVQFAA",
    "NOOP 15,NsVtZedXgLAAEE6",
    "NOOP 16,AMAAAToAwAAUEsF",
    "NOOP 17,BgAAAAABAAEATgA",
    "NOOP 18,AAGMAAAAAAA==",
]

# Estrai i dati Base64 dai chunk
base64_data = "".join([chunk.split(",")[1] for chunk in chunks])

# Decodifica la stringa Base64
try:
    decoded_data = base64.b64decode(base64_data)
    with open("flag.zip", "wb") as f:
        f.write(decoded_data)
    print("File ZIP salvato come 'flag.zip'")
except Exception as e:
    print(f"Errore durante la decodifica Base64: {e}")
    exit()

# Verifica se il file ZIP è valido
try:
    with zipfile.ZipFile("flag.zip", "r") as zip_ref:
        print("Il file ZIP è valido e contiene i seguenti file:")
        for file in zip_ref.namelist():
            print(f"- {file}")
except zipfile.BadZipFile:
    print("Il file ZIP è incompleto o corrotto. Tentativo di riparazione...")

    # Aggiungi manualmente la firma end-of-central-directory
    with open("flag.zip", "ab") as f:
        f.write(bytes.fromhex("50 4B 05 06 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"))
    print("Firma end-of-central-directory aggiunta manualmente.")

    # Verifica di nuovo il file ZIP
    try:
        with zipfile.ZipFile("flag.zip", "r") as zip_ref:
            print("Il file ZIP è stato riparato e contiene i seguenti file:")
            for file in zip_ref.namelist():
                print(f"- {file}")
    except zipfile.BadZipFile:
        print("Impossibile riparare il file ZIP. Verifica i chunk forniti.")
        exit()

# Estrai il contenuto del file ZIP
try:
    with zipfile.ZipFile("flag.zip", "r") as zip_ref:
        zip_ref.extractall()
        print("Contenuto del file ZIP estratto con successo.")
except Exception as e:
    print(f"Errore durante l'estrazione del file ZIP: {e}")
import pyshark
import jwt
from datetime import datetime

# Specifica il percorso del file PCAP da catturare
file_path = 'chall4.pcap'

# Crea un oggetto FileCapture
capture = pyshark.FileCapture(input_file=file_path, display_filter='http.request')

# Lista per memorizzare i token JWT
jwt_tokens = []

# Itera sui pacchetti catturati
for packet in capture:
    if 'http' in packet:
        http_layer = packet.http
        for field in http_layer.field_names:
            value = http_layer.get(field)
            if field == 'authorization' and value.startswith('Bearer '):
                token = value[len('Bearer '):]
                jwt_tokens.append(token)

# Rilascia le risorse
capture.close()

# Timestamp di riferimento per la validità del token
# Esempio di data e ora
data_ora = "2022-06-01 12:00:00"
# Converte la stringa in un oggetto datetime
data_ora_oggetto = datetime.strptime(data_ora, "%Y-%m-%d %H:%M:%S")
# Ottieni il timestamp
reference_timestamp = int(data_ora_oggetto.timestamp())


# Decodifica e stampa delle componenti dei token JWT
for token in jwt_tokens:
    try:
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        
        # Verifica i campi nbf e exp se presenti
        is_valid = True
        if 'nbf' in decoded_token and decoded_token['nbf'] > reference_timestamp:
            is_valid = False
        if 'exp' in decoded_token and decoded_token['exp'] < reference_timestamp:
            is_valid = False
        
        #Stampa il token solo se è valido
        if is_valid:
            print(f"Decoded JWT: {decoded_token}")
            if 'nbf' in decoded_token:
                nbf_time = datetime.fromtimestamp(decoded_token['nbf'], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                print(f"Not Before (nbf): {nbf_time}")
            if 'exp' in decoded_token:
                exp_time = datetime.fromtimestamp(decoded_token['exp'], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                print(f"Expiration Time (exp): {exp_time}")
            break  # Esci dal ciclo dopo aver trovato un token valido
        
    except jwt.DecodeError as e:
        print(f"Errore nella decodifica del token JWT: {e}")
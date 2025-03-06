def ascii_shift_decrypt(text, target="CCIT"):
    result = ""
    shifts = []  # Lista per memorizzare gli shift
    for i in range(len(target)):
        # Calcoliamo lo shift tra il carattere cifrato e quello in chiaro
        shift = ord(text[i]) - ord(target[i])
        shifts.append(shift)  # Salviamo lo shift
        if shifts[i] < 0:  # Se lo shift è negativo (ad esempio 'A' -> 'Z'), aggiustiamo
            shifts[i] += 26

    # Ora decriptiamo il testo con gli shift calcolati
    for i, char in enumerate(text):
        if char.isalpha():  # Consideriamo solo i caratteri alfabetici
            # Troviamo il valore ASCII del carattere
            char_code = ord(char)

            # Se il carattere è maiuscolo
            if char.isupper():
                # Applichiamo lo shift
                new_char_code = char_code - shifts[i % len(shifts)]
                if new_char_code < ord('A'):
                    new_char_code += 26
            else:
                # Se il carattere è minuscolo
                new_char_code = char_code - shifts[i % len(shifts)]
                if new_char_code < ord('a'):
                    new_char_code += 26

            result += chr(new_char_code)
        else:
            result += char  # Aggiungi caratteri non alfabetici senza modificarli

    return result

# Test con il messaggio cifrato
ciphertext = "TTZK{Xrzlj_Alczlj_Trvjri}"
decrypted_text = ascii_shift_decrypt(ciphertext)
print(decrypted_text)

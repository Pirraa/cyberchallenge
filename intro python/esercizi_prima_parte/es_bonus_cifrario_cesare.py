def cifra_messaggio(input_file_name, passo):
    file_name = input_file_name.split("/")[-1]
    output_file_name = "./encrypted_" + file_name

    with open(input_file_name, "r") as input_file, open(output_file_name, "wt") as output_file:
        for line in input_file:
            cipher_line = ""

            # Per ogni carattere che compone la riga, lo cifro e lo inserisco in una nuova stringa
            # che rappresenta la riga cifrata
            for char in line:
                char_cifrato = ord(char) + passo
                cipher_line += chr(char_cifrato)

            # Scrivo la linea cifrata all'interno di un nuovo file
            output_file.write(cipher_line)


def decifra_messaggio(input_file_name, passo):
    file_name = input_file_name.split("/")[-1]
    output_file_name = "./decrypted_" + file_name

    with open(input_file_name, "r") as input_file, open(output_file_name, "wt") as output_file:
        for line in input_file:
            decipher_line = ""

            # Per ogni carattere che compone la riga, lo cifro e lo inserisco in una nuova stringa
            # che rappresenta la riga cifrata
            for char in line:
                char_decifrato = ord(char) - passo
                decipher_line += chr(char_decifrato)

            # Scrivo la linea cifrata all'interno di un nuovo file
            output_file.write(decipher_line)


if __name__ == "__main__":
    print("Script Cifrario di Cesare")

    file_da_cifrare = input("Inserire il percorso del file da cifrare: ")
    passo = int(input("Inserire il valore del passo che verrà utilizzato per cifrare il messaggio: "))
    cifra_messaggio(file_da_cifrare, passo)

    file_da_decifrare = input("Inserire il percorso del file da decifrare: ")
    passo = int(input("Inserire il valore del passo che verrà utilizzato per decifrare il messaggio: "))
    decifra_messaggio(file_da_decifrare, passo)

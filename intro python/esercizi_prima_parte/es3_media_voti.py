def calcola_media(lista_studenti):
    for studente in lista_studenti:
        # Ogni "studente" è una tupla il cui primo elemento è il nome
        # dello studente, e il secondo è una lista che contiene tutti
        # i suoi voti. La media dei suoi voti si può calcolare facilmente
        # usando le funzioni sum() e len().
        somma_voti = sum(studente[1])
        media_voti = somma_voti / len(studente[1])

        print(f"Studente: {studente[0]}, Media voti: {media_voti}")


lista_studenti = []

with open("voti.txt", "rt") as file_voti:
    line = file_voti.readline()
    while line: # Vuol dire: "finchè ho letto qualcosa..."
        line = line.replace("\n", "") # Tolgo il carattere di "andata a capo" finale, per comodità (non per forza necessario)
        elementi = line.split() # Suddivido la riga in base agli spazi

        # Converto i voti da stringa a intero, in modo da poterli sommare con la funzione sum()
        lista_voti = []
        for voto in elementi[1:]:  # elementi[1:] è la lista elementi a partire dal secondo (il primo elemento è il nome dello studente)
            lista_voti.append(int(voto))  # Aggiungo i voti alla lista

        tupla_studente = (elementi[0], lista_voti) # È una tupla fatta da (nome, [voto1, voto2, ...])

        # print(f"Tupla studente: {tupla_studente}")
        lista_studenti.append(tupla_studente)

        line = file_voti.readline()

# Una volta usciti dal while vuol dire che si sono lette tutte le righe del file.
# Una volta lette tutte le righe, la lista di tuple è pronta e posso invocare
# la funzione per calcolare la media di ogni studente
calcola_media(lista_studenti)

"""
Nota: in questo esercizio abbiamo usato un ciclo while
per leggere un file invece di un ciclo for solo per
mostrare entrambe le modalità. Vanno bene entrambe.
"""

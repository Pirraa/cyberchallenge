diz_eta = {}

with open("dati.txt", "rt") as file_input:
    for linea in file_input:
        elementi = linea.split()
        nome = elementi[0]
        eta = int(elementi[1])

        if eta not in diz_eta:
            diz_eta[eta] = [nome]
        else:
            diz_eta[eta].append(nome)

print(diz_eta)

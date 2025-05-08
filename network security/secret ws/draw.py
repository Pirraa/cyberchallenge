import turtle

# Imposta finestra
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Disegno da coordinate")

# Inizializza turtle
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Centrare l'origine (opzionale, dipende da coordinate)
pen.penup()
pen.goto(-400, -300)
pen.pendown()

# Funzione per leggere e disegnare dal file
def disegna_da_file(nome_file):
    with open(nome_file, 'r') as file:
        for riga in file:
            dati = riga.strip().split(',')
            if len(dati) >= 4:
                try:
                    # Prende solo le ultime 4 coordinate
                    x1, y1, x2, y2 = map(int, dati[-4:])
                    pen.penup()
                    pen.goto(x1 - 350, 300 - y1)  # Inverti Y per il sistema turtle
                    pen.pendown()
                    pen.goto(x2 - 350, 300 - y2)
                except ValueError:
                    pass  # Salta righe non valide

# Esegui il disegno
disegna_da_file("drawcommands_numbers.txt")

# Mantieni la finestra aperta
turtle.done()

import requests

# Prima parte

res = requests.get("http://www.example.com")

with open("example.html", "wt") as output_file:
    output_file.write(res.text)

print("Pagina scritta sul file.")

# Seconda parte

data = {
    "userId": 12345,
    "title": "Fare l'esercizio sulla libreria Requests",
    "completed": True,
}
# Notare che non abbiamo specificato l'ID del todo,
# lo assegnerà automaticamente il sito e noi lo
# recupereremo accedendo alla risposta ottenuta

res = requests.post("http://jsonplaceholder.typicode.com/todos", data=data)

print(f"\nStato HTTP: {res.status_code}")
print(f"Risposta:\n{res.text}")
res_dizionario = res.json()  # È una classe "dict" di Python, un dizionario.
id_todo = res_dizionario["id"]
print(f"ID del todo inserito: {id_todo}")

res = requests.delete(f"http://jsonplaceholder.typicode.com/todos/{id_todo}")

print(f"\nStato HTTP: {res.status_code}")
print(f"Risposta:\n{res.text}")

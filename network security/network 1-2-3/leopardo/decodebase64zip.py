import base64

# Stringa Base64 dell'allegato ZIP (estratta dal messaggio)
base64_zip = """
UEsDBBQAAQAIABmKdlDUjcy25AAAAAUCAAAIAAAAZmxhZy50eHQYcOby79i3jTWYC7UZVJbp
IToyzKMenibecd/V4wDEIwKI4Ti0zGoSS0rqJLa3n6aAOUKeUmQuUrXb4doJ3ZJy4yG+Y1gb
W1/waWklAredll/B3Cv8g5IyzJ8RFpHmPR9NxDRFHzCe1MUEEGB/w7RMWD50M/It3Ga/eQIE
zt/He0QIe2A89wW06f9aq4bTE38WsMWhMoKZ7KRU6aiHc5a68cfuvmpDvhGC3TqCk7ACsg20
zToM0t5Q0u6kaHrmftXrBvECUYJUoIQjHy6qO4zp57vZ3zWEXtDGDnqI2C9NA0yXbXFQSwEC
PwAUAAEACAAZinZQ1I3MtuQAAAAFAgAACAAkAAAAAAAAACAAAAAAAAAAZmxhZy50eHQKACAA
AAAAAAEAGABylUhKZQDWAXKVSEplANYBc2pISmUA1gFQSwUGAAAAAAEAAQBaAAAACgEAAAAA
"""

# Rimuovi spazi e newline
base64_zip = base64_zip.replace("\n", "").replace(" ", "")

# Decodifica il Base64
zip_data = base64.b64decode(base64_zip)

# Scrivi il file ZIP decodificato su disco
with open("flag.zip", "wb") as f:
    f.write(zip_data)

print("File flag.zip estratto con successo!")

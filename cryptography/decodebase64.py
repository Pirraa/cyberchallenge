import re
import base64

# Funzione per estrarre la stringa base64 dall'HTML
def extract_base64_from_html(html_file):
    with open(html_file, 'r') as file:
        html_content = file.read()

    # Regex per trovare la stringa base64
    base64_pattern = r"data:image/png;base64,([A-Za-z0-9+/=]+)"
    match = re.search(base64_pattern, html_content)

    if match:
        return match.group(1)  # Restituisce la stringa base64 senza il prefisso
    else:
        raise ValueError("Base64 string not found in the HTML file.")

# Funzione per decodificare la stringa base64 e salvare l'immagine
def save_base64_image(base64_string, output_file):
    image_data = base64.b64decode(base64_string)
    
    with open(output_file, 'wb') as image_file:
        image_file.write(image_data)
    print(f"Image saved to {output_file}")

# Main
html_file = 'index2.html'  # Sostituisci con il tuo file HTML
output_image = 'output2.png'  # Nome del file di output

# Estrai la stringa base64 dal file HTML
base64_string = extract_base64_from_html(html_file)

# Decodifica e salva l'immagine
save_base64_image(base64_string, output_image)

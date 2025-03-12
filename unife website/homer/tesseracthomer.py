from PIL import Image
import pytesseract

# Carica l'immagine
image = Image.open("Homer.png")

# Estrai il testo
text = pytesseract.image_to_string(image)

print(text)

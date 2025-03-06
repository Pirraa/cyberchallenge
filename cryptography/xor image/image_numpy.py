import numpy as np
from PIL import Image

# Carica le immagini cifrate
enc_image1 = Image.open("flag_enc.png")
enc_image2 = Image.open("notflag_enc.png")

# Converte le immagini in array numpy
enc_image1_np = np.array(enc_image1)
enc_image2_np = np.array(enc_image2)

# Applica XOR tra le due immagini cifrate
result_np = np.bitwise_xor(enc_image1_np.astype(np.uint8), enc_image2_np.astype(np.uint8))

# Converte il risultato in immagine e lo salva
result_image = Image.fromarray(result_np)
result_image.save("xor_result.png")

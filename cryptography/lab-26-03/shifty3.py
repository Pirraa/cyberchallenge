def caesar_decrypt(ciphertext):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for key in range(1, 26):  # Try all possible keys (1 to 25)
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                shifted_index = (alphabet.index(char.lower()) - key) % 26
                decrypted_char = alphabet[shifted_index]
                plaintext += decrypted_char.upper() if char.isupper() else decrypted_char
            else:
                plaintext += char
        print(f"Key {key}: {plaintext}")

if __name__ == "__main__":
    ciphertext = input("Enter the ciphertext: ")
    caesar_decrypt(ciphertext)
# Lettura e conteggio delle stringhe criptate
crypted_counts = []
count = 0
with open("crypted.txt") as f:
    for line in f:
        if line.strip() == '-- end --':
            crypted_counts.append(count)
            count = 0
        else:
            count += 1
    if count > 0:
        crypted_counts.append(count)

print("File criptato")
for count in crypted_counts:
    print(count)

# Lettura e conteggio delle parole
words = []
with open("words.txt") as f:
    for word in f:
        words.append(word.strip())

words.sort()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_counts = {letter: 0 for letter in alphabet}

for word in words:
    first_letter = word[0]
    if first_letter in letter_counts:
        letter_counts[first_letter] += 1

print("File word")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")

# Determinazione della parola segreta
secret_word = ''
prefix = ''

for count in crypted_counts:
    found = False
    for letter in alphabet:
        if letter_counts[letter] == count:
            secret_word += letter
            prefix += letter
            found = True
            break
    if not found:
        print(f"Nessuna corrispondenza trovata per il conteggio: {count}")
        break

    # Aggiorna letter_counts per il nuovo prefisso
    letter_counts = {letter: 0 for letter in alphabet}
    for word in words:
        if word.startswith(prefix) and len(word) > len(prefix):
            next_letter = word[len(prefix)]
            if next_letter in letter_counts:
                letter_counts[next_letter] += 1

print("Parola segreta:", secret_word)
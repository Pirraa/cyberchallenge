import re

input_file = 'drawcommands_output.txt'
output_file = 'drawcommands_numbers.txt'

# Regex per trovare tutte le liste di numeri tra parentesi quadre
list_pattern = re.compile(r'\[(\d+(?:,\d+)*)\]')

with open(input_file, 'r', encoding='utf-8') as infile, \
     open(output_file, 'w', encoding='utf-8') as outfile:

    for line in infile:
        matches = list_pattern.findall(line)
        for match in matches:
            outfile.write(match + '\n')  # Scrivi ogni lista su una riga

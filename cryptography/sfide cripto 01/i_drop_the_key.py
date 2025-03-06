def swap_first_last(key):
    # Dividiamo la stringa in gruppi di 4
    groups = [key[i:i+4] for i in range(0, len(key), 4)]
    
    # Modifichiamo ogni gruppo scambiando il primo e l'ultimo carattere
    swapped_groups = []
    for group in groups:
        if len(group) == 4:
            swapped_group = group[-1] + group[1:3] + group[0]  # Scambia prima e ultima lettera
        else:
            swapped_group = group  # Non modificare se il gruppo è più corto di 4
        swapped_groups.append(swapped_group)
    
    # Ritorniamo la stringa concatenata
    flag = ''.join(swapped_groups)
    return flag

# La chiave che hai fornito
key = "TCICmI_{_d343_m4}s!s"

# Generiamo la flag
flag = swap_first_last(key)
print(flag)

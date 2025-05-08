from pwn import *

binary = ELF('./nextgen_safe')
print(hex(binary.symbols['print_safe_contents']))  # dovrebbe stampare 0x8049276

# Patch main per chiamare print_safe_contents
# Trova offset giusto nel main (tipicamente subito all'inizio)
offset = binary.symbols['main']

# Patch: call 0x08049276
patched = asm(f"call {hex(binary.symbols['print_safe_contents'])}")

# Scrivi la patch
binary = bytearray(open('./nextgen_safe', 'rb').read())
binary[offset:offset + len(patched)] = patched

# Salva nuovo binario
with open('./patched_safe', 'wb') as f:
    f.write(binary)

print("✅ Binario patchato salvato come 'patched_safe'")

import binascii

# I blocchi di testo cifrato forniti in formato esadecimale
ciphertexts = [
    "03f2794833cf53f9dcc2206609fd9c3b27269f7b8f38c79301db2f3ac2c764ab3ac0d7ad075ba191598664241d3d6e7ca113276612cbe476bf7ec544564dad",
    "1eee3b1b7cd753abd18b3e6a44fd913a3d6f853ddb29cdc640de2d3cd39369b47f8dd9a0420fa8d4148a73321d7a643af40e3a7a03cfe53ab570dc4e5f5aa3fa01fe7df7cd7986e15b31bafccbc4563160a1",
    "3def6f1c7cc25eb8c6cc28234cec9e37272c843a8931c1c705db6c3dc19369b33ac0d7b94e48a09a1883202c196e727be605737d198ae876ab76cc0c4757e2fa4ea773eccd7f86f91e30bbf8c1c65278",
    "35ef684828c957ad88c7226c42fedd2d662188349670d6dc40c8223dd3db78a97f90ddb95440a7da59ac43082866752ab13f3e2019d3d622ed7a865f1242",
    "1efc3c1c34c416aac9c6282342e8847f6e3ccc2e8835c6930dc63e3787c775ba31c0d7a5444ae5d41b8e646108756874e61373631ec6e576b476c55c5651a3ef00ba3ce08269c7e0572eb2aec3db06207dadba75a21277",
    "16e93c1b33ce58f9c9d86d7a46f8dd376639897b9e3ec1dc04cc2872c69370be2c93d9ac420fbe9d0d8720205c7a686ce40e736416cea576a87fc743441feafa4ebf6bf8943c8efa5327bae7c5c043386badb37eaa5e3fe7b98c0de3564243",
    "03f2794833cf53f9dcc2206609fd9c3b27269f7b883f82c009c43c3ec29369b33e9498a4494ae998109b742d193d6373f5403c7257c9e824b97bd05f4051e6fd1dfe7ff8833c85e55b23b5aecdc007"
]

# Converto ogni blocco esadecimale in un array di byte
ciphertexts_bytes = [binascii.unhexlify(ciphertext) for ciphertext in ciphertexts]

# Funzione per XOR tra due blocchi
def xor_blocks(block1, block2):
    return bytes([b1 ^ b2 for b1, b2 in zip(block1, block2)])

# Provo a XOR-izzare i blocchi tra loro
for i in range(len(ciphertexts_bytes) - 1):
    # XOR del blocco i-esimo con il successivo
    xor_result = xor_blocks(ciphertexts_bytes[i], ciphertexts_bytes[i + 1])
    
    # Stampa il risultato della XOR (in esadecimale e testo ASCII)
    print(f"XOR tra blocco {i} e blocco {i + 1}:")
    print(f"Hex: {binascii.hexlify(xor_result)}")
    print(f"ASCII: {xor_result.decode('ascii', errors='ignore')}")
    print("-" * 60)

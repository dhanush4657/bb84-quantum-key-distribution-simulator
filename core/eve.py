import random

def intercept(bits, alice_bases):
    eve_bases = [random.choice(["+", "x"]) for _ in range(len(bits))]
    eve_bits = []

    for i in range(len(bits)):
        if eve_bases[i] == alice_bases[i]:
            eve_bits.append(bits[i])
        else:
            eve_bits.append(random.randint(0, 1))

    return eve_bits, eve_bases
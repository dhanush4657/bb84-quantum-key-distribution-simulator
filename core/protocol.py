import random

def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def generate_bases(n):
    return [random.choice(["+", "x"]) for _ in range(n)]

def measure_bits(bits, alice_bases, bob_bases):
    result = []

    for i in range(len(bits)):
        if alice_bases[i] == bob_bases[i]:
            result.append(bits[i])
        else:
            result.append(random.randint(0, 1))

    return result

def shared_key(bits, alice_bases, bob_bases):
    key = []

    for i in range(len(bits)):
        if alice_bases[i] == bob_bases[i]:
            key.append(bits[i])

    return key
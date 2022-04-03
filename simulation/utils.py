import random

# generate bits array
def generate_bits(quantity: int):
    return [random.randint(0, 1) for _ in range(quantity)]

# calculate Bit Error Rate
def calculate_ber(input: list, output: list):
    errors = 0

    for i in range(len(input)):
        errors += input[i] * output[i]

    return errors / len(input)

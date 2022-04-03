import random

# Generate random array of bits
def generate_random_data(quantity: int):
    return [random.randint(0, 1) for _ in range(quantity)]

# Calculate Bit Error Rate
def calculate_ber(input: list, output: list):
    errors = 0

    for i in range(len(input)):
        errors += input[i] * output[i]

    return errors / len(input)

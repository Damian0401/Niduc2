
# Triple input bits
def encode(input: list) -> list:
    output = []
    
    for i in input:
        for _ in range(0, 3):
            output.append(i)

    return output

# Decode input bits
def decode(input: list) -> list:
    output = []

    for i in range(0, len(input), 3):
        output.append(int(sum(input[i:i+3]) / 2))

    return output
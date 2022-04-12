import komm

# Dimension: 4
# Length: 7
bch = komm.BCHCode(3, 1)

# Code input bits
def encode(input: list) -> list:
    if len(input) % 4 != 0:
        raise ValueError()

    output = []
    for i in range(0, len(input), 4):
        output.extend(bch.encode(input[i:i+4]))

    return output

# Decode input bits
def decode(input: list) -> list:
    if len(input) % 7 != 0:
        raise ValueError()

    output = []
    for i in range(0, len(input), 7):
        output.extend(bch.decode(input[i:i+7]))

    return output
import numpy

# Code input bits
def encode(input: list) -> list:
    if len(input) % 4 != 0:
        raise ValueError()

    output = []
    for i in range(0, len(input), 4):
        word = code_word(input[i:i+4])
        output.extend(word)

    return output

# Decode input bits
def decode(input: list):
    if len(input) % 7 != 0:
        raise ValueError()

    output = []
    for i in range(0, len(input), 7):
        output.extend(correct_error(input[i:i+7]))

    return output

# Code single 4 bit word
def code_word(input: list) -> list:
    if len(input) != 4:
        raise ValueError()

    input_matrix = numpy.array([input])
    G = numpy.array([[1,0,0,0,1,1,1],[0,1,0,0,1,0,1],[0,0,1,0,1,1,0],[0,0,0,1,0,1,1]])

    code = input_matrix.dot(G)
    code = code % 2

    return code[0]

# Calculate syndrome
def calculate_syndrome(input: list) -> list:
    if len(input) != 7:
        raise ValueError()

    input_matrix = numpy.array([input])
    H = numpy.array([[1,1,1],[1,0,1],[1,1,0],[0,1,1],[1,0,0],[0,1,0],[0,0,1]])

    syndrome = input_matrix.dot(H)
    syndrome = syndrome % 2

    return syndrome[0]

# Check index of the error if exists
def check_error_index(syndrome: list) -> int:
    if len(syndrome) != 3:
        raise ValueError()

    H = [[1,1,1],[1,0,1],[1,1,0],[0,1,1],[1,0,0],[0,1,0],[0,0,1]]

    for index, row in enumerate(H):
        if syndrome[0] == row[0] and syndrome[1] == row[1] and syndrome[2] == row[2]:
            return index

    return -1

# Find error and correct it if exists
def correct_error(input: list) -> list:
    if len(input) != 7:
        raise ValueError()

    syndrome = calculate_syndrome(input)

    error_index = check_error_index(syndrome)

    if error_index != -1:
        input[error_index] = (input[error_index] + 1) % 2

    return input[0:4]
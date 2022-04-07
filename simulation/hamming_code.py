import numpy

# Code input bits
def code_hamming(input: list) -> list:
    length = len(input)
    output = []

    if length % 4 != 0:
        raise ValueError()

    for i in range(0, length, 4):
        word = code_word(input[i:i+4])
        output.extend(word)

    return output

# Decode input bits
def decode_hamming():
    pass

def code_word(input: list) -> list:
    if len(input) != 4:
        raise ValueError()

    inputMatrix = numpy.array([input])
    G = numpy.array([[1,0,0,0,1,1,1],[0,1,0,0,1,0,1],[0,0,1,0,1,1,0],[0,0,0,1,0,1,1]])

    code = inputMatrix.dot(G)
    code = code % 2

    return code[0]
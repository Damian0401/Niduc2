from hamming_code import *


def main():
    # Raw data
    word = [0,0,0,1,1,0,0,0]
    print(f'data: {word}')

    # Encode data using hamming algorithm 
    word_encoded = code_hamming(word)
    print(f'encoded data: {word_encoded}')

    # Create 2 errora
    word_encoded[1] = (word_encoded[1] + 1) % 2
    word_encoded[10] = (word_encoded[10] + 1) % 2
    print(f'encoded data with error: {word_encoded}')

    # Decode data & correct errors
    word_decoded = decode_hamming(word_encoded)
    print(f'data: {word_decoded}')

if __name__ == '__main__':
    main()
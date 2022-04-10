import hamming_code
import triple_code
import utils
import komm

def main():
    # Create transmission channel
    bsc = komm.BinarySymmetricChannel(0.1)

    # Generate n * 8 (n bytes) random data
    data = utils.generate_random_data(1000 * 8)

    # Encode data
    hamming_encoded_data = hamming_code.encode(data)
    triple_encoded_data = triple_code.encode(data)

    # Transfer data
    hamming_after_transmission = bsc(hamming_encoded_data)
    triple_after_transmission = bsc(triple_encoded_data)

    # Decode data
    hamming_decoded_data = hamming_code.decode(hamming_after_transmission)
    triple_decoded_data = triple_code.decode(triple_after_transmission)

    # Calculate Bit Error Rate
    hamming_ber = utils.calculate_ber(data, hamming_decoded_data)
    triple_ber = utils.calculate_ber(data, triple_decoded_data)

    # Print results
    print(f'Hamming code: {hamming_ber * 100}%')
    print(f'Triple code: {triple_ber * 100}%')

    
if __name__ == '__main__':
    main()
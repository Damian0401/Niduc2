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

    # Calculate data size
    hamming_additional_size = len(hamming_encoded_data) / len(data)
    triple_additional_size = len(triple_encoded_data) / len(data)

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
    print(f'Hamming code:: BER: {hamming_ber * 100:.2f}%, data size: {hamming_additional_size * 100}%')
    print(f'Triple code:: BER: {triple_ber * 100:.2f}%, data size: {triple_additional_size * 100}%')
    
if __name__ == '__main__':
    main()
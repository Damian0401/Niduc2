import hamming_code
import triple_code
import utils
import channels

def main():
    # Create transmission channels
    bsc = channels.binary_symmetric(0.1)
    gec = channels.gilbert_elliot(0.9, 0.1, 0.25)

    # Generate n * 8 (n bytes) random data
    data = utils.generate_random_data(10000 * 8)

    # Encode data
    hamming_encoded_data = hamming_code.encode(data)
    triple_encoded_data = triple_code.encode(data)

    # Calculate data size
    hamming_additional_size = len(hamming_encoded_data) / len(data)
    triple_additional_size = len(triple_encoded_data) / len(data)

    # Transfer data through Binnary Symetric Channel
    hamming_after_bsc = bsc(hamming_encoded_data)
    triple_after_bsc = bsc(triple_encoded_data)

    # Transfer data through Gilbert-Elliot Channel
    hamming_after_gec = gec(hamming_encoded_data)
    triple_after_gec = gec(triple_encoded_data)

    # Decode data
    hamming_decoded_bsc = hamming_code.decode(hamming_after_bsc)
    triple_decoded_bsc = triple_code.decode(triple_after_bsc)
    hamming_decoded_gec = hamming_code.decode(hamming_after_gec)
    triple_decoded_gec = triple_code.decode(triple_after_gec)

    # Calculate Bit Error Rate for BSC
    hamming_bsc_ber = utils.calculate_ber(data, hamming_decoded_bsc)
    triple_bsc_ber = utils.calculate_ber(data, triple_decoded_bsc)

    # Calculate Bit Error Rate for GEC
    hamming_gec_ber = utils.calculate_ber(data, hamming_decoded_gec)
    triple_gec_ber = utils.calculate_ber(data, triple_decoded_gec)

    # Print results
    print(f'Hamming code message size: {hamming_additional_size * 100:.2f}%, Triple code message size: {triple_additional_size * 100:.2f}%')
    print(f'Hamming code:: BER: {hamming_bsc_ber * 100:.2f}%, channel: Binnary Symetric')
    print(f'Triple code:: BER: {triple_bsc_ber * 100:.2f}%, channel: Binnary Symetric')
    print(f'Hamming code:: BER: {hamming_gec_ber * 100:.2f}%, channel: Gilbert-Elliot')
    print(f'Triple code:: BER: {triple_gec_ber * 100:.2f}%, channel: Gilbert-Elliot')
    
if __name__ == '__main__':
    main()
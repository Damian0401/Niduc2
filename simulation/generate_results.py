import channels
import utils
import bch_code
import triple_code
import hamming_code


gec = channels.gilbert_elliot(0.75, 0.1, 0.35)
bsc = channels.binary_symmetric(0.25)

data_amount = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
file_path = './simulation/results/'

def simulate(code, channel, data_amount: list, file_name: str):
    file = open(file_name, 'w')
    file.write('amount [bytes];BER [%]\n')

    for amount in data_amount:
        data = utils.generate_random_data(amount * 8)

        encoded_data = code.encode(data)

        data_after_transmission = channel(encoded_data)

        decoded_data = code.decode(data_after_transmission)

        ber_rate = utils.calculate_ber(data, decoded_data)

        file.write(f'{amount};{ber_rate * 100:.2f}\n')

    file.close()

    print('Done.')

def main():
    simulate(hamming_code, bsc, data_amount, file_path + 'hamming_bsc.csv')
    simulate(hamming_code, gec, data_amount, file_path + 'hamming_gec.csv')
    simulate(triple_code, bsc, data_amount, file_path + 'triple_bsc.csv')
    simulate(triple_code, gec, data_amount, file_path + 'triple_gec.csv')
    simulate(bch_code, bsc, data_amount, file_path + 'bch_bsc.csv')
    simulate(bch_code, gec, data_amount, file_path + 'bch_gec.csv')

if __name__ == '__main__':
    main()
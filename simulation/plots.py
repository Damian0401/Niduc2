import pandas as pd
from matplotlib import pyplot as plt

file_path = './simulation/results/'

def show_plot(files_names: dict):
    headers = ['amount [bytes]', 'BER [%]']
    for file_name, data_name in files_names.items():
        data = pd.read_csv(file_path + file_name, sep = ';')
        x = data[headers[0]]
        y = data[headers[1]]
        plt.plot(x, y, label = data_name)
    plt.legend()
    plt.show()

def display():
    print('Select option:')
    print('1 <- All plots')
    print('2 <- Hamming code plots')
    print('3 <- Triple code plots')
    print('4 <- BCH code plots')
    print('5 <- Binnary symetric channel plots')
    print('6 <- Gilbert-Elltiot channel plots')

    selected_option = int(input())

    if selected_option == 1:
        files_names = {
            'hamming_bsc.csv' : 'Hamming - Binnary symetric',
            'hamming_gec.csv' : 'Hamming - Gilbert Elliot',
            'triple_bsc.csv' : 'Triple - Binnary symetric',
            'triple_gec.csv' : 'Triple - Gilbert Elliot',
            'bch_bsc.csv' : 'BCH - Binnary symetric',
            'bch_gec.csv' : 'BCH - Gilbert Elliot',
        }
        show_plot(files_names)
        return

    if selected_option == 2:
        files_names = {
            'hamming_bsc.csv' : 'Hamming - Binnary symetric',
            'hamming_gec.csv' : 'Hamming - Gilbert Elliot',
        }
        show_plot(files_names)
        return

    if selected_option == 3:
        files_names = {
            'triple_bsc.csv' : 'Triple - Binnary symetric',
            'triple_gec.csv' : 'Triple - Gilbert Elliot',
        }
        show_plot(files_names)
        return

    if selected_option == 4:
        files_names = {
            'bch_bsc.csv' : 'BCH - Binnary symetric',
            'bch_gec.csv' : 'BCH - Gilbert Elliot',
        }
        show_plot(files_names)
        return

    if selected_option == 5:
        files_names = {
            'hamming_bsc.csv' : 'Hamming - Binnary symetric',
            'triple_bsc.csv' : 'Triple - Binnary symetric',
            'bch_bsc.csv' : 'BCH - Binnary symetric',
        }
        show_plot(files_names)
        return

    if selected_option == 6:
        files_names = {
            'hamming_gec.csv' : 'Hamming - Gilbert Elliot',
            'triple_gec.csv' : 'Triple - Gilbert Elliot',
            'bch_gec.csv' : 'BCH - Gilbert Elliot',
        }
        show_plot(files_names)
        return

if __name__ == '__main__':
    display()
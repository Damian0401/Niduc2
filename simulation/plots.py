import pandas

file_path = './simulation/results/'

def show_plot(file_name: str):
    pass

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
        show_plot('hamming_bsc.csv')
        show_plot('hamming_gec.csv')
        show_plot('triple_bsc.csv')
        show_plot('triple_gec.csv')
        show_plot('bch_bsc.csv')
        show_plot('bch_gec.csv')
        return

    if selected_option == 2:
        show_plot('hamming_bsc.csv')
        show_plot('hamming_gec.csv')
        return

    if selected_option == 3:
        show_plot('triple_bsc.csv')
        show_plot('triple_gec.csv')
        return

    if selected_option == 4:
        show_plot('bch_bsc.csv')
        show_plot('bch_gec.csv')
        return

    if selected_option == 5:
        show_plot('hamming_bsc.csv')
        show_plot('triple_bsc.csv')
        show_plot('bch_bsc.csv')
        return

    if selected_option == 6:
        show_plot('hamming_gec.csv')
        show_plot('triple_gec.csv')
        show_plot('bch_gec.csv')
        return

if __name__ == '__main__':
    display()
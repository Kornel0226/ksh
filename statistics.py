import matplotlib.pyplot as plt
from pandas import DataFrame


def man_female_population(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Év'], data['A férfi népesség száma, január 1., ezer fő'], label='Férfi népesség')
    plt.plot(data['Év'], data['A női népesség száma, január 1., ezer fő'], label='Női népesség')
    plt.xlabel('Év')
    plt.ylabel('Népesség (ezer fő)')
    plt.title('Férfi és női népesség változása az évek során')
    plt.grid(True)
    plt.legend()
    plt.savefig('nepesseg_vonaldiagramm.png')


def man_woman_average_age(data: DataFrame):

    data = data[data["Év"] >= 1990]

    plt.figure(figsize=(10, 6))
    plt.plot(data['Év'], data['A férfiak átlagéletkora, év január 1.'], label='Férfi átlagéletkor')
    plt.plot(data['Év'], data['A nők átlagéletkora, év  január 1.'], label='Női átlagéletkor')
    plt.xlabel('Év')
    plt.ylabel('Átlagéletkor')
    plt.title('Férfi és női átlagéletkor az évek során')
    plt.grid(True)
    plt.legend()
    plt.savefig('atlageletkor_vonaldiagramm.png')

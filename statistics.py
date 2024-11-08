import matplotlib.pyplot as plt
def testx(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Év'], data['A férfi népesség száma, január 1., ezer fő'], label='Férfi népesség')
    plt.plot(data['Év'], data['A női népesség száma, január 1., ezer fő'], label='Női népesség')
    plt.xlabel('Év')
    plt.ylabel('Népesség (ezer fő)')
    plt.title('Férfi és női népesség változása az évek során')
    plt.grid(True)
    plt.legend()
    plt.savefig('nepesseg_vonaldiagramm.png')


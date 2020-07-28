# Biblioteki do opracowywania wykresów
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
# Pozostałe biblioteki
import numpy as np


def metoda_wyznaczników(tabx, taby, tabw):
    W = tabx[0] * taby[1] - tabx[1] * taby[0]
    Wx = tabx[0] * tabw[1] - tabx[1] * tabw[0]
    Wy = taby[0] * tabw[1] - taby[1] * tabw[0]

    x = Wx/W
    y = -Wy/W

    return({"a1" : x, "a0" : y})


def main():
    tab1 = []
    tab2 = []
    tabw = []
    tabx = [2.10, 6.22, 7.17, 10.52, 13.68]
    taby = [2.9, 3.83, 5.98, 5.71, 7.74]

    tab1.append(len(tabx))
    tab1.append(sum(tabx))

    tab2.append(sum(tabx))
    tab2.append(sum([item**2 for item in tabx]))

    tabw.append(sum(taby))
    print("SPR DLA JULI: "  + str(tabw[0]))
    tabw.append(sum([item * taby[i] for i, item in enumerate(tabx)]))

    wynik = metoda_wyznaczników(tab1, tab2, tabw)
    print(wynik)

    a0 = wynik["a0"]
    a1 = wynik["a1"]
    pkt = np.linspace(2, 14, 100)
    nasze = [a0 + a1*i for i in pkt]

    print(nasze)
    plt.plot(pkt, nasze, color='blue', label="aproksymacja")
    plt.plot(tabx, taby, 'ro', color='red', label="punkty podane")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
# Biblioteki do opracowywania wykresów
import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use('ggplot')
# Pozostałe biblioteki
import numpy as np
from math import sqrt

def interpolacja_Lagrangea(n, x, tabx, taby):
    Wn = 0.0
    for i in range(0,n):
        p = 1.0
        for j in range(0,n):
            if(i != j):
                p = p * (x - tabx[j]) / (tabx[i] - tabx[j])
        Wn = (Wn + taby[i] * p)
    return(Wn)

def example_plot(ax, fontsize=12):
    ax.plot([1, 2])

    ax.locator_params(nbins=3)
    ax.set_xlabel('liczba', fontsize=fontsize)
    ax.set_ylabel('pierwiatek z liczby', fontsize=fontsize)
    ax.set_title('Title', fontsize=fontsize)


def main():
    taby = [1.0, 2.0, 3.0]
    tabx = [1.0, 8.0, 27.0]
    x = 16.0

    wn = interpolacja_Lagrangea(3, x, tabx, taby)
    print(wn)
    """
    tabxa = [-5, -4, -3, -2]
    tabya = []
    for liczba in tabxa:
        print(liczba)
        tabya.append(1/(liczba**2+1))

    tabxb = [-2, -1, 0]
    tabyb = []
    for liczba in tabxb:
        print(liczba)
        tabyb.append(1/(liczba**2+1))

    tabxc = [0, 1, 2]
    tabyc = []
    for liczba in tabxc:
        print(liczba)
        tabyc.append(1 / (liczba ** 2 + 1))

    tabxd = [2, 3, 4, 5]
    tabyd = []
    for liczba in tabxd:
        print(liczba)
        tabyd.append(1/(liczba**2+1))

    a = np.linspace(-5, -2, 300)
    b = np.linspace(-2, 0, 400)
    c = np.linspace(0, 2, 200)
    d = np.linspace(2, 5, 300)
    wna = interpolacja_Lagrangea(len(tabxa), a, tabxa, tabya)
    wnb = interpolacja_Lagrangea(len(tabxb), b, tabxb, tabyb)
    wnc = interpolacja_Lagrangea(len(tabxc), c, tabxc, tabyc)
    wnd = interpolacja_Lagrangea(len(tabxd), d, tabxd, tabyd)
    #print(f"Wartość pierwiastka w punkcie {x} wynosi {wn}.")

    tabx = tabxa+tabxb+tabxc+tabxd
    taby= tabya+tabyb+tabyc+tabyd
    x = np.linspace(-5, 5, 1000)
    wartosci_dokladne = []
    for i in x:
        wartosci_dokladne.append(1/(i**2+1))

    plt.plot(a, wna, label = "Przedział od -5 do -2")
    plt.plot(b, wnb, label= "Przedział od -2 do 0")
    plt.plot(c, wnc, label="Przedział od 0 do 2")
    plt.plot(d, wnd, label= "Przedział od 2 do 5")
    plt.plot(tabx, taby, 'ro', color='b')
    plt.plot(x, wartosci_dokladne, label = "Wynik dokładny")
    plt.text(2, 0.6, "Autor: Edyta Mróz")
    plt.title('Porównanie funkcji dokładnej i sklejanej')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()
    """

    """
    plt.plot(x, wartosci_dokladne)
    plt.text(1, 0.9, "Autor: Edyta Mróz")
    plt.title('Wynik dokładny (0,1.5)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

    plt.plot(x, wn)
    plt.text(1, 0.9, "Autor: Edyta Mróz")
    plt.title('Przybliżenie (0,1.5)')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()


    """

    x = np.linspace(1, 15, 15)
    wartosci_dokladne = []
    c = 0.1
    for i in x:
        wartosci_dokladne.append(c*2)
        c = c *2

    adas = []
    for i in x:
        adas.append(2**i)

    plt.plot(x, wartosci_dokladne, label="2")
    plt.plot(x, adas, label="adasiowe")
    plt.title("Wykresik Adasia")
    plt.show()

if __name__ == "__main__":
    main()
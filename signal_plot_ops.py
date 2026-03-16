import matplotlib.pyplot as plt


def load_signal_from_txt(cesta):
    hodnoty = []

    subor = open(cesta, "r")

    for riadok in subor:
        cislo = float(riadok.strip())
        hodnoty.append(cislo)

    subor.close()

    return hodnoty


def signal_min(hodnoty):
    minimum = hodnoty[0]

    for h in hodnoty:
        if h < minimum:
            minimum = h

    return minimum


def signal_max(hodnoty):
    maximum = hodnoty[0]

    for h in hodnoty:
        if h > maximum:
            maximum = h

    return maximum


def signal_avg(hodnoty):
    suma = 0

    for h in hodnoty:
        suma = suma + h

    priemer = suma / len(hodnoty)

    return priemer


def plot_signal(hodnoty):
    plt.plot(hodnoty)
    plt.title("Signal")
    plt.xlabel("Vzorky")
    plt.ylabel("Hodnota")
    plt.show()


if __name__ == "__main__":

    signal = load_signal_from_txt("ekg_signal.txt")

    print("Minimum:", signal_min(signal))
    print("Maximum:", signal_max(signal))
    print("Priemer:", signal_avg(signal))

    plot_signal(signal)
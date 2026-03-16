import matplotlib.pyplot as plt

def vykresli(kruz1, kruz2):
    fig, ax = plt.subplots()

    c1 = plt.Circle((kruz1["x"], kruz1["y"]), kruz1["r"], fill=False, color="blue")
    c2 = plt.Circle((kruz2["x"], kruz2["y"]), kruz2["r"], fill=False, color="red")

    ax.add_patch(c1)
    ax.add_patch(c2)

    ax.set_aspect("equal")
    ax.set_xlim(min(kruz1["x"]-kruz1["r"], kruz2["x"]-kruz2["r"]) - 1,
                max(kruz1["x"]+kruz1["r"], kruz2["x"]+kruz2["r"]) + 1)
    ax.set_ylim(min(kruz1["y"]-kruz1["r"], kruz2["y"]-kruz2["r"]) - 1,
                max(kruz1["y"]+kruz1["r"], kruz2["y"]+kruz2["r"]) + 1)

    plt.title("Kružnice a ich prienik")
    plt.show()
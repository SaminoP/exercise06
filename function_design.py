def analyze_password(heslo,
                     minimalna_dlzka=8,
                     vyzaduje_cislo=True,
                     vyzaduje_velke_pismeno=True,
                     vyzaduje_symbol=False,
                     zakazane_slova=None):

    symboly = "!@#$%^&*()-_=+[]{};:,.?"

    if zakazane_slova is None:
        zakazane_slova = ['heslo', 'password', '1234']

    pocet_pravidiel = 0
    splnene_pravidla = 0
    chybajuce_pravidla = []

    pocet_pravidiel += 1
    if len(heslo) >= minimalna_dlzka:
        splnene_pravidla += 1
    else:
        chybajuce_pravidla.append("min_length")

    if vyzaduje_cislo:
        pocet_pravidiel += 1
        if any(znak.isdigit() for znak in heslo):
            splnene_pravidla += 1
        else:
            chybajuce_pravidla.append("digit")

    if vyzaduje_velke_pismeno:
        pocet_pravidiel += 1
        if any(znak.isupper() for znak in heslo):
            splnene_pravidla += 1
        else:
            chybajuce_pravidla.append("upper")

    if vyzaduje_symbol:
        pocet_pravidiel += 1
        if any(znak in symboly for znak in heslo):
            splnene_pravidla += 1
        else:
            chybajuce_pravidla.append("symbol")

    pocet_pravidiel += 1
    male_heslo = heslo.lower()

    if any(slovo in male_heslo for slovo in zakazane_slova):
        chybajuce_pravidla.append("banned_word")
    else:
        splnene_pravidla += 1

    percento_skore = int((splnene_pravidla / pocet_pravidiel) * 100)
    silne_heslo = len(chybajuce_pravidla) == 0

    return silne_heslo, percento_skore, chybajuce_pravidla


print(analyze_password("abcDEF12", 8, True, True, True, ['admin', 'root']))
print("Kratsie ale menej prehladne")

print(analyze_password("Test123!", 8, vyzaduje_symbol=True))
print("Zmena pravidla je jasnejšia.")

print(analyze_password("Test1234", vyzaduje_symbol=False))
print("Symbol nie je povinný. Nastavenie je dobre viditeľné.")

print(analyze_password("Login123!", zakazane_slova=["admin", "user", "test"]))
print("Použitý vlastný zoznam zakázaných slov.")
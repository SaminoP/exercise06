from circle_stats import ma_prienik
from circles_intersection_draw import vykresli


kruz1 = {"x": 0, "y": 0, "r": 2}
kruz2 = {"x": 3, "y": 0, "r": 1}

vysledok = ma_prienik(kruz1, kruz2)

if vysledok["is_intersection"]:
    print("pretínajú sa a majú", vysledok["intersections_count"], "prieniky")
else:
    print("nepretínajú sa")


vykresli(kruz1, kruz2)
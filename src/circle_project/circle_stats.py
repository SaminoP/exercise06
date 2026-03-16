from math import sqrt, isclose

def sucet_polomerov(r1, r2):
    return r1 + r2

def euklid_vzdialenost(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    return sqrt(dx*dx + dy*dy)

def ma_prienik(kruz1, kruz2):
    x1 = kruz1["x"]
    y1 = kruz1["y"]
    r1 = kruz1["r"]

    x2 = kruz2["x"]
    y2 = kruz2["y"]
    r2 = kruz2["r"]

    d = euklid_vzdialenost(x1, y1, x2, y2)
    r_suc = sucet_polomerov(r1, r2)
    r_diff = abs(r1 - r2)

    # rozhodovanie
    if d > r_suc:

        return {"is_intersection": False, "intersections_count": 0}
    elif isclose(d, r_suc) or isclose(d, r_diff):

        return {"is_intersection": True, "intersections_count": 1}
    elif d < r_diff:

        return {"is_intersection": False, "intersections_count": 0}
    else:

        return {"is_intersection": True, "intersections_count": 2}


# tesy

from circle_stats import ma_prienik, sucet_polomerov



# Test 1
k1 = {"x":0, "y":0, "r":2}
k2 = {"x":2, "y":0, "r":2}
print("Test 1:", ma_prienik(k1,k2))

# Test 2
k1 = {"x":1, "y":1, "r":3}
k2 = {"x":4, "y":3, "r":2}
print("Test 2:", ma_prienik(k1,k2))

# Test 3
k1 = {"x":0, "y":0, "r":2}
k2 = {"x":4, "y":0, "r":2}
print("Test 3:", ma_prienik(k1,k2))

# Test 4
k1 = {"x":0, "y":0, "r":5}
k2 = {"x":3, "y":0, "r":2}
print("Test 4:", ma_prienik(k1,k2))

# Test 5
k1 = {"x":0, "y":0, "r":2}
k2 = {"x":10, "y":0, "r":3}
print("Test 5:", ma_prienik(k1,k2))


print("Test radius_sum:", sucet_polomerov(3,4))
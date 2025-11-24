import math

def equazione_secondo_grado(fattore_a : float, fattore_b : float, fattore_c : float) -> list:
    risposte = []
    delta = pow(fattore_b, 2) - 4 * fattore_a * fattore_c
    if fattore_a == 0.0:
        return ["Error!"]
    if delta < 0.0:
        risposte.append("0 soluzioni")
    elif delta == 0.0:
        ans = (- fattore_b) / 2 * fattore_a
        risposte.append(ans)
    elif delta > 0:
        ans1 = ((-fattore_b) - math.sqrt(delta)) / (2 * fattore_a)
        ans2 = ((-fattore_b) + math.sqrt(delta)) / (2 * fattore_a)
        risposte.append(ans1)
        risposte.append(ans2)
    return risposte

def calcolo_angolo_lato_opposto_ipotenusa(lato_opposto : float, ipotenusa : float) -> float:
    if lato_opposto <= 0.0 or ipotenusa <= 0.0:
        return ["Error!"]
    sin_ang = lato_opposto / ipotenusa
    ang = math.asin(sin_ang)
    return math.degrees(ang)

def calcolo_angolo_lato_adiacente_ipotenusa(lato_adiacente : float, ipotenusa : float) -> float:
    if lato_adiacente <= 0.0 or ipotenusa <= 0.0:
        return ["Error!"]
    sin_ang = lato_adiacente / ipotenusa
    ang = math.acos(sin_ang)
    return math.degrees(ang)

def calcolo_ipotenusa(cateto1 : float, cateto2 : float) -> float:
    fattore_1 = pow(cateto1, 2)
    fattore_2 = pow(cateto2, 2)
    print(fattore_1 + fattore_2)
    return math.sqrt(fattore_1 + fattore_2)


print(equazione_secondo_grado(1, 7, -8))
print(calcolo_angolo_lato_adiacente_ipotenusa(40, 60))
print(calcolo_ipotenusa(4, 3))
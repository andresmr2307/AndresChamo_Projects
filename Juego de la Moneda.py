import random
import time



lanzamientos = 0
cara = "Cara"
sello = "Sello"

cara_y_sello = [(cara), (sello)]
while input("Quieres lanzar una moneda? [y|n]: \n") == 'y':
    print(random.choice(cara_y_sello))
    time.sleep(.5)
    lanzamientos += 1


else:
    print("Haz lanzado la moneda",lanzamientos,"veces")
    print("Blaos")

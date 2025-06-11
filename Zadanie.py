#zadanie1
def liczba_przeciwna():
   number = float(input("podaj licze rzeczywista różną od zera"))
   if number != 0:
       return number * -1
   else:
       while number == 0:
            number = float(input("podaj licze rzeczywista różną od zera"))
            if number != 0:
                return number * -1

absNumber = liczba_przeciwna()
print(f"Liczba przeciwna wynosi {absNumber}")

#zadanie2
print("\n")
def pole_trojkata(triangleSide, triangleHeight):
    return triangleSide * triangleHeight / 2

getSide = int(input("podaj dlugosć boku"))
if getSide > 0:
    side = getSide
else:
    while getSide < 0 or getSide == 0:
        getSide = int(input("podaj dlugos boku(wieksza od zera)"))
        if getSide > 0:
            side = getSide

height = 5

triangleArea = pole_trojkata(side, height)
print(f"Pole trójkąta wynosi: {triangleArea}")





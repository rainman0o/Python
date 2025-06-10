
#zmienne

from tarfile import FIFOTYPE


number1 = 10 
number2 = 9


#operacje na zmiennych
sumNumber = number1 + number2
print("suma number1 + number2  wynosi: ", sumNumber)
print("\n")

#instrukcja if
if number1 % 2 == 1:
    print("nieparzysta")
elif number1 % 2 == 0:
    print("parzysta")
else:
    print("to nie jest liczba")

#petle 
print("\n")
for i in range(1, 15, 2):
    print(i)

print("\n")

for j in range(10, 1, -1):
    print(j)

print("\n")
numberForLoop = 1

while numberForLoop < 10:
    print(numberForLoop)
    numberForLoop += 1


#stringi operacje
stringExample = "to jest String"

stringExample = stringExample.upper()
print(stringExample)

stringExample = stringExample.lower()
print(stringExample)

stringExample = "to jest String"
stringExample = stringExample.replace("to jest String", "Lancuch znakow")
print(stringExample)
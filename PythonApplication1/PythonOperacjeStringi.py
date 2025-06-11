from traceback import format_tb

stringExample = "Hello, World!"

#wyświetlanie
print(stringExample)

#wyświelanie typu
print(type(stringExample))

#małe duże litery
print(stringExample.lower())
print(stringExample.upper())

#wyświetlanie indexów
print(stringExample[1])
print(stringExample[2:8])
print(stringExample[-5: -2])

#wyswietlanie petlami
for x in range (1, len(stringExample)):
    if x % 2 == 0 and stringExample[x]  == 'o':
        print(stringExample[x])

print("\n")

for x in stringExample:
    print(x)

#sprawdzanie czy dane slowo jest w stringu
if 'Hello' in stringExample:
    print("słowo hello jest w tym str")
else:
    print("nie ma tego słowa")


if 'Przyklad' not in stringExample:
    print("nie ma tego słowa w tym str")
else:
    print("to słowo jest w tym str")

#usuwanie białych znaków
stringExample2 = "  Hello, World!     "
print(stringExample2.strip())

#zmianianie znaków
print(stringExample.replace("Hello", "Witaj"))
print(stringExample.replace("World!", "Świecie"))

#rozdzielenie słów
newString = stringExample.split(",")
print(newString[0])
print(newString[1])
print(newString[0][4])
print(newString[1][4])
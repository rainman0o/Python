def calculator(firstNumber, secondNumber, operation):
    if operation == '+':
        return firstNumber + secondNumber
    elif operation == '-':
        return firstNumber - secondNumber
    elif operation == '*':
        return firstNumber * secondNumber
    elif operation == '/':
        if secondNumber != 0:
            return firstNumber / secondNumber
        else:
            print("nie dziel przez zero")
    elif operation == 'pow':
        return pow(firstNumber, secondNumber)

firstNumber = int(input("Podaj pierwszą liczę: "))

operation = ''
operationsSign = {'+', '-', '/', '*', 'pow'}
while operation not in operationsSign:
        operation = (input("jakie dzilanie chcesz wykonać?(+, -, *, /)"))

secondNumber = int(input("Podaj druga liczbe: "))

print(calculator(firstNumber, secondNumber, operation))



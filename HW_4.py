def calculator(value1, value2, action):
    if action == '+':
        return value1 + value2
    elif action == '-':
        return value1 - value2
    elif action == '*':
        return value1 * value2
    elif action == '/':
        if value2 != 0:
            return value1 / value2
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Ошибка: недопустимое действие"

value1 = float(input("Введите значение 1: "))
value2 = float(input("Введите значение 2: "))
action = input("Введите действие (+, -, *, /): ")

result = calculator(value1, value2, action)

print("Результат:", result)
input("press any key to close window")

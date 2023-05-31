N = int(input("Введите число N: "))

total_sum = N * (N + 1) // 2

for _ in range(N - 1):
    card = int(input("Введите номер оставшейся карточки: "))
    total_sum -= card

print("Потерянная карточка:", total_sum)
input("press any key to close window")

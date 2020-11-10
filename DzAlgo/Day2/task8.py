summ = int(input("Введите количество чисел:"))
number = int(input("Введите цифру для подсчёта:"))

count = 0

for i in range(1, summ + 1):
    mass = int(input(f'Ввод числа {i}:'))
    while mass > 0:
        if mass % 10 == number:
            count += 1
        mass = mass // 10

print(f'Цифра {number} была введена {count} раз(а)')

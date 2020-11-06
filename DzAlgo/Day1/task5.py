first = ord(input('Буква №1'))
second = ord(input('Буква №2, но отличная от №1 '))
first = first - ord('a') + 1
second = second - ord('a') + 1
print(f"Порядковый номер буквы №1 = {first}, №2 = {second}")
print(f"Число букв между буквами №1 и №2 = {abs(first - second) - 1}")
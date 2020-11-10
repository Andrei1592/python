n = int(input('Введите элементы для сложения:'))
element = 1
summ = 0

for i in range(n):
    summ += element
    element /= -2
print(summ)
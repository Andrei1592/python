print('Введите три разных целых числа')

a = int(input('1ое число '))
b = int(input('2ое число '))
c = int(input('3ее число '))

if b < a < c or c < a < b:
    print("Среднее", a)
elif a < b < c or c < b < a:
    print("Среднее", b)
else:
    print("Среднее", c)

print(5 in range(1, 10))
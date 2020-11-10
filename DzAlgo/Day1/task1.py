number = int(input("Введите трехзначного число "))

a = number // 100
b = number % 100 // 10
c = number % 10

numberSumm = a + b + c
summs = a * b * c
print(f"Сумма цифр вашего трехзначного числа = {numberSumm}")
print(f"Произведение цифр вашего трехзначного числа = {summs}")
1

# другое решение
sum = str(number)
summary = 0
numberSumm = 1
for i in number:
    numberSumm += int(i)
    summs *= int(i)
print(f"Сумма цифр вашего трехзначного числа = {numberSumm}")
print(f"Произведение цифр вашего трехзначного числа = {summs}")
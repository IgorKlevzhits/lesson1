number_str = input("Введите число трехзначное число: ")
number = int(number_str)
sum = 0

sum += number % 10
number //= 10

sum += number % 10
number //= 10

sum += number % 10
number //= 10

print(f"Сумма цифр числа {number_str} равна - {sum}")
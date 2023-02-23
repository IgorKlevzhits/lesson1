# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

ticket_number_str = input("Введите шестизначный номер билета: ")
first_sum = 0
second_sum = 0

ticket_number = int(ticket_number_str)

first_sum += ticket_number % 10
ticket_number //= 10

first_sum += ticket_number % 10
ticket_number //= 10

first_sum += ticket_number % 10
ticket_number //= 10

second_sum += ticket_number % 10
ticket_number //= 10

second_sum += ticket_number % 10
ticket_number //= 10

second_sum += ticket_number % 10
ticket_number //= 10

if first_sum == second_sum:
    print(f"Билет с номером {ticket_number_str} - счастливый!")
else:
    print(f"Билет с номером {ticket_number_str} - несчастливый!")
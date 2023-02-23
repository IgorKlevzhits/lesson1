cranes_number = int(input("Введите количество готовых журавлей: "))
cranes_made_boys = 0
cranes_made_girl = 0

if cranes_number % 6 != 0:
    print("Кто-то из детей врёт!")
else:
    cranes_made_boys = int(cranes_number / 6)
    cranes_made_girl = int(cranes_made_boys * 4)
    print(f"Петя и Сережа сделали по {cranes_made_boys} журавлей, а Катя {cranes_made_girl} журавлей")
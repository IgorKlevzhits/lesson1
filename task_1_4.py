# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

chocolate_height = int(input("Введите высоту шоколадки: "))
chocolate_width = int(input("Введите ширину шоколадки: "))
sum_pieces_chocolate = chocolate_height * chocolate_width
number_pieces_chocolate = int(input("Сколько долек вы хотите отломать? "))

if (number_pieces_chocolate % chocolate_height == 0 or number_pieces_chocolate % chocolate_width == 0) and (sum_pieces_chocolate >= number_pieces_chocolate):
    print("У вас всё получится!")
else:
    print("Это нереально!")
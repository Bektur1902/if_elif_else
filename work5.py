print('Problem5:')

a = int(input('Введите число:'))

if a%2 == 0:
	print('Четное')

elif a%2 != 0:
	print('Не четное')

if a%3 == 0:
	print('Да')

elif a%3 != 0:
	print('Нет')

if a**2 < 1000:
	print('меньшее 1000')

elif a**2 > 1000:
	print('Больше 1000')
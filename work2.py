print ('Problem22:')

a = int(input('Введите число a:'))
b = int(input('Введите число b:'))
c = int(input('Введите число c:'))

if a > b and a > c:
	print('Наибольшее число', a)

	if b > c:
		print('Наименьшее число', c)

	elif b < c:
		print('Наименьшее число', b)
	
	else:
		print(b, c, 'Наименьшие числа')

elif b > a and b > c:
	print('Наибольшее число', b)

	if a > c:
		print('Наименьшее число', c)

	elif a < c:
		print('Наименьшее число', a)

	else:
		print(a, c, 'Наименьшие числа')

elif c > a and c > b:
	print('Наибольшее число', c)

	if a > b: 
		print('Наименьшее число', b)

	elif a < b:
		print('Наименьшее число', a)
	else:
		print(a, b, 'Наименьшие числа')

else:
	print('Все числа равны')







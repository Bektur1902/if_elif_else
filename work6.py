print('Problem 3')

a = int(input('Введите число от 0 до 100: '))

if a in range(0, 21) or a in range(57, 100):
	print('Число разрешенно')
else:
	print('Число запрешенно')
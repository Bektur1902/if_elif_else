print('Problem15:')

a = 17391 % 17
b = 546 % 17
c = 934 % 17

if a < b and a < c:
	print('меньше всего', a)
	if b < c and b < a:
		print('меньше всего', b)
else:
	print('меньше всего', c)
while True:
	try:
		a, b = input() .split()
		a = int(a)
		b = int(b)
		c = a ^ b
		print(c)
	except EOFError:
		break
